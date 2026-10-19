#!/usr/bin/env python3
"""Build Excel-compatible models with live formulas.

Output: models/excel/speculators_desk_core.xlsx

Every sheet uses native Excel formulas (no macros) so the reader can audit and
change inputs. tests/test_excel.py recalculates the workbook with LibreOffice
(headless) and checks key cells against the Python library.

Input cells are blue font; formulas are black (a common modeling convention).
"""

from __future__ import annotations

import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "models" / "excel" / "speculators_desk_core.xlsx"

BLUE = Font(color="0000CC")
BOLD = Font(bold=True)
HDR = PatternFill("solid", fgColor="DDDDDD")


def _inputs(ws, rows, start=3):
    """Write label/value/note rows; values in column B are inputs (blue)."""
    for i, (label, value, note) in enumerate(rows, start=start):
        ws.cell(i, 1, label)
        c = ws.cell(i, 2, value)
        c.font = BLUE
        if note:
            ws.cell(i, 3, note)
    return start + len(rows)


def _title(ws, text):
    ws["A1"] = text
    ws["A1"].font = Font(bold=True, size=13)
    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 60


def sheet_readme(wb):
    ws = wb.active
    ws.title = "README"
    _title(ws, "The Speculator's Desk — Core Models")
    notes = [
        "Blue cells are inputs; black cells are formulas. Change inputs only.",
        "Rates are entered as decimals (0.065 = 6.5%). Payments are monthly in arrears unless stated.",
        "Excel PMT returns a negative value for a positive principal; formulas here pass -principal to show positive payments.",
        "Excel NPV discounts its first argument; formulas use =CF0+NPV(rate,CF1:CFn).",
        "Each sheet cites the textbook chapter and the Python function that reproduces it.",
        "Hypothetical inputs only. Replace with sourced data before any real decision.",
    ]
    for i, n in enumerate(notes, start=3):
        ws.cell(i, 1, n)


def sheet_loan(wb):
    ws = wb.create_sheet("Loan")
    _title(ws, "Loan amortization — Ch. 10 | sdesk.tvm.amortization_schedule")
    _inputs(ws, [("Principal ($)", 8_400_000, "Ch. 1 §1.6 warehouse loan"),
                 ("Nominal annual rate", 0.065, "monthly rate = rate/12"),
                 ("Amortization (years)", 30, ""),
                 ("Payments per year", 12, "")])
    ws["A8"], ws["B8"] = "Periodic rate", "=B4/B6"
    ws["A9"], ws["B9"] = "Number of payments", "=B5*B6"
    ws["A10"], ws["B10"] = "Payment", "=PMT(B8,B9,-B3)"
    ws["A11"], ws["B11"] = "Annual debt service", "=B10*B6"
    ws["A12"], ws["B12"] = "Loan constant", "=B11/B3"
    ws["A13"], ws["B13"] = "Balance after 120 payments (closed form)", "=-FV(B8,120,-B10,B3)"
    ws["A14"], ws["B14"] = "Balance after 120 payments (schedule)", "=G136"
    ws["A15"], ws["B15"] = "Effective annual rate", "=EFFECT(B4,B6)"
    hdr = ["Period", "Begin", "Payment", "Interest", "Principal", "End"]
    # schedule in columns B..G starting row 16 (header) to keep column A for labels
    for j, h in enumerate(hdr):
        cell = ws.cell(16, 2 + j, h)
        cell.font, cell.fill = BOLD, HDR
    for k in range(1, 361):
        r = 16 + k
        ws.cell(r, 2, k)
        ws.cell(r, 3, "=B3" if k == 1 else f"=G{r - 1}")
        ws.cell(r, 4, "=$B$10")
        ws.cell(r, 5, f"=C{r}*$B$8")
        ws.cell(r, 6, f"=D{r}-E{r}")
        ws.cell(r, 7, f"=C{r}-F{r}")
    ws["A378"], ws["B378"] = "Sum of principal (should equal loan)", "=SUM(F17:F376)"


