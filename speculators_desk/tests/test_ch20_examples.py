"""Reproduces every number in Chapter 20 text, problems, and solutions.

Independent routes are used where possible: closed forms for the t distribution,
numerical integration of densities, odds-form Bayes, direct expected-utility sums,
and enumeration of decision trees.
"""

import math

import pytest

from sdesk import markets, stats
from sdesk import x_decision as xd

R = pytest.approx
Phi = markets.norm_cdf


# ---------------------------------------------------------------------------
# Library checks (x_decision)
# ---------------------------------------------------------------------------

def _t_pdf(x, nu):
    c = math.exp(math.lgamma((nu + 1) / 2) - math.lgamma(nu / 2)) / math.sqrt(nu * math.pi)
    return c * (1 + x * x / nu) ** (-(nu + 1) / 2)


def _simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


@pytest.mark.parametrize("t", [-5.0, -2.0, -0.5, 0.0, 1.0, 3.0])
def test_t_cdf_closed_forms(t):
    # nu = 1 (Cauchy) and nu = 2 have closed forms
    assert xd.student_t_cdf(t, 1) == R(0.5 + math.atan(t) / math.pi, abs=1e-12)
    assert xd.student_t_cdf(t, 2) == R(0.5 + t / (2 * math.sqrt(2 + t * t)), abs=1e-12)


@pytest.mark.parametrize("nu,t", [(3, -5.774), (4, -4.714), (5, -4.303), (8, -3.849), (9, 2.262)])
def test_t_cdf_against_integration(nu, t):
    lo = -400.0 if t < 0 else 0.0
    if t < 0:
        num = _simpson(lambda x: _t_pdf(x, nu), lo, t, 200000)
        # add the analytic tail beyond -400 (negligible for nu >= 3)
        assert xd.student_t_cdf(t, nu) == R(num, rel=1e-4)
    else:
        num = 0.5 + _simpson(lambda x: _t_pdf(x, nu), 0.0, t)
        assert xd.student_t_cdf(t, nu) == R(num, abs=1e-9)


def test_t_ppf_and_boundaries():
    assert xd.student_t_ppf(0.975, 9) == R(2.2622, abs=1e-4)
    assert xd.student_t_ppf(0.975, 7) == R(2.3646, abs=1e-4)
    assert xd.student_t_ppf(0.5, 5) == R(0.0, abs=1e-6)   # bisection precision near the median
    assert xd.student_t_ppf(0.975, 10_000) == R(1.96, abs=1e-3)   # tends to the normal
    with pytest.raises(ValueError):
        xd.student_t_ppf(1.0, 5)
    with pytest.raises(ValueError):
        xd.scaled_t_tail(3.0, 2)
    assert xd.t_excess_kurtosis(4) == math.inf
    assert xd.t_excess_kurtosis(5) == 6.0


def test_crra_boundaries():
    # gamma = 1 equals log utility; a sure lottery has CE equal to wealth
    assert xd.crra_certainty_equivalent([10.0], [1.0], 3) == R(10.0)
    assert xd.crra_certainty_equivalent([10, 20], [0.5, 0.5], 1) == R(math.sqrt(200))
    assert xd.crra_certainty_equivalent([10, 20], [0.5, 0.5], 1 + 1e-9) == R(math.sqrt(200), rel=1e-6)
    with pytest.raises(ValueError):
        xd.crra_utility(0.0, 3)


# ---------------------------------------------------------------------------
# Examples
# ---------------------------------------------------------------------------

def test_example_20_1():
    lt = xd.law_of_total_variance([0.6, 0.4], [72.0, 62.0], [4.0, 5.0])
    assert lt["mean"] == R(68.0)
    assert (lt["within"], lt["between"], lt["var"]) == (R(19.6), R(24.0), R(43.6))
    assert lt["sd"] == R(6.603, abs=5e-4)
    assert 0.6 * 0.4 * (72 - 62) ** 2 == R(24.0)          # two-point check
    cov2 = 2 * 0.3 * lt["sd"] * 3.0
    assert cov2 == R(11.885, abs=5e-4)
    var_p = 43.6 + 9.0 - cov2
    assert var_p == R(40.715, abs=5e-4)
    sd_p = math.sqrt(var_p)
    assert sd_p == R(6.381, abs=5e-4)
    assert 68.0 - 61.2 == R(6.8)
    assert 6.8 / sd_p == R(1.066, abs=5e-4)
    assert Phi(-6.8 / sd_p) == R(0.143, abs=5e-4)


