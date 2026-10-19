"""Run the SQL schema, sample data, and named queries in SQLite and check them
against Python calculations."""

import sqlite3
from pathlib import Path

import pytest

from sdesk import markets as mk

SQL = Path(__file__).resolve().parents[1] / "models/sql"


def load_queries():
    text = (SQL / "03_queries.sql").read_text()
    out, name, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith("-- name:"):
            if name:
                out[name] = "\n".join(buf)
            name, buf = line.split(":", 1)[1].strip(), []
        elif name:
            buf.append(line)
    out[name] = "\n".join(buf)
    return out


@pytest.fixture()
def con():
    c = sqlite3.connect(":memory:")
    c.executescript((SQL / "01_schema.sql").read_text())
    c.executescript((SQL / "02_sample_data.sql").read_text())
    return c


def test_hotel_kpis(con):
    q = load_queries()["hotel_t12_kpis"]
    row = con.execute(q, {"property_id": 1}).fetchone()
    sold = 1830 + 1600 + 1450 + 1500 + 1560 + 1910
    avail = 2542 * 4 + 2460 + 2296
    rev = 214110 + 184000 + 162400 + 169500 + 180960 + 229200
    assert row[3] == pytest.approx(sold / avail)
    assert row[4] == pytest.approx(rev / sold)
    assert row[5] == pytest.approx(rev / avail)
    assert row[5] == pytest.approx(row[3] * row[4])


def test_position_pnl_respects_multipliers(con):
    rows = {r[1]: r for r in con.execute(load_queries()["position_pnl"]).fetchall()}
    assert rows["ES"][5] == pytest.approx(mk.futures_pnl(5000.0, 4910.75, 3, 50))
    assert rows["GC"][5] == pytest.approx(mk.futures_pnl(2400.0, 2445.0, 2, 100, side=-1))
    assert rows["EURUSD"][5] == pytest.approx(mk.fx_pnl(2_000_000, 1.0850, 1.0720))
    assert rows["ES"][7] == pytest.approx(-15_000)


def test_implied_caps(con):
    rows = con.execute(load_queries()["implied_cap_rates"]).fetchall()
    assert rows[1][5] == pytest.approx(560000 / 6100000)
    assert rows[1][6] == pytest.approx(560000 / 6850000)
    assert rows[1][8] == 1


def test_daily_returns(con):
    rows = [r for r in con.execute(load_queries()["daily_returns"]).fetchall() if r[0] == "ES"]
    assert rows[0][3] is None
    assert rows[1][3] == pytest.approx(4985.25 / 5000 - 1)
