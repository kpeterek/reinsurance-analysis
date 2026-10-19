"""Case G numbers as stated in case_G.md and case_G_rubric.md."""

import importlib.util
from pathlib import Path

import pytest

from sdesk import tvm

R = pytest.approx
_P = Path(__file__).resolve().parents[1] / "cases/hypothetical/case_G_buying_the_debt/case_g_model.py"
_spec = importlib.util.spec_from_file_location("case_g_model", _P)
m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(m)


def test_reference_points():
    assert m.AS_IS_NOI / m.AS_IS_CAP == R(36_000_000)
    assert m.STABILIZED_NOI / m.STABILIZED_CAP == R(49_600_000)
    assert m.stabilized_sale_net() == R(48_608_000)
    per_unit = {"upb": 153_846, "asis": 115_385, "note": 105_769, "note_allin": 106_250,
                "reo": 120_192, "reo_allin": 121_995, "stab": 155_795}
    vals = {"upb": m.UPB, "asis": 36e6, "note": m.NOTE_PRICE, "note_allin": m.NOTE_PRICE + m.NOTE_CLOSING,
            "reo": m.REO_PRICE, "reo_allin": m.REO_PRICE * (1 + m.REO_CLOSING), "stab": m.stabilized_sale_net()}
    for k, v in per_unit.items():
        assert round(vals[k] / m.UNITS) == v
    assert m.NOTE_PRICE / m.UPB == R(0.6875)
    assert m.REO_PRICE * 1.015 == R(38_062_500)
    assert round(m.REO_PRICE / 36e6, 4) == 1.0417
    assert round((38_062_500 - 33_150_000) / 1e6, 1) == 4.9


def test_ownership_flows():
    f = m.ownership_flows(m.AS_IS_NOI)
    assert len(f) == 24
    assert round(f[0]) == 29_653
    assert round(sum(f)) == 50_048_000
    assert 4_000_000 / 24 == R(166_666.67, abs=0.01)


def test_note_scenarios():
    s = m.note_summary()
    exp = {"Cure / refinance at par": (6, 1.3632, 17_810_000, 1.54, 14_370_445),
           "Discounted payoff": (4, 0.7371, 6_700_000, 1.20, 4_886_077),
           "Deed-in-lieu": (28, 0.1845, 16_148_000, 1.48, 2_378_624),
           "Contested foreclosure": (34, 0.1431, 15_558_000, 1.45, -568_540),
           "Bankruptcy, stay lifted": (44, 0.1162, 16_308_000, 1.47, -3_400_224),
           "Bankruptcy, cramdown": (74, 0.0660, 14_250_000, 1.41, -11_306_608)}
    for n, (months, irr, profit, mult, npv) in exp.items():
        x = s["scenarios"][n]
        assert (x["months"], round(x["irr"], 4), round(x["profit"]), round(x["multiple"], 2), round(x["npv"])) == \
            (months, irr, profit, mult, npv), n
    cure = m.UPB + m.ACCRUED_INTEREST + m.UPB * m.CONTRACT_RATE * 6 / 12
    assert cure == R(51_060_000)
    assert cure - 100_000 - 33_150_000 == R(17_810_000)
    assert round(s["expected_profit"]) == 14_198_200
    assert round(s["sd_profit"]) == 3_820_622
    assert s["p_loss"] == 0
    assert round(s["irr_of_expected"], 4) == 0.1862
    assert round(s["mean_irr"], 4) == 0.3898
    assert round(s["expected_npv"]) == 2_080_359
    assert s["p_title"] == R(0.65)


def test_irr_annualization_trap():
    f = m.note_flows("Deed-in-lieu")
    irr_m = tvm.irr(f)
    assert (1 + irr_m) ** 12 - 1 == R(m.note_scenarios()["Deed-in-lieu"]["irr"])
    assert 12 * irr_m < (1 + irr_m) ** 12 - 1      # x12 understates


def test_max_note_price():
    mp = m.max_note_price()
    assert round(mp) == 35_080_359
    assert round(mp / m.UPB, 4) == 0.7308
    assert m.note_summary(mp)["expected_npv"] == R(0.0, abs=1.0)
    # expected NPV at 33.0m equals the cushion
    assert round(mp - m.NOTE_PRICE) == round(m.note_summary()["expected_npv"])


def test_dpo_decision():
    sc = m.note_scenarios()
    names = ["Deed-in-lieu", "Contested foreclosure", "Bankruptcy, stay lifted", "Bankruptcy, cramdown"]
    num = sum(m.SCENARIOS[n]["p"] * sc[n]["npv"] for n in names)
    den = sum(m.SCENARIOS[n]["p"] for n in names)
    assert den == R(0.70)
    assert round(num / den / 1e6, 2) == -0.48
    assert round(sc["Discounted payoff"]["npv"] / 1e6, 2) == 4.89


def test_reo():
    r = m.reo_summary()
    assert round(r["basis"]) == 38_062_500
    assert round(r["irr"], 4) == 0.1467
    assert round(r["profit"]) == 11_845_500
    assert round(r["multiple"], 2) == 1.31
    assert round(r["expected_profit_incl_losing"]) == 4_145_925


def test_stress():
    exp = {0.10: (0.1459, 0.0849), 0.20: (0.1034, 0.0197), 0.30: (0.0585, -0.0496)}
    for d, (note, reo) in exp.items():
        x = m.loss_given_title_value(d)
        assert round(x["note_irr_of_expected"], 4) == note
        assert round(x["reo_irr"], 4) == reo
        assert x["note_p_loss"] == 0
    assert m.STABILIZED_NOI == 3_100_000       # restored


def test_credit_bid():
    assert round(m.credit_bid_capacity()) == 55_500_000