def test_example_20_2():
    pf = 0.85 * 0.15 + 0.20 * 0.85
    assert pf == R(0.2975)
    post = stats.bayes_posterior(0.15, 0.85, 0.20)
    assert post == R(0.4286, abs=5e-5)
    assert stats.likelihood_ratio_update(0.15, 0.85 / 0.20) == R(post)
    assert (0.15 / 0.85) * 4.25 == R(0.75)
    no = 0.15 * 0.15 / (1 - pf)
    assert no == R(0.0320, abs=5e-5)
    assert pf * post + (1 - pf) * no == R(0.15)


RET_103 = [0.12, 0.08, -0.05, 0.15, 0.10, 0.06, -0.17, 0.11, 0.09, 0.07]


def test_example_20_3():
    ti = xd.t_interval(RET_103)
    assert ti["mean"] == R(0.056)
    assert ti["sd"] == R(0.09548, abs=5e-6)
    assert ti["se"] == R(0.03019, abs=5e-6)
    assert ti["t_crit"] == R(2.262, abs=5e-4)
    assert ti["half_width"] == R(0.06830, abs=5e-6)
    assert (ti["lo"], ti["hi"]) == (R(-0.0123, abs=5e-5), R(0.1243, abs=5e-5))
    assert stats.geometric_mean_return(RET_103) == R(0.0517, abs=5e-5)
    assert stats.stdev(RET_103) == R(ti["sd"])
    ne = xd.effective_sample_size_ar1(10, 0.5)
    assert ne == R(10 / 3)
    se_adj = ti["sd"] / math.sqrt(ne)
    assert se_adj == R(0.05229, abs=5e-6)
    hw = 1.96 * se_adj
    assert hw == R(0.1025, abs=5e-5)
    assert (0.056 - hw, 0.056 + hw) == (R(-0.0465, abs=5e-5), R(0.1585, abs=5e-5))
    assert (1.96 * ti["sd"] / 0.01) ** 2 == R(350, abs=0.5)
    assert (2 * 0.06 / 0.02) ** 2 == R(36)


def test_ar1_variance_formula_approaches_effective_n():
    # exact finite-n variance factor approaches (1+rho)/(1-rho) as n grows
    rho = 0.5
    for n in (1000, 5000):
        fac = 1 + 2 * sum((1 - k / n) * rho ** k for k in range(1, n))
        assert fac == R((1 + rho) / (1 - rho), rel=5e-3)


LOSSES = [31.7, 22.0, 20.1, 16.9, 15.2, 14.0, 13.1, 12.4, 11.8, 11.0, 10.4, 10.0]