def sheet_debt_sizing(wb):
    ws = wb.create_sheet("DebtSizing")
    _title(ws, "Loan sizing: LTV / DSCR / debt yield — Ch. 10 | sdesk.cre.max_loan")
    _inputs(ws, [("NOI ($)", 1_000_000, ""), ("Value ($)", 16_000_000, ""),
                 ("Rate", 0.07, ""), ("Amortization (years)", 30, ""),
                 ("Max LTV", 0.65, ""), ("Min DSCR", 1.25, ""), ("Min debt yield", 0.09, "")])
    ws["A11"], ws["B11"] = "Loan constant", "=PMT(B5/12,B6*12,-1)*12"
    ws["A12"], ws["B12"] = "Max loan — LTV", "=B4*B7"
    ws["A13"], ws["B13"] = "Max loan — DSCR", "=B3/B8/B11"
    ws["A14"], ws["B14"] = "Max loan — debt yield", "=B3/B9"
    ws["A15"], ws["B15"] = "Max loan (binding)", "=MIN(B12:B14)"
    ws["A16"], ws["B16"] = "Binding constraint", '=INDEX({"LTV","DSCR","Debt yield"},MATCH(B15,B12:B14,0))'
    ws["A17"], ws["B17"] = "Resulting DSCR", "=B3/(B15*B11)"


def sheet_loaded_cap(wb):
    ws = wb.create_sheet("LoadedCap")
    _title(ws, "Direct cap with property-tax reassessment — Ch. 9, Case A | sdesk.cre.loaded_cap_value")
    _inputs(ws, [("NOI before property tax ($)", 607_927.24, "Case A normalized"),
                 ("Market cap rate", 0.095, "on NOI after reserve and reassessed tax"),
                 ("Tax rate", 0.023, ""), ("Assessment ratio (assessed/price)", 0.85, ""),
                 ("Seller's current tax bill ($)", 78_200, "")])
    ws["A9"], ws["B9"] = "Effective tax on price t", "=B5*B6"
    ws["A10"], ws["B10"] = "Loaded cap rate c + t", "=B4+B9"
    ws["A11"], ws["B11"] = "Value V = N/(c+t)", "=B3/B10"
    ws["A12"], ws["B12"] = "Reassessed tax", "=B9*B11"
    ws["A13"], ws["B13"] = "NOI after tax", "=B3-B12"
    ws["A14"], ws["B14"] = "Check: NOI after tax / V", "=B13/B11"
    ws["A15"], ws["B15"] = "Naive value (seller's tax bill)", "=(B3-B7)/B4"
    ws["A16"], ws["B16"] = "Overstatement", "=B15-B11"


def sheet_hotel(wb):
    ws = wb.create_sheet("HotelRevenue")
    _title(ws, "Hotel room revenue and occupancy sensitivity — Ch. 11 | sdesk.hotel")
    _inputs(ws, [("Rooms", 120, ""), ("Occupancy", 0.72, ""), ("ADR ($)", 125, ""), ("Days", 365, "")])
    ws["A8"], ws["B8"] = "Available room-nights", "=B3*B6"
    ws["A9"], ws["B9"] = "Rooms sold", "=B8*B4"
    ws["A10"], ws["B10"] = "Room revenue", "=B9*B5"
    ws["A11"], ws["B11"] = "RevPAR", "=B10/B8"
    ws["A12"], ws["B12"] = "Revenue lost from -3 occupancy points", "=0.03*B8*B5"


def sheet_bond(wb):
    ws = wb.create_sheet("Bond")
    _title(ws, "Bond price, duration, DV01 — Ch. 6 | sdesk.fixed_income")
    _inputs(ws, [("Settlement", "2026-01-15", "use coupon-date settlement to avoid accrued interest"),
                 ("Maturity", "2036-01-15", ""), ("Coupon", 0.04, ""), ("Yield", 0.045, ""),
                 ("Frequency", 2, "")])
    ws["A9"], ws["B9"] = "Price per 100", "=PRICE(DATEVALUE(B3),DATEVALUE(B4),B5,B6,100,B7,1)"
    ws["A10"], ws["B10"] = "Macaulay duration", "=DURATION(DATEVALUE(B3),DATEVALUE(B4),B5,B6,B7,1)"
    ws["A11"], ws["B11"] = "Modified duration", "=MDURATION(DATEVALUE(B3),DATEVALUE(B4),B5,B6,B7,1)"
    ws["A12"], ws["B12"] = "Price at yield + 1bp", "=PRICE(DATEVALUE(B3),DATEVALUE(B4),B5,B6+0.0001,100,B7,1)"
    ws["A13"], ws["B13"] = "Price at yield - 1bp", "=PRICE(DATEVALUE(B3),DATEVALUE(B4),B5,B6-0.0001,100,B7,1)"
    ws["A14"], ws["B14"] = "DV01 per 100 (central difference)", "=(B13-B12)/2"
    ws["A15"], ws["B15"] = "Price via PV (cross-check)", "=PV(B6/B7,10*B7,-B5/B7*100,-100)"
    ws["C10"] = ("Built-in DURATION; LibreOffice's implementation can differ slightly from Excel. "
                 "B17-B18 compute duration explicitly from the cash flows.")
    # explicit cash-flow table: periods 1..20 in E..H
    for j, h in enumerate(["Period k", "t (years)", "Cash flow", "PV", "t x PV"]):
        c = ws.cell(2, 5 + j, h)
        c.font, c.fill = BOLD, HDR
    for k in range(1, 21):
        r = 2 + k
        ws.cell(r, 5, k)
        ws.cell(r, 6, f"=E{r}/$B$7")
        ws.cell(r, 7, f"=$B$5/$B$7*100+IF(E{r}=20,100,0)")
        ws.cell(r, 8, f"=G{r}/(1+$B$6/$B$7)^E{r}")
        ws.cell(r, 9, f"=F{r}*H{r}")
    ws["A16"], ws["B16"] = "Price (sum of PVs)", "=SUM(H3:H22)"
    ws["A17"], ws["B17"] = "Macaulay duration (explicit)", "=SUM(I3:I22)/B16"
    ws["A18"], ws["B18"] = "Modified duration (explicit)", "=B17/(1+B6/B7)"


