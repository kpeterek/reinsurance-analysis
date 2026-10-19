# Chapter 10 — Capital Structure, Debt, and Equity

> **Status:** Complete (v1.0). Numerical examples are reproduced in `tests/test_ch10_examples.py`. Problems are in `problems/questions/ch10_problems.md` and solutions in `problems/solutions/ch10_solutions.md`. Sources are listed in `references/sources_ch10.md`. One item, the size of trade-press-reported replacement-cap price increases, is marked *(verification pending)* and is not used as a number. Drills D046–D055. Case B (`cases/hypothetical/case_B_refinancing_cliff/`) applies the chapter.

## Learning objectives

After this chapter you should be able to:

1. Size a commercial mortgage under loan-to-value (LTV), debt service coverage (DSCR), and debt-yield constraints. Identify the binding constraint and find the interest rate at which the binding constraint changes.
2. Compute payments, loan constants, amortization, and balloon balances, including loans with an interest-only (IO) period, both in Python and on an HP-12C.
3. Analyze floating-rate debt: index plus spread, interest-rate caps, DSCR sizing at the cap strike, the price of a cap under the normal (Bachelier) model, and why replacement caps became a solvency problem when forward rates rose.
4. Read a capital stack by attachment and detachment points. Allocate value losses across senior debt, mezzanine debt, preferred equity, and common equity, and explain what an intercreditor agreement changes.
5. Run an IRR-hurdle waterfall with `sdesk.cre.irr_hurdle_waterfall`, explain catch-up provisions, and value the sponsor's promote as an option on the upside.
6. Compute a refinancing gap and decompose it into its causes. Analyze covenants, cash traps, and cures.
7. Value the borrower's default option under non-recourse debt, and show how carve-out ("bad boy") guarantees change the borrower's behavior.
8. Compute dilution from capital calls under fair-value, book-value, and punitive terms.
9. Price a distressed loan purchase, and explain the lender incentives behind "extend and pretend".

---

## 10.1 Opening investment problem: Ridgeview's rescue request

All facts in this section are [HYPOTHESIS], a constructed teaching case. The same property recurs in Examples 10.3, 10.7, 10.8, and 10.10.

You run the structured-credit allocation of a family office. A sponsor you know asks for \$5.0 million of rescue capital for **Ridgeview**, a 280-unit garden apartment community in a Sun Belt metro.

* The sponsor bought Ridgeview three years ago for \$40.0 million with a \$30.0 million floating-rate bridge loan: 75% LTV at one-month SOFR + 3.25%, interest-only, with a three-year initial term and two one-year extension options. The lender required a two-year interest-rate cap struck at 3.00% SOFR. The sponsor bought it for a few thousand dollars because, at the time, forward SOFR was near zero.
* The business plan was to renovate units and grow NOI from \$2.1 million to \$2.8 million. Renovations are about half done. Insurance and payroll costs rose. NOI is still \$2.1 million.
* SOFR is now above the strike. The original cap has expired, and a replacement cap has been bought once, out of reserves. The current replacement cap expires in two months. The lender requires another replacement cap as a condition of the extension, and the lender has started trapping all excess cash because DSCR and debt yield are below their triggers.
* Comparable sales suggest a 7.75% cap rate on in-place NOI, which implies a value of about \$27 million. The loan balance is \$30.0 million.

The sponsor proposes \$5.0 million of **preferred equity** at a 12% current-pay rate, senior to the sponsor's common equity. Proceeds would buy the replacement cap, pay down the loan enough to release the cash trap, and finish the renovations. Separately, a broker tells you that the senior lender, a regional bank, would sell the \$30.0 million note at 80 cents on the dollar.

You have three choices: fund the preferred equity, buy the note, or do nothing. By the end of the chapter you will be able to value each one. Section 10.10 returns to the decision.

---

## 10.2 Economic intuition: debt is a short put on the property

Start from the payoff at maturity. A non-recourse lender with balance $B$ receives $\min(V, B)$, where $V$ is the property's value. The equity holder receives $\max(V - B, 0)$. The identity

$$\min(V,B) = B - \max(B - V, 0)$$

says that the lender owns a riskless claim of $B$ **minus a put option** on the property struck at $B$. The borrower bought that put. The borrower's equity is a **call** on the property. Every topic in this chapter follows from this structure:

* **Loan sizing** limits how far in the money the put can drift. LTV caps the strike relative to value. DSCR and debt yield cap it relative to income, which is harder to manipulate than an appraisal.
* **Amortization** lowers the strike over time. Interest-only debt keeps it constant. A balloon is the strike that must be refinanced.
* **Covenants and cash traps** let the lender act before maturity, when the put is moving into the money but has not yet been exercised.
* **Recourse and carve-out guarantees** take away part of the put. They make the borrower pay for specific bad acts, which changes what the borrower does when equity is underwater.
* **Mezzanine debt and preferred equity** split the claim between senior debt and common equity into further layers. Each layer is a call spread on the property: it gains nothing above its detachment point and loses everything below its attachment point.
* **The promote** is a call on the equity, which is a call on the property: a compound option. It makes the sponsor's payoff convex. Convex payoffs reward volatility, so a sponsor with an out-of-the-money promote prefers risk.
* **Refinancing risk** is the risk that, at maturity, the strike exceeds what new lenders will advance. The put is then exercised not because the property is worthless, but because nobody will refinance the strike.

Two consequences matter in practice.

**First, the option view explains behavior that cash-flow analysis cannot.** When $V < B$, equity is worth more than zero only because of time value. A sponsor with one more year of optionality will pay something for an extension even though the equity is "underwater". A lender who forecloses gives up nothing in option terms. The bargaining zone between them is computable (Example 10.8).

**Second, leverage is not a return; it is a transfer of risk.** The lender is short volatility. The equity is long volatility. The promote is longer still. When a lender's incentives (avoid recognizing losses) and a sponsor's incentives (keep the option alive, keep the fees) align against an outside investor, the result is "extend and pretend" (§10.8 and Example 10.10).

---

## 10.3 Technical definitions

| Term | Definition |
|---|---|
| Loan-to-value (LTV) | $L/V$. Value is an appraisal or the purchase price, whichever is lower, in most acquisition loans |
| Loan-to-cost (LTC) | $L/\text{total project cost}$. Used for construction and value-add loans, where "value" is a forecast |
| Debt service ($DS$) | Annual interest plus scheduled principal. For IO loans, interest only |
| Loan constant ($K$) | $DS/L$, annual debt service per dollar of loan. For IO debt $K = r$ |
| DSCR | $NOI/DS$, or underwritten net cash flow (NCF) / $DS$. Lenders specify which numerator |
| Debt yield ($DY$) | $NOI/L$. Independent of rate and amortization, so it cannot be gamed by IO or a low coupon |
| Balloon | Balance due at maturity, $B_T$ |
| Amortization term vs loan term | Amortization sets the payment (e.g., 30 years). Term sets maturity (e.g., 10 years). The difference creates the balloon |
| Index + spread | Floating rate = reference rate (SOFR in the U.S. since the end of LIBOR) + a fixed credit spread |
| Interest-rate cap | A strip of call options (caplets) on the index. Each pays notional × accrual × max(index − strike, 0) |
| Sizing at strike | DSCR computed at strike + spread, the worst-case rate when a cap is in place |
| Cash trap / sweep | After a trigger (DSCR or DY below a level), excess cash is held by the lender or applied to principal |
| Cash management | Hard lockbox (tenants pay into a lender-controlled account) or springing lockbox (activated on a trigger) |
| Recourse | The lender can pursue the borrower's or guarantor's other assets for a deficiency |
| Non-recourse carve-out ("bad boy") guarantee | A guarantee that converts non-recourse into recourse for specified acts. *Loss* carve-outs (misapplied rents, waste, environmental) cover actual losses. *Springing full recourse* (voluntary bankruptcy, unpermitted transfer or financing) makes the full debt recourse |
| Mezzanine loan | A loan secured by a pledge of the equity interests in the property-owning entity. Remedy: a UCC foreclosure on the equity, usually much faster than a mortgage foreclosure |
| Preferred equity | An equity interest with a priority return and, often, control rights on default. It is not debt and has no lien |
| Attachment / detachment | The cumulative LTV at which a tranche's claim begins (attachment) and ends (detachment), measured on original value. A mezz loan "from 60% to 75%" sits behind 60% of senior debt and ahead of everything above 75% |
| Intercreditor agreement | Contract between senior and mezzanine lenders: cure rights, purchase option, standstill, and what the mezz lender must do to take control |
| Waterfall | Rules for splitting equity cash flows between investors (LP) and sponsor (GP) |
| Preferred return ("pref") | Return investors receive before the promote applies, often 8%, usually compounding |
| Catch-up | After the pref, a tier in which the GP receives most or all distributions until it holds its target share of total profit |
| Promote (carried interest) | The GP's disproportionate share above hurdles |
| Refinancing gap | Balance + refinancing costs − new loan. Positive means equity must be contributed |
| Capital call dilution | Reduction in a non-funding partner's ownership when others fund a call |
| Discounted payoff (DPO) | Lender accepts less than the balance in full satisfaction |
| Deed-in-lieu | Borrower conveys the property to the lender instead of a contested foreclosure |
| Extend and pretend | Extending a loan whose collateral no longer supports it, to defer loss recognition |