def test_example_20_4():
    z = 20 / 6
    assert Phi(-z) == R(0.000429, abs=5e-7)
    assert 1 / Phi(-z) == R(2331, abs=1)
    assert 1 / Phi(-z) / 12 == R(194, abs=0.5)
    assert 360 * Phi(-z) == R(0.15, abs=0.005)
    rows = {8: (0.05196, 3.849, 0.002442, 0.88, 5.7, 1.5),
            5: (0.04648, 4.303, 0.003846, 1.38, 9.0, 6.0),
            4: (0.04243, 4.714, 0.004606, 1.66, 10.7, math.inf),
            3: (0.03464, 5.774, 0.005165, 1.86, 12.0, math.inf)}
    for nu, (scale, tthr, p, cnt, ratio, kurt) in rows.items():
        s = math.sqrt((nu - 2) / nu)
        assert 0.06 * s == R(scale, abs=5e-6)
        assert z / s == R(tthr, abs=5e-4)
        pt = xd.scaled_t_tail(z, nu)
        assert pt == R(p, abs=5e-7)
        assert 360 * pt == R(cnt, abs=0.005)
        assert pt / Phi(-z) == R(ratio, abs=0.05)
        assert xd.t_excess_kurtosis(nu) == kurt
    # (b) table, t4 vs normal
    tab = {2: (0.02275, 0.02371, 1.04), 3: (0.001350, 0.006618, 4.90),
           4: (0.0000317, 0.002406, 76.0), 5: (0.000000287, 0.001055, 3682)}
    for zz, (pn, pt, ratio) in tab.items():
        assert Phi(-zz) == R(pn, rel=2e-3)
        assert xd.scaled_t_tail(zz, 4) == R(pt, rel=1e-3)
        assert xd.scaled_t_tail(zz, 4) / Phi(-zz) == R(ratio, rel=5e-3)
    # (c) Hill
    h = xd.hill_estimator(LOSSES, 11)
    assert h["threshold"] == 10.0
    assert sum(math.log(x / 10.0) for x in LOSSES[:11]) == R(4.7054, abs=5e-5)
    assert h["alpha"] == R(2.338, abs=5e-4)
    assert h["alpha"] / math.sqrt(11) == R(0.70, abs=0.005)
    pu = 11 / 360
    assert pu == R(0.03056, abs=5e-6)
    p20 = xd.pareto_tail_prob(20, 10, pu, h["alpha"])
    assert p20 == R(0.00604, abs=5e-6)
    assert 360 * p20 == R(2.2, abs=0.05)
    assert sum(1 for x in LOSSES if x > 20) == 3
    assert xd.pareto_tail_prob(30, 10, pu, h["alpha"]) == R(0.00234, abs=5e-6)
    assert Phi(-5) == R(2.9e-7, abs=5e-9)
    assert xd.pareto_tail_prob(40, 10, pu, h["alpha"]) == R(0.00120, abs=5e-6)
    assert 2 ** h["alpha"] == R(5.06, abs=0.005)
    # 'once in 14-22 years' range (t3..t5 and Hill)
    yrs = [1 / xd.scaled_t_tail(z, nu) / 12 for nu in (3, 4, 5)] + [1 / p20 / 12]
    assert min(yrs) == R(13.8, abs=0.05) and max(yrs) == R(21.7, abs=0.05)
    # normal 3 sigma -> 6 sigma ratio "about 1.4 million"
    assert Phi(-3) / Phi(-6) == R(1.37e6, rel=0.01)


def test_example_20_5():
    l1, l2 = xd.normal_pdf(0, 3, 2), xd.normal_pdf(0, -2, 3)
    assert (l1, l2) == (R(0.06476, abs=5e-6), R(0.10648, abs=5e-6))
    assert l1 / l2 == R(0.608, abs=5e-4)
    w = xd.bma_weights([0.7, 0.3], [l1, l2])
    assert 0.7 * l1 == R(0.04533, abs=5e-6)
    assert 0.7 * l1 + 0.3 * l2 == R(0.07728, abs=5e-6)
    assert w[0] == R(0.5866, abs=5e-5) and w[1] == R(0.4134, abs=5e-5)
    m = xd.mixture_moments(w, [3.0, -2.0], [2.0, 3.0])
    assert m["mean"] == R(0.933, abs=5e-4)
    assert m["within"] == R(6.067, abs=5e-4) and m["between"] == R(6.062, abs=5e-4)
    assert m["var"] == R(12.129, abs=5e-4) and m["sd"] == R(3.483, abs=5e-4)
    assert Phi(-1.5) == R(0.0668, abs=5e-5)
    assert Phi((3 - 3) / 2 - 1.5) == R(0.0668, abs=5e-5)
    p0 = xd.mixture_normal_cdf(0, w, [3, -2], [2, 3])
    assert p0 == R(w[0] * Phi(-1.5) + w[1] * Phi(2 / 3))
    assert p0 == R(0.348, abs=5e-4)
    assert Phi(2 / 3) == R(0.7475, abs=5e-5)
    assert Phi((0 - m["mean"]) / m["sd"]) == R(0.394, abs=5e-4)
    assert xd.mixture_normal_cdf(-3, w, [3, -2], [2, 3]) == R(0.1535, abs=5e-4)
    assert Phi((-3 - m["mean"]) / m["sd"]) == R(0.129, abs=5e-4)
    assert Phi(-3 / 2) == R(0.0668, abs=5e-5) and Phi(-6 / 2) == R(0.00135, abs=5e-6)