def sheet_scenarios(wb):
    ws = wb.create_sheet("Ch01_Scenarios")
    _title(ws, "Expected vs realized return — Example 1.1 | tests/test_ch01_examples.py")
    _inputs(ws, [("Price ($)", 7_800_000, ""), ("Buyer closing cost %", 0.015, ""), ("Selling cost %", 0.03, "")])
    ws["A6"], ws["B6"] = "All-in basis", "=B3*(1+B4)"
    hdr = ["Scenario", "Prob", "NOI Y1", "NOI Y2", "Gross sale", "Net sale", "CF0", "CF1", "CF2", "Profit", "IRR"]
    for j, h in enumerate(hdr, start=1):
        c = ws.cell(8, j, h)
        c.font, c.fill = BOLD, HDR
    data = [("Good", 0.55, 780_000, 850_000, 9_400_000), ("Base", 0.30, 760_000, 800_000, 8_600_000),
            ("Bad", 0.15, 650_000, 560_000, 6_400_000)]
    for i, row in enumerate(data, start=9):
        for j, v in enumerate(row, start=1):
            c = ws.cell(i, j, v)
            if j > 1:
                c.font = BLUE
        ws.cell(i, 6, f"=E{i}*(1-$B$5)")
        ws.cell(i, 7, "=-$B$6")
        ws.cell(i, 8, f"=C{i}")
        ws.cell(i, 9, f"=D{i}+F{i}")
        ws.cell(i, 10, f"=SUM(G{i}:I{i})")
        ws.cell(i, 11, f"=IRR(G{i}:I{i})")
    ws["A13"], ws["B13"] = "Expected profit", "=SUMPRODUCT(B9:B11,J9:J11)"
    ws["A14"], ws["B14"] = "Std. deviation of profit", "=SQRT(SUMPRODUCT(B9:B11,(J9:J11-B13)^2))"
    ws["A15"], ws["B15"] = "Expected IRR", "=SUMPRODUCT(B9:B11,K9:K11)"
    ws["A16"], ws["B16"] = "E[CF1]", "=SUMPRODUCT(B9:B11,H9:H11)"
    ws["A17"], ws["B17"] = "E[CF2]", "=SUMPRODUCT(B9:B11,I9:I11)"
    ws["A18"], ws["B18"] = "CF0", "=-B6"
    ws["C18"], ws["D18"], ws["E18"] = "=B18", "=B16", "=B17"
    ws["A19"], ws["B19"] = "IRR of expected flows (C18:E18)", "=IRR(C18:E18)"
    for col in range(2, 12):
        ws.column_dimensions[get_column_letter(col)].width = 14


def build(path: Path = OUT) -> Path:
    wb = Workbook()
    sheet_readme(wb)
    sheet_loan(wb)
    sheet_debt_sizing(wb)
    sheet_loaded_cap(wb)
    sheet_hotel(wb)
    sheet_bond(wb)
    sheet_scenarios(wb)
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return path


if __name__ == "__main__":
    p = build(Path(sys.argv[1]) if len(sys.argv) > 1 else OUT)
    print(f"wrote {p}")