Convention for attachment points: a 60–75% mezzanine loan is repaid in full if $V \ge 0.75\,V_0$, is partly impaired for $0.60\,V_0 < V < 0.75\,V_0$, and is wiped out if $V \le 0.60\,V_0$. Equivalently, it is impaired once value falls more than 25% and wiped out once value falls 40% or more. Accrued but unpaid interest or preference, which raises a tranche's claim over time, is ignored in this convention and must be added when a claim has been accruing.

---

## 10.4 Equations and derivations

### 10.4.1 Payment, loan constant, and balance

With monthly rate $i = r/12$ and $n$ amortization months, the level payment solves $L = PMT \cdot a_{\overline{n}|i}$, where $a_{\overline{n}|i} = (1-(1+i)^{-n})/i$:

$$PMT = \frac{L\,i}{1-(1+i)^{-n}}, \qquad K = \frac{12\,PMT}{L} = \frac{12\,i}{1-(1+i)^{-n}}.$$

$K$ depends only on rate and amortization, not on the loan amount. That is why lenders size on it.

The balance after $k$ payments has two equivalent forms. **Prospectively**, it is the present value of the remaining payments:

$$B_k = PMT \cdot a_{\overline{n-k}|i}.$$

**Retrospectively**, it is the loan accumulated at $i$, less accumulated payments:

$$B_k = L(1+i)^k - PMT\,\frac{(1+i)^k - 1}{i}.$$

The two agree because the payment was set so that the loan's present value equals the payments' present value. Tests use both forms as independent checks.

With an IO period of $m$ months followed by amortization on an $n$-month schedule, the balance during IO stays at $L$, and the balance at month $T > m$ is $B_{T-m}$ computed on the original schedule. The IO period does not change the amortization payment. It delays principal reduction and raises the balloon.

### 10.4.2 Sizing: three constraints, one loan

$$L^* = \min\left(\lambda_{max} V,\; \frac{NOI}{DSCR_{min}\,K},\; \frac{NOI}{DY_{min}}\right).$$

The DSCR constraint binds instead of LTV when $NOI/(DSCR_{min} K) < \lambda_{max} V$. Substituting $V = NOI/c$:

$$\text{DSCR binds} \iff K > \frac{c}{\lambda_{max}\,DSCR_{min}}.$$

The crossover loan constant depends only on the cap rate and the two covenants. At $c = 6.00\%$, $\lambda_{max} = 65\%$, $DSCR_{min} = 1.25$, the crossover is $K^* = 0.06/0.8125 = 7.385\%$, which a 30-year loan reaches at about 6.24% (Example 10.1). When rates rise and cap rates do not, DSCR takes over from LTV as the binding constraint. That is the first channel through which rate increases shrink loan proceeds, even before values fall.

For IO debt, the DSCR and debt-yield tests are linked:

$$\frac{NOI}{L\,r} \ge DSCR_{min} \iff \frac{NOI}{L} \ge DSCR_{min}\, r.$$

A 1.20x IO DSCR test at 6.25% is the same constraint as a 7.50% debt-yield test. Example 10.7 uses this identity.

### 10.4.3 Floating-rate debt and caps

Interest on floating debt is $L(I + s)$ where $I$ is the index and $s$ the spread. With a cap struck at $K_{cap}$ on the index, the borrower's net interest is $L(\min(I, K_{cap}) + s)$, and the cap pays $L\max(I - K_{cap}, 0)$ per year. Lenders size such loans at the worst-case rate: $DSCR = NOI / [L(K_{cap} + s)]$.