def test_example_20_6():
    assert xd.reference_class_adjust(9.0, 2.0, 0.3) == R(6.9)
    b = (25 * 9.0 + 5 * 30.0) / 30
    assert b == R(12.5)
    adj = xd.reference_class_adjust(b, 2.0, 0.3)
    assert adj == R(9.35)
    cost = 60.0 * (1 + adj / 100)
    assert cost == R(65.61)
    lease = xd.reference_class_adjust(19, 14, 0.4)
    assert lease == R(17.0)
    carry = (lease - 14) * 0.25
    assert carry == R(0.75)
    allin = cost + carry
    assert allin == R(66.36)
    assert 68.0 - allin == R(1.64)
    sd_p = math.sqrt(43.6 + 9 - 2 * 0.3 * math.sqrt(43.6) * 3)
    assert (68.0 - allin) / sd_p == R(0.257, abs=5e-4)
    assert Phi(-(68.0 - allin) / sd_p) == R(0.399, abs=5e-4)
    assert (b - 9.0) * 60 / 100 == R(2.1)
    assert 6.8 / 61.2 == R(0.111, abs=5e-4) and 1.64 / 66.36 == R(0.025, abs=5e-4)


BINS_207 = [(0.1, 8, 1), (0.3, 10, 4), (0.5, 8, 5), (0.7, 8, 4), (0.9, 6, 4)]


def test_example_20_7():
    f, o = xd.expand_bins(BINS_207)
    assert len(f) == 40 and sum(o) == 18
    bs = stats.brier_score(f, o)
    assert bs == R(0.2340)
    d = xd.brier_decomposition(BINS_207)
    assert d["bs"] == R(bs)
    terms_rel = [n * (fk - ok / n) ** 2 for fk, n, ok in BINS_207]
    terms_res = [n * (ok / n - 0.45) ** 2 for fk, n, ok in BINS_207]
    assert [round(x, 3) for x in terms_rel] == [0.005, 0.100, 0.125, 0.320, 0.327]
    assert [round(x, 3) for x in terms_res] == [0.845, 0.025, 0.245, 0.020, 0.282]
    assert sum(terms_rel) == R(0.877, abs=5e-4) and sum(terms_res) == R(1.417, abs=5e-4)
    assert terms_rel[3] + terms_rel[4] == R(0.647, abs=5e-4)
    assert d["rel"] == R(0.02192, abs=5e-6)
    assert d["res"] == R(0.03542, abs=5e-6)
    assert d["unc"] == R(0.2475)
    assert d["rel"] - d["res"] + d["unc"] == R(bs)
    assert d["bss"] == R(0.055, abs=5e-4)
    # binomial standard errors for bins of 6 to 10 forecasts
    assert math.sqrt(0.9 * 0.1 / 6) == R(0.122, abs=5e-4)
    assert math.sqrt(0.5 * 0.5 / 8) == R(0.177, abs=5e-4)


def test_example_20_8():
    assert 0.30 + 0.45 - 0.10 == R(0.65)
    assert 0.70 + 0.10 - 0.30 - 0.45 == R(0.05)
    # Dutch book payoff is zero in every state
    for r in (0, 1):
        for c in (0, 1):
            assert r + c - r * c - max(r, c) == 0
    cells = [-12.0, -2.5, 1.0, 4.0]
    for pcr, ev in [(0.10 / 0.30, 0.05), (0.45, -0.1775), (0.60, -0.47)]:
        rc = 0.30 * pcr
        joint = [rc, 0.30 - rc, 0.45 - rc, 1 - 0.30 - 0.45 + rc]
        assert sum(joint[:2]) == R(0.30) and joint[0] + joint[2] == R(0.45)
        assert sum(p * x for p, x in zip(joint, cells)) == R(ev)
    assert 0.35 / 0.70 == R(0.5)
    assert [0.30 * 0.45, 0.30 * 0.55, 0.70 * 0.45, 0.70 * 0.55] == [R(0.135), R(0.165), R(0.315), R(0.385)]