A cap is a strip of caplets. This book prices caplets with normal (basis-point) volatility, because lognormal volatility explodes as the forward rate approaches zero, which makes it unusable for the near-zero forwards of 2020–2021 [INFERENCE from the model's mathematics; dealer quoting conventions vary and are not sourced here]. Under the normal (Bachelier) model a caplet fixing at $T$, covering accrual $\tau$, paid with discount factor $P$, on forward rate $F$ with normal volatility $\sigma_N$ is worth

$$c = N\,\tau\,P\left[(F - K)\,\Phi(d) + \sigma_N\sqrt{T}\,\phi(d)\right], \qquad d = \frac{F - K}{\sigma_N \sqrt{T}}.$$

Two terms matter. $(F-K)\Phi(d)$ is intrinsic value weighted by exercise probability. $\sigma_N\sqrt T\,\phi(d)$ is time value. When the forward is far below the strike, both are near zero and the cap is cheap. When the forward is above the strike, the cap is mostly intrinsic value: the borrower prepays, in cash, the interest the cap will save. **A deep in-the-money cap does not hedge anything. It converts future interest into an upfront payment.** That was the economics of replacement caps after 2022 (§10.9). Chapter 18 develops caps, floors, and swaptions fully.

### 10.4.4 Capital stack loss allocation

Let tranches $j = 1,\dots,J$ be ordered senior to junior with amounts $A_j$ summing to $V_0$. A value decline $\Delta = V_0 - V$ is allocated from the bottom. The loss to tranche $j$ is

$$\ell_j = \min\left(A_j,\; \max\left(\Delta - \sum_{k>j} A_k,\; 0\right)\right).$$

Attachment $a_j = \sum_{k<j}A_k/V_0$; detachment $d_j = a_j + A_j/V_0$. Tranche $j$ is impaired once value falls by more than $1 - d_j$ and wiped out once it falls by more than $1 - a_j$.

### 10.4.5 Waterfall mechanics

`sdesk.cre.irr_hurdle_waterfall` accrues one balance per hurdle $h$ at rate $h$ on contributions net of investor distributions. Distributable cash first goes to investors at the tier-1 split until the first balance is zero (investors have earned $h_1$), then at the tier-2 split until the second balance is zero, and so on. The investor IRR exceeds $h$ if and only if the final balance for $h$ is $\le 0$.

A **catch-up** changes the second tier. On a single terminal distribution $D$ against contribution $C$ over $T$ years with pref rate $h$ and carry share $\pi$:

1. Return of capital: $\min(D, C)$ to investors.
2. Pref: $p = \min(D - C, C[(1+h)^T - 1])$ to investors.
3. Catch-up: the GP receives a share $\gamma$ of each dollar until the GP holds $\pi$ of all profit distributed. If $x$ dollars flow through this tier, $\gamma x = \pi(p + x)$, so $x = \pi p/(\gamma - \pi)$.
4. Split the rest $(1-\pi)/\pi$.

With a full catch-up ($\gamma = 1$) and enough profit, the GP ends with exactly $\pi$ of total profit. The pref then only affects *timing* and *bad outcomes*: it protects investors when profit is low and gives nothing extra when profit is high. Without catch-up ($\gamma = \pi$), the GP's share applies only to profit above the pref.

### 10.4.6 The refinancing gap

$$G = B_T + C_{refi} - L^*_{new}.$$

If $G > 0$, equity must be contributed or the loan defaults. Write $L^*_{new} = \lambda_{new} NOI_T / c_T$ when LTV binds. Then the gap rises with the balloon $B_T$, the new cap rate $c_T$, and falls with NOI and the permitted LTV. A **gap attribution** walks from the old loan to the new proceeds one cause at a time (Case B, Mode B).

### 10.4.7 The borrower's default option

At maturity with balance $B$, a non-recourse borrower who must either repay or hand over the property holds equity worth $\max(V - B, 0)$. If the lender extends for one period for a fee $f$, and $V_1$ is uncertain, the borrower's extension value is

$$E_0 = \frac{E[\max(V_1 - B, 0)]}{1 + k_E} - f.$$

The lender compares extension with foreclosure. With foreclosure costs $\kappa$ as a fraction of value, and recovery in either path received at $t=1$:

$$PV_{ext} = \frac{E[\min(B,\; V_1(1-\kappa))]}{1+k_L} + f, \qquad PV_{fc} = \frac{V_0(1-\kappa)}{1+k_L}\ \text{(time-to-sale one period)}.$$

A bargaining zone exists for fees with $PV_{ext} \ge PV_{fc}$ and $E_0 \ge 0$. A springing-recourse guarantee adds a penalty $B - \text{recovery}$ to any borrower action that triggers it. Its purpose is to make obstruction (for example, a bankruptcy filing to stay foreclosure) unprofitable.

### 10.4.8 Capital-call dilution

With pre-call fair equity value $E_{pre}$ over $U$ units, a funding partner buys new units at $E_{pre}/U$. If it also funds a non-funding partner's share $c_B$, punitive terms credit it with $\theta c_B$ of contributions ($\theta > 1$). The non-funding partner's post-call ownership is

$$s_B' = \frac{U_B}{U + c_A U/E_{pre} + \theta c_B U/E_{pre}}.$$

If new units are issued at fair value and $\theta = 1$, dilution transfers no value: the non-funder keeps the value of its old units. Value transfers come from **pricing** the units away from fair value, in either direction, and from $\theta > 1$.

---

## 10.5 Worked examples

All inputs are hypothetical [HYPOTHESIS]. All ten examples are reproduced in `tests/test_ch10_examples.py`.

### Example 10.1 — Sizing a loan when rates move the binding constraint

**Given.** Multifamily NOI after reserves \$2,400,000. Appraised value \$40,000,000 (6.00% cap). Lender terms: 30-year amortization, max 65% LTV, min 1.25x DSCR on NOI, min 8.0% debt yield. Quoted rate 6.50%. Compare 6.25% and a 6.50% interest-only quote.

**Find.** Maximum loan, binding constraint, and the rate at which DSCR replaces LTV as binding.

**Solution.**

Loan constant at 6.50%, 30 years: $K = 12 \times 0.0054167/(1 - 1.0054167^{-360}) = 7.5848\%$.

| Constraint | Formula | Loan |
|---|---|---|
| LTV | $0.65 \times 40{,}000{,}000$ | \$26,000,000 |
| DSCR | $2{,}400{,}000 / 1.25 / 0.075848$ | \$25,313,731 |
| Debt yield | $2{,}400{,}000 / 0.08$ | \$30,000,000 |

DSCR binds: $L^* = \$25{,}313{,}731$. Debt service = $1{,}920{,}000$ by construction ($2{,}400{,}000/1.25$). Resulting LTV 63.28%, debt yield 9.48%.

At 6.25%: $K = 7.3886\%$, DSCR loan = \$25,985,956, still marginally below the LTV loan.

Crossover: $K^* = c/(\lambda_{max} DSCR_{min}) = 0.06/(0.65 \times 1.25) = 7.3846\%$. Solving $K(r, 30) = 7.3846\%$ gives $r^* = 6.24\%$.

Interest-only at 6.50%: $K = 6.50\%$, DSCR loan $= 2{,}400{,}000/1.25/0.065 = \$29{,}538{,}462$. LTV binds at \$26,000,000.

**Check.** $25{,}313{,}731 \times 0.075848 = 1{,}920{,}000$ and $2{,}400{,}000/1{,}920{,}000 = 1.25$. ✓

**Decision consequence.** Above about 6.24%, every 25 bp of rate costs about \$0.67 million of proceeds on this asset, because DSCR now binds. The borrower has three levers: accept less leverage, negotiate IO (which restores LTV as the binding test but leaves the balance undiminished at maturity), or buy down the rate with points. IO is the cheapest lever today and the most expensive at maturity: it raises the balloon (Example 10.2) exactly when refinancing is hardest. A lender that permits IO to make a deal "work" on DSCR is relying on value, not income, for repayment.

### Example 10.2 — Amortization and balloon, with HP-12C keystrokes

**Given.** \$25,000,000 loan, 6.50%, 30-year amortization, 10-year term, monthly payments in arrears. Variant: the first 36 months are interest-only, then amortization on the original 30-year schedule.

**Find.** Monthly payment; annual debt service; year-1 interest and principal; balance after 120 months; total principal and interest paid over the term; the balloon with three years of IO.

**Solution.**

$i = 0.065/12 = 0.0054167$; $n = 360$.

$PMT = 25{,}000{,}000 \times 0.0054167/(1 - 1.0054167^{-360}) = \$158{,}017.01$ per month; $DS = \$1{,}896{,}204$ per year.

Year-1 interest = \$1,616,773; year-1 principal = \$279,431. Only 14.7% of first-year debt service reduces principal.

Balance after 120 payments (prospective form): $B_{120} = 158{,}017.01 \times a_{\overline{240}|i} = \$21{,}194{,}032$.

Principal repaid over 10 years: $25{,}000{,}000 - 21{,}194{,}032 = \$3{,}805{,}968$ (15.2% of the loan). Interest paid: $120 \times 158{,}017.01 - 3{,}805{,}968 = \$15{,}156{,}072$.

**Three years IO.** Months 1–36: payment = $25{,}000{,}000 \times 0.065/12 = \$135{,}417$ ($DS = \$1{,}625{,}000$). Months 37–120: the 30-year payment of \$158,017.01. Balloon = balance after 84 amortizing payments = **\$22,604,061**, which is \$1,410,030 higher than with full amortization.

**HP-12C keystrokes** (END mode; `f 2` display):

| Step | Keys | Display |
|---|---|---|
| Clear | `f` `CLEAR FIN` | |
| Loan | `25000000` `PV` | 25,000,000.00 |
| Rate | `6.5` `g` `12÷` | 0.54 |
| Term | `30` `g` `12×` | 360.00 |
| Payment | `PMT` | −158,017.01 |
| Balloon at month 120 | `120` `n` `FV` | −21,194,031.59 |
| Alternative: amortize 120 payments | (re-enter PV, i, n=360, PMT as above) `120` `f` `AMORT` | −15,156,072.30 (interest) |
| | `x≷y` | −3,805,968.41 (principal) |
| | `RCL` `PV` | 21,194,031.59 |
| IO variant: balloon after 84 amortizing months | `f CLEAR FIN`, `25000000 PV`, `6.5 g 12÷`, `360 n`, `PMT`, then `84` `n` `FV` | −22,604,061.20 |

The `AMORT` function rounds each period's interest to the display setting, so with `f 2` its results can differ from the closed form by a few cents. The `n`/`FV` route uses the unrounded payment held in the PMT register.

**Check.** Retrospective form: $25{,}000{,}000 \times 1.0054167^{120} - 158{,}017.01 \times (1.0054167^{120} - 1)/0.0054167 = \$21{,}194{,}032$, which matches the prospective form. ✓

**Decision consequence.** A 30-year amortization on a 10-year loan retires only 15% of principal. The refinancing risk at year 10 is therefore about 85% of the original loan, and about 90% with three years of IO. Underwriting that focuses on the year-1 DSCR is underwriting the wrong date. The question to ask is: on what NOI, cap rate, and lending terms does a \$21.2 million (or \$22.6 million) balloon refinance in year 10? (§10.6, Example 10.6.)

### Example 10.3 — Floating-rate debt, the cap, and the cost of replacing it (Ridgeview)

**Given.** Ridgeview at acquisition: value \$40,000,000, NOI \$2,100,000. Bridge loan terms: SOFR + 3.25%, IO, max 75% LTV, min 1.10x DSCR **sized at the cap strike** of 3.00% SOFR. Two-year cap, quarterly caplets, on \$30,000,000. Flat forward curve and normal volatility are hypothetical: at acquisition, forward SOFR 1.25% with normal vol 0.80% (80 bp); at replacement, forward SOFR 4.75% with normal vol 1.20%.

**Find.** (a) The loan amount. (b) Interest and DSCR at SOFR of 0.05% and 5.30%, with and without the cap. (c) The upfront cost of the cap at acquisition and at replacement, as a percentage of notional and as an annual equivalent. (d) The replacement cost at strikes of 4.75% and 5.00%.

**Solution.**

(a) Sizing rate = 3.00% + 3.25% = 6.25%. DSCR loan $= 2{,}100{,}000/1.10/0.0625 = \$30{,}545{,}455$. LTV loan $= 0.75 \times 40{,}000{,}000 = \$30{,}000{,}000$. LTV binds: $L = \$30{,}000{,}000$.

(b)

| SOFR | Unhedged rate | Unhedged interest | DSCR | Capped rate | Capped interest | DSCR | Cap payout/yr |
|---|---|---|---|---|---|---|---|
| 0.05% | 3.30% | \$990,000 | 2.12x | 3.30% | \$990,000 | 2.12x | \$0 |
| 5.30% | 8.55% | \$2,565,000 | 0.82x | 6.25% | \$1,875,000 | 1.12x | \$690,000 |

(c) Caplets $j = 2,\dots,8$ fix at $t = 0.25, \dots, 1.75$ and pay one quarter later; the first period is already fixed. Discount factors use the flat forward compounded quarterly.

* Acquisition ($F = 1.25\%$, $\sigma_N = 0.80\%$): premium **\$3,680**, or 0.012% of notional, about 0.6 bp a year.
* Replacement ($F = 4.75\%$, $\sigma_N = 1.20\%$): premium **\$888,370**, or 2.96% of notional. Dividing by the quarterly annuity of 1.8972 gives an annual equivalent of **156 bp**.

(d) Replacement at a 4.75% strike (at the money): \$226,647. At a 5.00% strike: \$170,675 (30 bp a year).

**Check.** Most of the 3.00%-strike replacement premium is intrinsic value: seven caplets each worth $30{,}000{,}000 \times 0.25 \times (0.0475 - 0.03) \times P_j = 131{,}250\,P_j$ at expiry, summing to \$866,331 discounted. Time value adds the remaining \$22,039. ✓

**Decision consequence.** The original cap was nearly free because it was far out of the money. The same strike, bought when the forward is above it, costs almost 3% of the loan, payable in cash up front, at the moment the property's cash flow is already absorbed by higher interest. Buying a higher strike lowers the premium but raises the sizing rate, so the loan may fail the extension DSCR test. The cap protects the lender's DSCR. It does not protect the sponsor's liquidity. A sponsor who underwrote "the cap limits our rate risk" was right about the interest rate and wrong about the cash requirement.

### Example 10.4 — The capital stack: attachment, detachment, and who loses first

**Given.** A \$50,000,000 office acquisition with NOI \$3,250,000 (6.50% cap). Senior loan \$30,000,000 at 6.00%, 30-year amortization (0–60%). Mezzanine \$7,500,000 at 11.0% IO (60–75%). Preferred equity \$5,000,000 at a 12% current-pay preference (75–85%). Common equity \$7,500,000 (85–100%).

**Find.** Coverage at each level; losses by tranche if value falls to \$40.0 million, \$35.0 million, and \$32.5 million; the value declines at which mezz is first impaired and wiped out.

**Solution.**

Senior DS $= \$2{,}158{,}382$ (DSCR 1.51x, DY 10.83%). Mezz DS $= 7{,}500{,}000 \times 0.11 = \$825{,}000$. Combined DSCR $= 3{,}250{,}000/2{,}983{,}382 = 1.09x$. Debt yield through the mezz $= 3{,}250{,}000/37{,}500{,}000 = 8.67\%$. Pref current pay \$600,000. Cash after senior, mezz and pref: $3{,}250{,}000 - 2{,}158{,}382 - 825{,}000 - 600{,}000 = -\$333{,}382$. The pref cannot be paid currently from property cash flow. It accrues.

| Tranche | Attach–detach | Loss at \$40.0m | Loss at \$35.0m | Loss at \$32.5m |
|---|---|---|---|---|
| Senior \$30.0m | 0–60% | 0 | 0 | 0 |
| Mezz \$7.5m | 60–75% | 0 | \$2.5m (33%) | \$5.0m (67%) |
| Pref \$5.0m | 75–85% | \$2.5m (50%) | \$5.0m (100%) | \$5.0m (100%) |
| Common \$7.5m | 85–100% | \$7.5m (100%) | \$7.5m (100%) | \$7.5m (100%) |

Mezz is impaired once value falls more than $1 - 0.75 = 25\%$, and wiped out beyond $1 - 0.60 = 40\%$.

**Check.** Losses sum to the value decline in each column: $10.0$, $15.0$, $17.5$ million. ✓

**Decision consequence.** A 20% value decline wipes out the common and half the pref while the mezz is untouched. The mezz lender's real risk is not the 25% decline threshold. It is **control**: when the common is wiped out, the mezz lender becomes the effective owner. It must be ready to foreclose on the equity pledge, cure senior defaults, and own an office building. The intercreditor agreement determines what it must do to get there: a typical agreement requires the mezz lender to cure monetary defaults on the senior loan, to be or hire a "qualified transferee" acceptable to the senior lender, and to replace any recourse guarantor. Preferred equity at 75–85% is economically a junior mezz loan without a lien, so it relies entirely on the partnership agreement's control rights. An investor who prices pref at 12% "because it is senior to the common" is pricing the wrong risk.

### Example 10.5 — The waterfall and the promote as an option

**Given.** Total equity \$10,000,000 (90% LP, 10% GP co-invest, pooled). Annual flows, base case: −10.00, 0.60, 0.65, 0.70, 0.75, 14.00 (\$ million). Downside: −10.0, 0.5, 0.5, 0.5, 0.5, 10.5. Upside: as base, but 17.0 in year 5. Waterfall: 100% to investors until an 8% IRR; 80/20 until 12%; 70/30 thereafter. Catch-up comparison: \$10,000,000 contributed, a single distribution after five years, 8% compounding pref, 20% carry.

**Find.** Project IRR, investor IRR, and promote in each case; then the GP share with and without a full catch-up when the terminal distribution is \$18.0 million.

**Solution.** Using `cre.irr_hurdle_waterfall(flows, [0.08, 0.12], [1.0, 0.8, 0.7])`:

| Case | Project IRR | Investor IRR (after promote) | Promote |
|---|---|---|---|
| Downside | 5.00% | 5.00% | \$0 |
| Base | 11.93% | 11.19% | \$513,661 |
| Upside | 15.89% | 14.19% | \$1,343,451 |

Catch-up comparison: pref amount $= 10{,}000{,}000 \times (1.08^5 - 1) = \$4{,}693{,}281$. Total profit \$8,000,000.

* Full catch-up ($\gamma = 1$): GP receives 100% of distributions after the pref until it holds 20% of profit; GP = **\$1,600,000**; investors \$16,400,000 (IRR 10.40%).
* No catch-up: GP receives 20% only of profit above the pref: $0.20 \times (8{,}000{,}000 - 4{,}693{,}281) = \$661{,}344$; investors \$17,338,656.

The catch-up tier is $x = 0.2 \times 4{,}693{,}281/0.8 = \$1{,}173{,}320$, so it is complete when terminal distributions reach $10{,}000{,}000 + 4{,}693{,}281 + 1{,}173{,}320 = \$15{,}866{,}601$. At that point the GP holds exactly 20% of \$5,866,601 of profit. Above it, every dollar splits 80/20 and the GP's share stays at 20%. Investor IRR at \$18.0 million: 10.40% with the catch-up, 11.64% without.

**Check.** Base case: investor flows plus promote equal project flows in every year. ✓ (tested)

**Decision consequence.** The promote is zero in the downside and grows faster than profit in the upside: from base to upside, project profit rises \$3.0 million and the promote rises \$0.83 million, 28% of the increment. That convexity is the point of a promote and also its hazard. A GP whose promote is out of the money gains from volatility and loses nothing extra from failure beyond its co-invest. In Case B the promote is out of the money in every state, and the GP's remaining incentive is its fee stream. A catch-up shifts \$0.94 million to the GP at \$18 million of distributions in this example. LPs should value a catch-up as a transfer at good outcomes, not as a technicality.

### Example 10.6 — The refinancing gap on a "good" asset

**Given.** Five years ago, an industrial property with NOI \$2,000,000 was bought at a 4.75% cap (\$42,105,263) with a \$26,000,000 loan at 3.25%, 30-year amortization, 5-year term. Today NOI is \$2,200,000 (up 10%). The market cap rate is 6.25%. New loan terms: 6.50%, 30-year amortization, max 65% LTV, min 1.25x DSCR, min 9.0% debt yield; costs 1.5% of the new loan.

**Find.** The balloon, today's value, the new loan, the refinancing gap, and the change in equity value and cash flow.

**Solution.**

Old DS $= \$1{,}357{,}844$. Balloon $B_{60} = \$23{,}219{,}757$.

Value $= 2{,}200{,}000/0.0625 = \$35{,}200{,}000$ (−16.4% despite +10% NOI).

| Constraint | Loan |
|---|---|
| LTV 65% | \$22,880,000 |
| DSCR 1.25x at $K = 7.5848\%$ | \$23,204,254 |
| Debt yield 9.0% | \$24,444,444 |

LTV binds at \$22,880,000. Costs \$343,200. Gap $= 23{,}219{,}757 + 343{,}200 - 22{,}880{,}000 = \$682{,}957$.

Equity value: \$16,105,263 at purchase; $35{,}200{,}000 - 23{,}219{,}757 = \$11{,}980{,}243$ today. New DS $= \$1{,}735{,}406$. Cash flow after debt service falls from \$842,156 to \$464,594.

**Check.** If the old balance were refinanced at 6.50%/30 years, DSCR would be $2{,}200{,}000/(23{,}219{,}757 \times 0.075848) = 1.249x$, just below 1.25x; the gap is LTV-driven, not coverage-driven. ✓

**Decision consequence.** NOI rose and the owner still has to write a \$0.68 million check to keep the asset, after which cash yield on remaining equity falls by almost half. This is the mild form of the refinancing cliff: a positive-equity sponsor funds the gap because the alternative is losing \$12 million of equity. The question is whether to fund it with the sponsor's cash, with partner capital calls (Example 10.9), or with expensive mezzanine debt. The severe form, where equity is negative and the gap exceeds the equity, is Case B.

### Example 10.7 — Cash traps and cures (Ridgeview, year 3)

**Given.** Ridgeview's \$30,000,000 bridge loan, with SOFR above the 3.00% strike, so the capped rate is 6.25%. NOI \$2,100,000. Cash management triggers: DSCR below 1.20x (at the actual capped rate) or debt yield below 7.50%. When triggered, all excess cash after debt service is trapped in a lender-controlled account. A cure requires both tests to be met for two consecutive quarters, or a principal paydown that restores them.

**Find.** DSCR, DY, the trapped cash per year, the paydown needed to cure, and how long the trap would take to cure if the trapped cash were applied to principal.

**Solution.** DS $= 30{,}000{,}000 \times 0.0625 = \$1{,}875{,}000$; DSCR $= 1.12x$; DY $= 7.00\%$. Both tests fail. Trapped cash $= 2{,}100{,}000 - 1{,}875{,}000 = \$225{,}000$ a year.

Paydown to cure DSCR: $L$ must satisfy $2{,}100{,}000/(0.0625 L) \ge 1.20$, so $L \le \$28{,}000{,}000$: paydown \$2,000,000. Paydown to cure DY: $L \le 2{,}100{,}000/0.075 = \$28{,}000{,}000$: the same \$2,000,000, because $1.20 \times 6.25\% = 7.50\%$ (§10.4.2).

If trapped cash were swept to principal, the cure would take $2{,}000{,}000/(225{,}000/12) = 106.7$ months, far longer than the loan's remaining term.

**Check.** At $L = 28{,}000{,}000$: $2{,}100{,}000/1{,}750{,}000 = 1.20x$ and $2{,}100{,}000/28{,}000{,}000 = 7.50\%$. ✓

**Decision consequence.** The cash trap does not resolve the problem. It changes who controls the cash while the problem persists. For the sponsor, the trap ends distributions, which ends the LPs' current return and often the sponsor's ability to pay its own overhead. That creates pressure to inject capital to "cure", which is rational only if the equity option is worth more than the cure (Example 10.8). For the lender, trapped cash is a reserve against the next cap purchase or a partial paydown. A rescue investor should notice that \$2.0 million of the sponsor's \$5.0 million request goes to cure a test, not to create value.

### Example 10.8 — The borrower's default option and the bargaining zone (Ridgeview at maturity)

**Given.** Ridgeview's \$30,000,000 non-recourse loan is at maturity. Value today \$27,000,000. In one year value will be \$33.0m, \$27.0m, or \$21.0m with probabilities 0.30, 0.40, 0.30. Property cash flow pays interest in both paths and is ignored. The lender offers a one-year extension for a fee $f$. Sponsor required return on new money 15%. Lender opportunity rate 8%. Foreclosure, holding and sale costs 8% of value; a foreclosure sale, or the sale of a property returned at maturity, closes in one year. The sponsor's principal has signed a springing-recourse guarantee triggered by a voluntary bankruptcy filing.

**Find.** The value of the sponsor's option; the maximum fee the sponsor will pay; the lender's PV under foreclosure and extension; the bargaining zone; the deficiency exposure if the sponsor files for bankruptcy to delay foreclosure.

**Solution.**

Sponsor: $E[\max(V_1 - 30, 0)] = 0.30 \times 3.0 = \$0.90$ million. PV at 15% = **\$782,609**. Intrinsic value today is zero ($27 < 30$), so all \$782,609 is time value. Note that $E[V_1] = \$27.0$ million, equal to today's value: the option value comes from dispersion, not drift. Maximum fee = \$782,609.

Lender, foreclosure: $27{,}000{,}000 \times 0.92 = \$24{,}840{,}000$ at $t=1$; PV at 8% = **\$23,000,000**.

Lender, extension: recovery at $t=1$ is \$30.0m if $V_1 \ge 30$; otherwise $V_1 \times 0.92$. $E = 0.30(30.0) + 0.40(24.84) + 0.30(19.32) = \$24{,}732{,}000$; PV = \$22,900,000, plus the fee.

Bargaining zone: the lender needs $22{,}900{,}000 + f \ge 23{,}000{,}000$, so $f \ge \$100{,}000$. The sponsor accepts $f \le \$782{,}609$. Any fee in **[\$100,000, \$782,609]** makes both better off than foreclosure today.

Bankruptcy deficiency: $30{,}000{,}000 - 24{,}840{,}000 = \$5{,}160{,}000$ owed personally by the guarantor if the springing-recourse trigger is pulled.

**Check.** At $f = 782{,}609$ the sponsor's NPV is zero; at $f = 100{,}000$ the lender's PV equals foreclosure. ✓

**Decision consequence.** Extension is efficient here: it preserves an option worth \$0.78 million to the sponsor at an expected cost to the lender of only \$0.10 million. Calling that "extend and pretend" would be wrong. It becomes extend-and-pretend when the lender's accounting, not the economics, drives the decision (Example 10.10). The springing guarantee does its job: a filing that might delay foreclosure by a year and preserve the option is worth at most \$0.78 million to the sponsor, against a \$5.16 million personal deficiency. The guarantee converts an obstruction strategy into a cooperative one (deed-in-lieu or a negotiated extension). That is why lenders insist on carve-outs from a creditworthy individual, and why a carve-out guarantor with no assets is a weaker structure than its paper suggests.

### Example 10.9 — Capital-call dilution: who transfers value to whom

**Given.** A joint venture with 100 units: LP 90, GP 10, originally priced at \$100,000 a unit (\$10.0 million contributed). A \$3,000,000 capital call is needed to fund a refinancing gap. The pre-call fair value of the equity is \$4,000,000 (\$40,000 a unit). The LP will fund. The GP cannot. Compare: (a) both fund; (b) LP funds both shares, units issued at fair value; (c) as (b) with a 150% punitive credit on the GP's share; (d) LP funds both shares, units issued at the original \$100,000 price.

**Find.** GP ownership and the value of the GP's stake after the call (post-call equity \$7,000,000).

**Solution.**

| Case | New LP units | GP ownership | GP stake value | Transfer to (from) GP vs. fair |
|---|---|---|---|---|
| (a) Both fund | 67.5 (GP buys 7.5) | 10.00% | \$700,000 (after paying \$300,000) | 0 |
| (b) Fair value, no penalty | 75.0 | 5.714% | \$400,000 | 0 |
| (c) Fair value, 150% credit | 78.75 | 5.594% | \$391,608 | (\$8,392) |
| (d) Issued at \$100,000 | 30.0 | 7.692% | \$538,462 | +\$138,462 |

In (b), the GP's \$400,000 equals 10% of the \$4.0 million pre-call value: issuing at fair value is value-neutral. In (d), issuing units at the historical price, which is above today's value, **rewards** the non-funding partner. Even with a 150% credit at the historical price, the LP receives 31.5 units, the GP keeps 7.605%, and the GP's stake is worth \$532,319.

**Check.** (b): $10/(90 + 75 + 10) = 5.714\%$; $5.714\% \times 7{,}000{,}000 = 400{,}000$. ✓

**Decision consequence.** Many joint-venture agreements price capital-call units at capital-account or "book" value, which made sense when calls were expected to fund growth at values above cost. In a downturn the same clause penalizes the partner who funds and rewards the one who does not. A 150% punitive credit at book value still leaves the GP better off than fair-value issuance (\$532,319 against \$400,000). Before funding a call, compute the post-call value of your stake under the document's actual pricing rule, not the percentage it shows.

### Example 10.10 — Buying the distressed note, and why the bank might not sell (Ridgeview)

**Given.** The bank will sell Ridgeview's \$30,000,000 defaulted note for \$24,000,000 (80% of par). You model three resolutions, with no interest received during the workout:

| Resolution | Probability | Gross recovery | Costs | Years |
|---|---|---|---|---|
| Modification, then payoff at par | 0.25 | \$30,000,000 | \$300,000 | 2 |
| DPO | 0.35 | \$26,500,000 | \$250,000 | 1 |
| Foreclosure and REO sale | 0.40 | \$27,000,000 | \$1,800,000 | 2 |

Your required return is 12%. The bank's cost of funds and hurdle on this asset is 6%, and it carries the note at par.

**Find.** Expected PV at 12%; NPV at the ask; scenario returns; the bank's PV at 6%.

**Solution.** Using `cre.distressed_loan_recovery`:

| Resolution | Net | PV at 12% | Annualized return on \$24.0m |
|---|---|---|---|
| Mod + payoff | \$29,700,000 | \$23,676,658 | 11.24% |
| DPO | \$26,250,000 | \$23,437,500 | 9.38% |
| Foreclosure | \$25,200,000 | \$20,089,286 | 2.47% |

Expected PV $= 0.25(23.68) + 0.35(23.44) + 0.40(20.09) = \$22{,}158{,}004$. NPV at \$24.0 million = **−\$1,841,996**. Maximum bid at 12%: \$22.16 million, 73.9% of par.

Bank's PV of the same resolutions at 6%: **\$24,246,841**, about \$0.25 million above the bid. Selling at \$24.0 million also realizes a \$6.0 million loss against the \$30.0 million carrying value.

**Check.** No scenario earns 12% at the ask, so expected PV at 12% must be below \$24.0 million. ✓

**Decision consequence.** Do not buy at 80. The bank's economic value of the note at its own cost of capital is already \$5.75 million below par; selling makes that loss visible now, while an extension keeps the loan at par on the bank's books for as long as accounting and examiners allow. That is the precise meaning of "extend and pretend": the lender's private value of delay includes avoided loss recognition and capital charges, which a note buyer does not share. The gap between a 6% holder and a 12% buyer, about \$2.1 million here, is the price of moving the risk to a specialist. Expect bid–ask gaps in distressed loan markets to close only when regulators, auditors, or the lender's own liquidity force recognition (Chapter 12).

---

## 10.6 CRE application: reading a loan as a sequence of dates

A loan document is a set of dated tests. Underwriting it means asking what NOI, rates, and values must hold on each date for the borrower to keep control.

| Date | Test | What fails it | Who gains control |
|---|---|---|---|
| Closing | LTV/LTC, DSCR at sizing rate, DY | Appraisal, rate, NOI | — |
| Each quarter | DSCR/DY cash-management triggers | NOI decline, rate rise (floating), cap expiry | Lender controls cash |
| Cap expiry | Replacement cap at required strike | Forward rates above strike | Lender (default if not bought) |
| Extension date | Extension DSCR/DY/LTV tests, fee, new cap | Same, plus value | Lender (maturity default) |
| Maturity | Refinance or repay balloon | Gap $G > 0$ | Lender (foreclosure, DPO, or extension) |

**Covenants.** Financial covenants (minimum DSCR, minimum DY, maximum LTV, minimum guarantor net worth and liquidity) usually do not cause immediate acceleration in CRE loans. They trigger cash management, reserve deposits, or rebalancing (paydown) obligations. Non-financial covenants (transfer restrictions, single-purpose-entity requirements, reporting) protect the lender's ability to enforce. Violating the transfer and SPE covenants is typically what springs full recourse.

**Recourse versus non-recourse.** Non-recourse debt prices the default option into the spread. Recourse debt from a creditworthy guarantor removes most of that option and is cheaper. The sponsor should value the difference explicitly: Example 10.8's put is worth \$0.78 million to the sponsor on a \$30 million loan over one year. Over a five-year term, in a volatile asset class, the put is worth much more. Banks often lend with partial recourse (a percentage of the loan, burning off as DSCR or DY targets are met). The burn-off tests are covenants in disguise.

**Lender types.** [INFERENCE from standard market structure; Chapters 12 and 17 document the details] Banks hold loans on balance sheet and can extend; CMBS loans are administered by servicers under pooling and servicing agreements that restrict modification until default and transfer to a special servicer; debt funds and CRE CLOs funded floating-rate bridge loans, and their own financing (repurchase lines, CLO coverage tests) can force them to act faster than banks. The same property in the same distress can receive a quick extension from a bank, a slow, rule-bound special-servicer process in CMBS, or a fast enforcement from a debt fund whose own lender is calling margin.

**Mezzanine and preferred equity in a recapitalization.** New junior capital raises proceeds but makes the stack more fragile. In Example 10.4 the combined DSCR is 1.09x, so a 9% NOI decline makes the mezz interest uncoverable. A rescue investor should insist on: (1) seniority to all existing equity, including its accrued preference; (2) control rights on default (removal of the GP, a forced sale); (3) a cash-flow sweep after its current pay; and (4) a recognition agreement from the senior lender, which mezz has through the intercreditor and pref usually does not.

**Distressed purchases.** A buyer can buy the property (after foreclosure), the note (before resolution), or a junior position (mezz or pref) that controls the equity. Buying the note buys the lender's remedies and the lender's timeline. Buying the mezz near its attachment point buys control at a low price but obliges the buyer to cure the senior loan.

---

## 10.7 When the relationships fail

1. **DSCR on trailing NOI misses the cap expiry.** A floating-rate loan sized at the strike can pass every covenant until the day the cap expires. The relevant DSCR is at the forward index on the next cap date, plus the cap's cost.
2. **LTV relies on a value that does not exist.** In illiquid markets appraisals lag (Chapter 2). A 65% LTV on a stale appraisal can be 85% on a clearing price. Debt yield is the more robust test because it uses income alone.
3. **Non-recourse is not non-recourse for everyone.** Carve-out guarantees, environmental indemnities, and completion guarantees create personal exposure that sponsors sometimes treat as remote. Whether and how a given carve-out is enforced is a legal question that depends on the documents and the jurisdiction; this book does not rely on specific court holdings. The analytical point is that the guarantee's value depends on the guarantor's assets and on which acts trigger it.
4. **Waterfall hurdles measured on IRR can be gamed by timing.** Early distributions (from a refinancing) raise IRR without raising multiple. A promote that crystallizes on an IRR test after an early cash-out refinance may pay the GP before the LP's capital is safe. Look-back and clawback provisions, and multiple-based hurdles, address this.
5. **"Senior to the common" is not "safe".** Preferred equity and mezz sit at 75–85% and 60–75% in Example 10.4. Their loss probability is governed by the probability of value declines of 15–40%. Whether such declines are rare is an empirical question by property type and period, which Chapter 23 examines; do not assume it.
6. **The lender may not behave as the option model predicts.** Regulatory capital, accounting, servicer standards, workout staff capacity, and reputational concerns enter the lender's objective. The bargaining zone in Example 10.8 can be wider or narrower than the economics alone imply.
7. **Correlated maturities break the refinancing market itself.** The refinancing gap assumes a lender exists at the stated terms. When many loans mature at once into a market where lenders are also impaired, the new-loan terms are not exogenous.

---

## 10.8 Lender and sponsor incentives

**Moral hazard in non-recourse debt.** Once equity is out of the money, the sponsor's payoff is a call. Calls gain from volatility. A sponsor with negative equity prefers riskier strategies (speculative re-leasing, deferred maintenance, aggressive lease-up concessions) because the lender bears the downside. Covenants, cash management, and recourse carve-outs are the lender's tools to limit this.

**The GP's fee incentive.** A GP whose promote is worthless still earns asset-management and property-management fees while the partnership owns the asset. In Case B the GP's 10% co-invest share of a fresh-equity refinance is negative, but adding three years of fees makes the GP's private payoff positive while the LP's is −\$2.8 million. LPs must compute the GP's private payoff from each strategy before accepting a GP recommendation.

**The lender's accounting incentive.** A lender carrying a loan at par must recognize a loss on sale or foreclosure. An extension, if it passes accounting and supervisory tests, defers recognition. In Example 10.10 the bank's economic value is \$24.2 million against a \$30.0 million book value. Extending keeps \$5.75 million of economic loss off the income statement for now. The lender is not wrong to extend when the extension is economically efficient (Example 10.8). It is wrong when the extension is chosen because it defers recognition, and the collateral is deteriorating while it waits.

**The special servicer's incentive.** CMBS special servicers earn workout and liquidation fees and may be affiliated with the controlling (most junior) bondholder. The controlling class prefers strategies that delay realized losses, which would wipe it out [INFERENCE from CMBS structure; Chapter 17 develops tranche incentives].

**Alignment tools.** For LPs: GP co-invest that is material relative to GP net worth; fee offsets; promote clawbacks; removal rights. For lenders: recourse carve-outs, cash management, and sizing on debt yield. For rescue investors: seniority, control, and a price that is right without assuming the sponsor's business plan.

---

## 10.9 Historical episode: floating-rate bridge loans and the rate-cap squeeze, 2022–2024

**Date and environment.** On 16 March 2022 the Federal Open Market Committee raised the target range for the federal funds rate to 1/4 to 1/2 percent, the first increase of the cycle [FACT: FOMC statement, 16 March 2022; ch10-S01, VERIFIED-PRIMARY]. On 26 July 2023 it raised the range to 5-1/4 to 5-1/2 percent [FACT: FOMC statement, 26 July 2023; ch10-S02, VERIFIED-PRIMARY], a cumulative increase of 525 bp in about sixteen months. SOFR, the index for most new floating-rate CRE loans, is a secured overnight rate that trades close to the policy range [INFERENCE from the policy implementation framework; the daily SOFR series on FRED was not retrieved for this edition, so no specific SOFR prints are quoted].

**What the loans looked like.** [INFERENCE from standard market structure, consistent with the GSE disclosures below] Value-add multifamily acquisitions in 2020–2022 were often financed with short-term (two- to three-year initial term) floating-rate bridge loans at high LTV, interest-only, with interest-rate caps required by the lender. Many such loans were funded by debt funds and securitized in CRE CLOs. A Federal Reserve Bank of Philadelphia working paper describes CRE CLOs as securitizations backed by pools of floating-rate, interest-only loans and reports that multifamily made up about three-quarters of their collateral [FACT: Philadelphia Fed Working Paper 25-43; ch10-S08, VERIFIED-SECONDARY].

**The cap mechanism.** Fannie Mae's 2023 annual report states that it generally requires multifamily borrowers with adjustable-rate loans to maintain interest-rate caps for the life of the loan, with escrows for replacement caps, and that rising cap replacement costs contributed to the increase in its multifamily serious delinquency rate in 2023 [FACT: Fannie Mae Form 10-K for 2023; ch10-S04, VERIFIED-SECONDARY: read via search excerpt of the SEC filing]. Freddie Mac's January 2024 *Multifamily Maturity Risk* research note describes a cap as functioning like insurance against the rate rising above the underwritten rate, and notes that floating-rate loans may come under more stress because of higher rates and cap premiums [FACT: ch10-S05, VERIFIED-SECONDARY; paraphrased from a search excerpt, not quoted]. Trade press reported that replacement-cap prices rose by more than an order of magnitude between 2019 and 2023 *(verification pending; ch10-S10, class C; no figure is used)*. Example 10.3 shows why: a cap bought far out of the money costs almost nothing, and the same strike bought after forwards rise above it is mostly prepaid intrinsic value.

**The maturity wall.** The Mortgage Bankers Association reported in February 2024 that \$929 billion, 20% of the \$4.7 trillion of outstanding commercial and multifamily mortgages held by lenders and investors, would mature in 2024, a 28% increase from the \$729 billion that matured in 2023, and attributed much of the increase to loans extended or modified in 2023. It also reported that 38% of hotel/motel loan balances and 25% of office balances would mature in 2024, against only 3% (\$28 billion) of multifamily and health-care mortgages held or guaranteed by Fannie Mae, Freddie Mac, FHA, and Ginnie Mae [FACT: MBA, "20 Percent of Commercial and Multifamily Mortgage Balances Mature in 2024", 12 February 2024; ch10-S03, VERIFIED-PRIMARY]. Different data providers estimate different totals; the MBA figure is a survey of lenders' own holdings.

**What the official sector said.** The Federal Reserve's April 2024 *Financial Stability Report* noted that delinquency rates on CRE loans, especially those backed by office properties, increased in the second half of 2023 [FACT: ch10-S06, VERIFIED-SECONDARY]. Its November 2024 *Supervision and Regulation Report* noted that multifamily delinquencies at large banks had risen steadily from a low base and that valuations had declined for certain multifamily properties [FACT: ch10-S07, VERIFIED-SECONDARY]. The Philadelphia Fed working paper reports CRE CLO delinquency rates in 2024 of 12.64% for static and 8.41% for managed deals, up from 0.63% and 1.20% in 2019 [FACT: ch10-S08, VERIFIED-SECONDARY; delinquency definitions follow the paper's data source]. The Federal Reserve's May 2023 report explicitly excluded multifamily mortgages from its CRE price-vulnerability analysis because the sector's fundamentals differ [FACT: ch10-S09, VERIFIED-SECONDARY].