def test_example_20_9():
    w = [25.8, 22.3, 16.8]
    p = [0.5, 0.3, 0.2]
    assert 15 * 1.12 == R(16.8) and 20 * 1.12 == R(22.4)
    ew = sum(a * b for a, b in zip(w, p))
    assert ew == R(22.95)
    sd = math.sqrt(sum(b * (a - ew) ** 2 for a, b in zip(w, p)))
    assert sd == R(3.428, abs=5e-4)
    terms = [b * a ** -2 for a, b in zip(w, p)]
    assert [round(t, 6) for t in terms] == [0.000751, 0.000603, 0.000709]
    assert sum(terms) == R(0.002063, abs=5e-7)
    # direct expected utility route versus library CE
    eu = sum(b * xd.crra_utility(a, 3) for a, b in zip(w, p))
    ce3 = (-2 * eu) ** (-0.5)
    assert ce3 == R(xd.crra_certainty_equivalent(w, p, 3))
    assert ce3 == R(22.016, abs=5e-4)
    table = {1: (22.665, 0.265, 0.285, 0.256), 3: (22.016, -0.384, 0.934, 0.768),
             5: (21.307, -1.093, 1.643, 1.280)}
    for g, (ce, vs, prem, pratt) in table.items():
        c = xd.crra_certainty_equivalent(w, p, g)
        assert c == R(ce, abs=5e-4)
        assert c - 22.4 == R(vs, abs=5e-4)
        assert ew - c == R(prem, abs=5e-4)
        assert 0.5 * g * sd ** 2 / ew == R(pratt, abs=5e-4)
    assert ce3 - 16.8 == R(5.216, abs=5e-4)
    assert 0.5 * 9.0 + 0.3 * 5.5 == R(6.15)
    assert 6.15 - 5.6 == R(0.55)
    assert 1 - 0.768 / 0.934 == R(0.18, abs=0.005)
    assert 0.5 * 1.8 + 0.3 * 1.1 == R(1.23)

    def ce_x(x, g):
        return xd.crra_certainty_equivalent([1.12 * (20 - x) + x * m for m in (1.8, 1.1, 0.0)], p, g)

    for g, (opt, brk) in {1: (4.65, 8.81), 3: (1.62, 3.16), 5: (0.98, 1.92)}.items():
        grid = [i / 100 for i in range(0, 2000)]
        best = max(grid, key=lambda x: ce_x(x, g))
        assert best == R(opt)
        first_bad = next(x for x in grid[1:] if ce_x(x, g) < 22.4 - 1e-12)
        assert first_bad == R(brk)
    assert 4.65 / 20 == R(0.2325)


def test_example_20_10():
    pay = [[0.60, -2.40], [0.0, 0.0]]
    e = xd.evpi(pay, [0.85, 0.15])
    assert e["ev_prior"] == R(0.15) and e["best_action"] == 0
    assert e["ev_perfect"] == R(0.51) and e["evpi"] == R(0.36)
    s = xd.evsi_binary_signal(pay, [0.85, 0.15], [0.20, 0.85])
    assert s["p_signal_1"] == R(0.2975)
    assert s["posterior_1"][1] == R(0.4286, abs=5e-5)
    assert s["evs_1"][0] == R(-0.686, abs=5e-4) and s["action_1"] == 1
    assert 0.5714 * 0.6 == R(0.3429, abs=5e-4) and 0.4286 * 2.4 == R(1.0286, abs=5e-4)
    assert s["posterior_0"][1] == R(0.0320, abs=5e-5)
    assert s["evs_0"][0] == R(0.504, abs=5e-4) and s["action_0"] == 0
    assert 0.9680 * 0.6 == R(0.5808, abs=5e-4) and 0.0320 * 2.4 == R(0.0769, abs=5e-4)
    # independent route: enumerate the tree
    ev_with = 0.7025 * (0.85 * 0.80 * 0.6 - 0.15 * 0.15 * 2.4) / 0.7025
    assert s["ev_with_signal"] == R(ev_with) == R(0.354)
    assert s["evsi"] == R(0.204)
    assert s["evsi"] - 0.020 == R(0.184)
    assert 0 <= s["evsi"] <= s["evpi"]
    assert s["evsi"] / s["evpi"] == R(0.57, abs=0.005)


def test_example_20_11():
    pay = [[8.0, 3.0, -7.0], [6.5, 2.0, -0.5], [0.0, 0.0, 0.0]]
    mr = xd.minimax_regret(pay)
    assert mr["regret"] == [[0, 0, 7], [1.5, 1.0, 0.5], [8, 3, 0]]
    assert mr["max_regret"] == [7.0, 1.5, 8.0] and mr["action"] == 1
    assert max(range(3), key=lambda a: min(pay[a])) == 2          # maximin
    assert max(range(3), key=lambda a: max(pay[a])) == 0          # maximax
    pr = [0.40, 0.45, 0.15]
    evs = [sum(a * b for a, b in zip(row, pr)) for row in pay]
    assert evs == [R(3.50), R(3.425), R(0.0)]
    gbar = (40 * 1.5 + 45 * 1.0) / 85
    assert gbar == R(1.235, abs=5e-4)
    q = gbar / (gbar + 6.5)
    assert q == R(0.160, abs=5e-4)
    assert evs[0] - evs[1] == R(0.075)


def test_historical_2016_scores():
    assert (1 - 0.286) ** 2 == R(0.510, abs=5e-4)
    assert (1 - 0.20) ** 2 == R(0.640)
    assert 0.286 / 0.20 == R(1.43)
    assert 0.286 / (0.286 + 0.20) == R(0.59, abs=0.005)


# ---------------------------------------------------------------------------
# Problems
# ---------------------------------------------------------------------------

def test_problem_20_1():
    d = xd.brier_decomposition([(0.45, 40, 18)])
    assert d["rel"] == R(0) and d["res"] == R(0) and d["bs"] == R(0.2475) and d["bss"] == R(0)


def test_problem_20_2():
    assert stats.bayes_posterior(0.10, 0.90, 0.10) == R(0.5)
    assert (1 / 9) * 9 == R(1.0)


def test_problem_20_3():
    assert Phi(-3) == R(0.00135, abs=5e-6)
    assert 360 * Phi(-3) == R(0.49, abs=0.005)
    pt = xd.scaled_t_tail(3, 4)
    assert pt == R(0.006618, abs=5e-7)
    assert 360 * pt == R(2.38, abs=0.005)
    assert pt / Phi(-3) == R(4.90, abs=0.005)


RET_204 = [0.18, 0.09, -0.22, 0.25, 0.11, 0.04, -0.08, 0.14]


def test_problem_20_4():
    ti = xd.t_interval(RET_204)
    assert sum(RET_204) == R(0.51)
    assert ti["mean"] == R(0.06375)
    assert ti["sd"] == R(0.15052, abs=5e-6)
    assert ti["se"] == R(0.05322, abs=5e-6)
    assert ti["t_crit"] == R(2.365, abs=5e-4)
    assert ti["half_width"] == R(0.1258, abs=5e-5)
    assert (ti["lo"], ti["hi"]) == (R(-0.0621, abs=5e-5), R(0.1896, abs=5e-5))
    assert stats.geometric_mean_return(RET_204) == R(0.0536, abs=5e-5)
    ne = xd.effective_sample_size_ar1(8, 0.3)
    assert ne == R(4.31, abs=5e-3)
    assert ti["sd"] / math.sqrt(ne) == R(0.0725, abs=5e-5)
    assert 1.96 * ti["sd"] / math.sqrt(ne) == R(0.1421, abs=5e-5)
    assert (1.96 * ti["sd"] / 0.02) ** 2 == R(217.6, abs=0.05)
    assert -0.22 / 8 == R(-0.0275)
    assert (0.51 + 0.22) / 7 == R(0.1043, abs=5e-5)