**What was knowable at origination (2020–2022).** That the loans floated, that caps would expire before loan maturity, and that extension tests required new caps were all in the loan documents. The forward curve in 2021 implied low future rates [INFERENCE: consistent with the near-zero policy range before March 2022]. What was not knowable was the speed of the 2022–23 tightening: 525 bp in about sixteen months (ch10-S01, S02). A sponsor who stress-tested "SOFR at the cap strike for the full term" would have found the debt service bearable. A sponsor who also tested "the cost of a replacement cap when forwards are above the strike" would have found a cash requirement of several percent of the loan at each extension (Example 10.3).

**Interpretations.**

* *Rate shock.* Floating-rate debt transferred the policy shock directly to borrowers. Caps delayed it but did not remove it, because caps were shorter than the loans.
* *Underwriting.* High-LTV bridge loans sized on projected (post-renovation) NOI were vulnerable to any delay in the business plan, and expense growth (insurance, payroll) delayed many plans. On this view, rates exposed weak underwriting rather than causing losses on their own.
* *Structure.* CRE CLO and debt-fund lenders, financed with their own short-term or market-value-sensitive liabilities, had less ability to extend than banks [HYPOTHESIS for this edition; to be tested against servicer and rating-agency data].

**What the episode establishes.** That a hedge with a shorter maturity than the exposure is a roll-over bet on the price of the hedge. That DSCR sized at the cap strike is a statement about debt service, not about liquidity. That maturity walls are partly manufactured by extensions, which move maturities rather than resolve them (the MBA's own attribution of the 2024 increase).

**What it does not establish.** It does not establish loss severities on multifamily bridge loans as a class: delinquency is not loss, and resolution data are incomplete. It does not show that floating-rate debt is imprudent in general: a borrower with a matched-maturity cap, lower leverage, or a shorter business plan would have fared differently. It does not establish that 2007–09-style CMBS losses recurred; that comparison requires loss data not used here (Chapter 23 treats 2007–09).

**CRE connection.** Case B studies the fixed-rate version of the same cliff: a loan whose coupon was safe until the day it had to be refinanced.

---

## 10.10 Decision exercise: Ridgeview

Return to §10.1. Use Examples 10.3, 10.7, 10.8, and 10.10. Write a one-page decision record (`desk/investment_memos/decision_record_template.md`) that answers:

1. **What does the \$5.0 million buy?** Allocate it: replacement cap (about \$0.89 million at a 3.00% strike, less at a higher strike), the \$2.0 million cure paydown, renovation capital. Which uses create value and which only preserve the sponsor's option?
2. **Where does the pref attach?** With the loan at \$28.0 million after the paydown and value about \$27 million, the pref attaches above 100% of current value. What value must Ridgeview reach for the pref to be repaid in full, and in which of Example 10.8's states does that happen?
3. **Is the note at 80 better?** Compare your answer from Example 10.10 with the pref.
4. **What would you need to see** to invest in either: a signed extension from the lender with stated tests; a replacement cap bid; renovation results on the completed units (rent premiums achieved versus plan); insurance renewal; the GP's ability to fund its share.
5. **What is your decision?** Abstention is a legitimate answer, and is likely the best answer at the proposed terms.

**Rubric (see `problems/solutions/ch10_solutions.md` §Decision exercise).** Full credit requires: identifying that the pref attaches above current value and is therefore equity risk priced as credit; noting that \$2.0 million cures a test rather than creating value; valuing the note below 80 at a 12% target (Example 10.10); stating the conditions under which either investment would be acceptable (for example, pref only with the senior lender's extension signed, a lower attachment through a larger paydown by the existing equity, and control rights); and an explicit abstain/invest decision with invalidation criteria.

---

## 10.11 Frequent analytical errors

1. **Sizing on the coupon instead of the loan constant.** DSCR uses debt service, which includes amortization. A 6.50% loan on 30-year amortization has a 7.58% constant.
2. **Treating IO as free proceeds.** IO raises proceeds by moving principal repayment to the balloon (Example 10.2).
3. **Underwriting DSCR at today's index for floating debt.** Underwrite at the strike, at the forward index after cap expiry, and include the replacement cap's cost.
4. **Annual versus monthly.** The mortgage rate is nominal annual; the monthly rate is $r/12$; the effective annual rate is higher. Never divide an annual debt service by 12 and call it a payment when the loan pays monthly in arrears; the annual figure is 12 × the monthly payment.
5. **Ignoring the balloon in the exit analysis.** A sale or refinance at year $T$ repays $B_T$, not $L$.
6. **Reading attachment points as safety.** A 75–85% pref loses half its value on a 20% decline (Example 10.4).
7. **Confusing waterfall IRR hurdles with multiples.** An early refinancing distribution can meet an IRR hurdle without returning capital at risk.
8. **Assuming dilution is always punitive.** It depends on the issue price relative to fair value (Example 10.9).
9. **Taking the lender's ask as its reservation price.** A bank's private value of delay includes accounting effects that a buyer does not share (Example 10.10).
10. **Ignoring guarantees in the option analysis.** Carve-outs make some exercise strategies very expensive (Example 10.8).

---

## 10.12 Connections to other chapters

* Chapter 1 §1.6 introduced leverage as the conversion of investment into speculation. This chapter adds amortization, sizing, and maturity.
* Chapter 2 explains why appraisals lag, which weakens LTV as a covenant.
* Chapter 3 develops reflexive collateral loops: falling values tighten LTV, which forces sales, which lowers values.
* Chapter 6 links cap rates to Treasury yields and the cost of capital that drives $c_T$ in the refinancing gap.
* Chapter 9 supplies the valuation inputs ($V$, loaded cap rates) used in sizing.
* Chapter 11 applies debt sizing to hotels, where NOI volatility makes debt yield the dominant test.
* Chapter 12 treats maturity walls, loan sales, foreclosure timelines, and CMBS at market scale.
* Chapter 13 analyzes hold, sell, or refinance as real options.
* Chapter 17 prices credit tranches and CMBS subordination.
* Chapter 18 prices caps, floors, and swaptions.
* Case A uses the sizing functions on a hotel acquisition. Case B applies the whole chapter to a maturing office loan.

---

## 10.13 One-page reference sheet

| Quantity | Formula |
|---|---|
| Monthly payment | $PMT = L\,i/(1-(1+i)^{-n})$, $i = r/12$ |
| Loan constant | $K = 12\,PMT/L$; IO: $K = r$ |
| Balance (prospective) | $B_k = PMT \cdot a_{\overline{n-k}\vert i}$ |
| Balance (retrospective) | $B_k = L(1+i)^k - PMT[(1+i)^k-1]/i$ |
| IO then amortizing | Balance at $T$ = $B_{T-m}$ on the original schedule |
| Max loan | $\min(\lambda V,\ NOI/(DSCR\cdot K),\ NOI/DY)$ |
| DSCR binds iff | $K > c/(\lambda\,DSCR)$ |
| IO identity | DSCR test at rate $r$ ⇔ DY test at $DSCR \cdot r$ |
| Floating interest with cap | $L(\min(I,K_{cap}) + s)$; cap pays $L\max(I-K_{cap},0)$ |
| Bachelier caplet | $N\tau P[(F-K)\Phi(d) + \sigma_N\sqrt{T}\phi(d)]$, $d = (F-K)/(\sigma_N\sqrt T)$ |
| Tranche loss | $\ell_j = \min(A_j, \max(\Delta - \sum_{k>j}A_k, 0))$ |
| Catch-up tier size | $x = \pi p/(\gamma - \pi)$ |
| Refinancing gap | $G = B_T + C - L^*_{new}$ |
| Borrower option (1 period) | $E[\max(V_1-B,0)]/(1+k_E) - f$ |
| Lender extension PV | $E[\min(B, V_1(1-\kappa))]/(1+k_L) + f$ |
| Dilution | $s_B' = U_B/(U + \text{new units})$; transfers only if issue price ≠ fair value or $\theta > 1$ |

**HP-12C:** `f CLEAR FIN`, `L PV`, `r g 12÷`, `years g 12×`, `PMT`; balloon after $k$ months: `k n FV`.

**Questions for any loan:** On what date does each test bite? What is the balloon? What does the cap cost to replace? Who controls cash after a trigger? What springs recourse? What is the sponsor's option worth, and to whom does the sponsor's private payoff differ?

---

## References for this chapter

Source IDs refer to `references/sources_ch10.md`.

* Board of Governors of the Federal Reserve System. FOMC statement, 16 March 2022. https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm (ch10-S01).
* Board of Governors of the Federal Reserve System. FOMC statement, 26 July 2023. https://www.federalreserve.gov/newsevents/pressreleases/monetary20230726a.htm (ch10-S02).
* Mortgage Bankers Association (2024). "20 Percent of Commercial and Multifamily Mortgage Balances Mature in 2024", 12 February 2024. https://www.mba.org/news-and-research/newsroom/news/2024/02/12/20-percent-of-commercial-and-multifamily-mortgage-balances-mature-in-2024 (ch10-S03).
* Fannie Mae, Form 10-K for fiscal year 2023. https://www.sec.gov/Archives/edgar/data/310522/000031052224000184/fnm-20231231.htm (ch10-S04).
* Freddie Mac Multifamily (2024). *Multifamily Maturity Risk*, January 2024. https://mf.freddiemac.com/docs/multifamily_maturity_risk_report.pdf (ch10-S05).
* Board of Governors of the Federal Reserve System (2024). *Financial Stability Report*, April 2024 (ch10-S06).
* Board of Governors of the Federal Reserve System (2024). *Supervision and Regulation Report*, November 2024, "Banking System Conditions" (ch10-S07).
* Federal Reserve Bank of Philadelphia (2025). "Does Skin in the Game Align Incentives? The Case of CRE CLOs." Working Paper 25-43 (ch10-S08).
* Board of Governors of the Federal Reserve System (2023). *Financial Stability Report*, May 2023, "Asset Valuations" (ch10-S09).
* Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École Normale Supérieure, 17, 21–86 (ch10-S11).