BINS_205 = [(0.2, 10, 1), (0.4, 10, 3), (0.6, 10, 7), (0.8, 10, 9)]


def test_problem_20_5():
    f, o = xd.expand_bins(BINS_205)
    assert stats.brier_score(f, o) == R(0.16)
    d = xd.brier_decomposition(BINS_205)
    assert (d["rel"], d["res"], d["unc"], d["bss"]) == (R(0.01), R(0.10), R(0.25), R(0.36))
    d2 = xd.brier_decomposition([(0.1, 10, 1), (0.3, 10, 3), (0.7, 10, 7), (0.9, 10, 9)])
    assert d2["bs"] == R(0.15) and d2["rel"] == R(0) and d2["bss"] == R(0.40)
    assert stats.brier_score([0.5] * 40, o) == R(0.25)


def test_problem_20_6():
    l1, l2 = xd.normal_pdf(6.25, 5.75, 0.40), xd.normal_pdf(6.25, 6.50, 0.50)
    assert (l1, l2) == (R(0.4566, abs=5e-5), R(0.7041, abs=5e-5))
    assert l1 / l2 == R(0.6485, abs=5e-5)
    w = xd.bma_weights([0.5, 0.5], [l1, l2])
    assert w == [R(0.3934, abs=5e-5), R(0.6066, abs=5e-5)]
    m = xd.mixture_moments(w, [5.75, 6.5], [0.4, 0.5])
    assert m["mean"] == R(6.205, abs=5e-4)
    assert (m["within"], m["between"], m["var"]) == (R(0.2146, abs=5e-5), R(0.1342, abs=5e-5), R(0.3488, abs=5e-5))
    assert m["sd"] == R(0.591, abs=5e-4)
    p1, p2 = 1 - Phi(2.5), 1 - Phi(0.5)
    assert (p1, p2) == (R(0.0062, abs=5e-5), R(0.3085, abs=5e-5))
    assert 1 - xd.mixture_normal_cdf(6.75, w, [5.75, 6.5], [0.4, 0.5]) == R(w[0] * p1 + w[1] * p2)
    assert w[0] * p1 + w[1] * p2 == R(0.1896, abs=5e-5)
    v1, v2 = 3.0 / 0.0575, 3.0 / 0.065
    assert (v1, v2) == (R(52.17, abs=5e-3), R(46.15, abs=5e-3))
    assert 3.0 / (m["mean"] / 100) == R(48.35, abs=5e-3)
    assert w[0] * v1 + w[1] * v2 == R(48.52, abs=5e-3)


def test_problem_20_7():
    pay = [[1.5, -1.8], [0.0, 0.0]]
    e = xd.evpi(pay, [0.6, 0.4])
    assert e["ev_prior"] == R(0.18) and e["evpi"] == R(0.72)
    s = xd.evsi_binary_signal(pay, [0.6, 0.4], [0.8, 0.3])
    assert s["p_signal_1"] == R(0.60) and s["posterior_1"][0] == R(0.80)
    assert s["evs_1"][0] == R(0.84) and s["action_1"] == 0
    assert s["p_signal_0"] == R(0.40) and s["posterior_0"][0] == R(0.30)
    assert s["evs_0"][0] == R(-0.81) and s["action_0"] == 1
    assert s["ev_with_signal"] == R(0.504) and s["evsi"] == R(0.324)
    assert s["evsi"] - 0.075 == R(0.249)
    c = xd.evsi_binary_signal(pay, [0.6, 0.4], [0.8, 0.7])
    assert c["p_signal_1"] == R(0.76) and c["posterior_1"][0] == R(0.6316, abs=5e-5)
    assert c["evs_1"][0] == R(0.284, abs=5e-4)
    assert c["p_signal_0"] == R(0.24) and c["posterior_0"][0] == R(0.50)
    assert c["evs_0"][0] == R(-0.15)
    assert c["ev_with_signal"] == R(0.216, abs=5e-4) and c["evsi"] == R(0.036, abs=5e-4)
    assert (0.8 / 0.3, 0.2 / 0.7, 0.8 / 0.7) == (R(2.67, abs=5e-3), R(0.29, abs=5e-3), R(1.14, abs=5e-3))


def test_problem_20_8():
    p = [0.45, 0.35, 0.20]
    w = [9.9 + 5.4, 9.9 + 3.3, 9.9 + 0.6]
    assert w == [R(15.3), R(13.2), R(10.5)]
    assert sum(a * b for a, b in zip(w, p)) == R(13.605)
    assert 1.8 * 0.45 + 1.1 * 0.35 + 0.2 * 0.2 == R(1.235)
    ce2 = 1 / sum(b / a for a, b in zip(w, p))
    assert ce2 == R(xd.crra_certainty_equivalent(w, p, 2)) == R(13.338, abs=5e-4)
    ce4 = xd.crra_certainty_equivalent(w, p, 4)
    assert ce4 == R(13.044, abs=5e-4)
    assert ce2 > 13.2 > ce4

    def ce_x(x, g):
        return xd.crra_certainty_equivalent([1.10 * (12 - x) + x * m for m in (1.8, 1.1, 0.2)], p, g)

    for g, (opt, brk) in {2: (2.25, 4.36), 4: (1.14, 2.24)}.items():
        grid = [i / 100 for i in range(0, 1200)]
        assert max(grid, key=lambda x: ce_x(x, g)) == R(opt)
        assert next(x for x in grid[1:] if ce_x(x, g) < 13.2 - 1e-12) == R(brk)


def test_problem_20_9():
    pab = 0.25 * 0.80
    assert pab == R(0.20)
    # Dutch book: zero payoff in each state, premium +0.05
    for a in (0, 1):
        for b in (0, 1):
            payoff = a * b + a * (0.80 - b) - 0.80 * a
            assert payoff == R(0.0, abs=1e-12)
    assert -0.15 + 0.80 * 0.25 == R(0.05)
    cells = [pab, 0.25 - pab, 0.40 - pab, 1 - 0.25 - 0.40 + pab]
    assert cells == [R(0.20), R(0.05), R(0.20), R(0.55)]
    assert (0.40 - pab) / 0.75 == R(0.267, abs=5e-4)
    pay = [[-4.0, -1.5, -2.0, 2.5], [-1.0, -0.5, -0.5, 1.2], [0, 0, 0, 0]]
    evs = [sum(a * b for a, b in zip(r, cells)) for r in pay]
    assert evs == [R(0.100), R(0.335), R(0.0)]
    mr = xd.minimax_regret(pay)
    assert mr["max_regret"] == [R(4.0), R(1.3), R(2.5)] and mr["action"] == 1
    assert 0.25 + 0.40 - 0.15 == R(0.50) and 0.25 + 0.40 - 0.20 == R(0.45)


def test_problem_20_10():
    out = {}
    for miss, (b, adj, cost, prof) in {25: (11.2, 8.44, 54.22, 1.78), 15: (7.2, 5.64, 52.82, 3.18)}.items():
        bb = (6 * 2.0 + 4 * miss) / 10
        assert bb == R(b)
        a = xd.reference_class_adjust(bb, 2.0, 0.3)
        assert a == R(adj)
        c = 50.0 * (1 + a / 100)
        assert c == R(cost)
        assert 56.0 - c == R(prof)
        out[miss] = 56.0 - c
    assert 56.0 - 50.0 * 1.02 == R(5.0)


def test_reference_sheet_and_text_misc():
    assert 2.2622 * 0.10 / math.sqrt(10) == R(0.0715, abs=5e-4)       # "roughly +/-7%"
    assert 2.1 / 6.8 == R(0.31, abs=0.005)                               # "31% of the sponsor's projected profit"
    assert 1 / Phi(-20 / 6) / 12 == R(194, abs=0.5)                      # "about once in 190 years"
