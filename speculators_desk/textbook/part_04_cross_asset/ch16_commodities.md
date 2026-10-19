# Chapter 16 — Commodities

> **Status:** Complete (v1.0). Numerical examples, problems and solutions are reproduced in `tests/test_ch16_examples.py` using `models/python/sdesk/x_commodities.py`. Problems are in `problems/questions/ch16_problems.md` and solutions in `problems/solutions/ch16_solutions.md`. Drills D150–D156. Historical figures are VERIFIED-SECONDARY (search excerpts of EIA, CFTC, Dallas Fed and STR releases); items still awaiting primary confirmation are marked *(verification pending)* and listed in `references/sources_ch16.md`.

## Learning objectives

After this chapter you should be able to:

1. Explain why a commodity is a claim on a physical flow that must be produced, moved and stored, and why that makes its futures curve a statement about **inventory**, not a forecast of price.
2. Derive the cost-of-carry relationship with financing, storage and convenience yield; state which side of it is enforced by arbitrage and which is not; and back out the implied convenience yield from a quoted curve.
3. Classify a curve as contango or backwardation and connect its slope to inventory using the Working–Kaldor theory of storage, including the nonlinearity near stock-outs and near tank-tops.
4. Decompose the return on a rolling, fully collateralized futures position into **spot**, **roll** and **collateral** components exactly, and explain why a "commodity exposure" can lose money while spot is unchanged.
5. Compute P&L and notional with the correct contract multiplier and quotation unit for WTI crude, Henry Hub natural gas, gold, silver, copper and corn, including the cents-per-bushel trap.
6. Value a seasonal storage trade (natural gas) and size its hedge in contracts.
7. Trace an oil-price shock into hotel RevPAR, NOI, DSCR and value in an energy-dependent Texas market, with labeled hypothetical elasticities; size and criticize an oil hedge of that exposure.
8. Translate commodity input prices (copper, steel, lumber) into replacement cost, and judge when a developer should hedge them.

---

## 16.1 Opening investment problem: a Midland hotel, an apartment site, and a "commodity hedge"

You run acquisitions for a Texas-focused value-add fund. Three items are on Thursday's agenda. All deal facts are [HYPOTHESIS], a constructed teaching case. Market prices quoted in this section are hypothetical too. Historical facts appear only in §16.8, with sources.

**Item 1 — the hotel.** A 120-room select-service hotel in Midland is offered at \$17.8 million. The seller's trailing-12 statement shows 80% occupancy at a \$160 ADR, so RevPAR is \$128. NOI after a 4% FF&E reserve is \$1.69 million, a 9.5% cap rate. The broker's memorandum describes demand as "diversified: corporate, construction, and leisure". The STR segmentation shows that about half of room-nights are booked by oilfield-services firms, midstream contractors and their vendors. WTI front-month futures trade at \$80 per barrel. The 12-month contract trades at \$74.

**Item 2 — the apartment site.** A developer offers you a joint venture on a 150-unit garden apartment project in the same metro. The pro forma hard cost is \$27.0 million. Lumber prices have been volatile, and copper and steel have risen. The developer projects a stabilized value of \$255,000 per unit and says the deal "pencils" because that exceeds replacement cost.

**Item 3 — the inflation hedge.** A limited partner asks whether the fund should hold a long, rolling position in front-month energy futures "as an inflation hedge for our hard assets". The partner's evidence is a chart showing that spot crude rose over a period in which the partner's proposed strategy would have held it.

Three questions follow, and the chapter answers each:

* What does a \$6 backwardation between the front and the 12-month contract tell you about the Permian economy, and what does it **not** tell you?
* How much of the hotel's NOI is really an oil position, and could you hedge it with futures?
* Is a rolling futures position a claim on spot price? If not, what is it a claim on?

Section 16.9 returns to the decision.

---

## 16.2 Economic intuition

### A commodity is a flow that must be stored

A building produces rent. A bond produces coupons. A barrel of crude produces nothing while it sits in a tank. It costs money to store, insure and finance. Physical commodities therefore earn no cash yield in the usual sense. Their prices are set by the balance of a **production flow**, a **consumption flow**, and the **stock** that buffers the two.

Two facts follow:

1. **Supply and demand are both inelastic in the short run.** A shale well takes months to drill and complete. A copper mine takes years. Refineries, power plants and feedlots cannot change their consumption quickly. When a shock hits, quantities barely move at first and price does the adjusting. That is why commodity volatility is high compared with the volatility of the underlying quantities.
2. **Inventory is the shock absorber.** When inventories are ample, a supply disruption is met by drawing on stocks, and price moves little. When inventories are near their working minimum, the same disruption must be met by rationing consumption, and price spikes. When storage is nearly full, an excess of supply cannot be stored and must be sold, at whatever price clears it. Prices therefore respond **nonlinearly** to the same quantity shock depending on how full the tanks are.

### The curve is a price of storage, not a forecast

A futures curve lists prices today for delivery at different future dates. A common mistake is to read it as the market's forecast of future spot prices. It is better read as the **price of moving a barrel through time**.

Consider a merchant who owns crude today. She can sell it now at spot $S$, or store it and sell it forward at $F$ for delivery in six months. If $F$ exceeds $S$ by more than the cost of financing and storing the barrel, she buys spot, stores it and sells forward. That locks in a riskless profit. Competition among merchants caps $F$ at "full carry". If $F$ is below $S$, holding inventory loses money on paper, yet merchants and refiners still hold some. They do so because a barrel in the tank today has a **convenience yield**: it keeps a refinery running, it meets a customer order, and it avoids the cost of a stock-out. The convenience yield is high when inventory is scarce and close to zero when inventory is abundant.

This is the **theory of storage** of Kaldor (1939) and Working (1949). Brennan (1958) developed it into a supply curve of storage. Its central prediction is that the **slope of the futures curve is a function of inventory**:

* **Contango** (deferred contracts above the front) goes with high inventory. The marginal holder is paid to store.
* **Backwardation** (deferred contracts below the front) goes with low inventory. The market pays a premium for barrels now.

The expected future spot price enters only through a risk premium that the theory of storage does not pin down. Gorton, Hayashi and Rouwenhorst (2013) find, for 31 commodities from 1969 to 2006, that the futures basis reflects the state of inventories, that the convenience yield falls nonlinearly as inventories rise, and that futures risk premia are higher when inventories are low [FACT; ch16-S08, VERIFIED-SECONDARY].

### Why a rolling futures position is not a claim on spot

A futures contract expires. To keep exposure, an investor sells the expiring contract and buys the next one, which is called **rolling**. In contango, the investor repeatedly sells the cheaper expiring contract and buys a dearer one. If spot stays flat, each new contract drifts down toward spot as it approaches expiry, and the investor loses that drift. In backwardation the opposite happens. The total return on a rolling position is therefore spot change + roll + interest on collateral. The roll component can dominate for years. Example 16.3 makes the decomposition exact.

This is why Item 3's chart answers the wrong question. The partner showed that spot rose. The strategy earns spot **plus roll**, and the roll term depends on the curve shape over the holding period, which in turn depends on inventory.

### Seasonality is storage with a calendar

Natural gas is consumed for heating in winter and produced roughly evenly through the year. Storage fills from spring to autumn and empties in winter. The futures strip therefore shows a **seasonal premium**: winter contracts trade above summer contracts. The spread pays for moving gas from summer to winter, and it is bounded by the cost of doing so. Corn has the opposite pattern within a crop year: stocks peak at harvest and run down until the next one. That creates "old crop / new crop" spreads, where the last contract before harvest can trade above the first contract after it. In both cases a seasonal spread wider than the cost of storage invites storage, and storage competition compresses it.

### Commodities and real estate meet in two places

For a CRE investor, commodity prices matter through two channels.

1. **Demand.** In energy-producing regions such as the Permian Basin, oil prices drive drilling, drilling drives employment and business travel, and those drive hotel room-nights and apartment absorption. The transmission is lagged, it is leveraged by hotel operating leverage, and it is amplified by supply that was started during the boom.
2. **Cost.** Copper, steel and lumber are inputs to construction. Their prices move replacement cost, and replacement cost sets the ceiling above which new supply enters (Chapter 8). A rise in input prices protects existing owners from new competition and squeezes developers who have not fixed their costs.

---

## 16.3 Technical definitions

| Term | Definition |
|---|---|
| Spot price $S_t$ | Price for prompt delivery at a specified location and quality. For WTI the delivery point of the NYMEX contract is Cushing, Oklahoma |
| Futures price $F_t(T)$ | Price agreed at $t$ for delivery at $T$, marked to market daily |
| Front month, nearby | The contract closest to expiry |
| Contango | $F(T_2) > F(T_1)$ for $T_2 > T_1$; deferred contracts above nearby |
| Backwardation | $F(T_2) < F(T_1)$; deferred contracts below nearby |
| Basis | $S - F$ (in this chapter); positive in backwardation |
| Financing rate $r$ | Continuously compounded rate at which the inventory holder funds the purchase |
| Storage cost $u$ or $U_T$ | Cost of holding a unit, as a continuous yield $u$ or a dollar amount $U_T$ paid at $T$ |
| Convenience yield $y$ | The implicit yield, per unit of time, of holding physical inventory rather than a forward claim |
| Full carry | $F^* = S e^{(r+u)T}$ (or $S e^{rT} + U_T$); the cash-and-carry upper bound |
| Cash-and-carry | Buy spot, store, sell futures. Enforces $F \le F^*$ |
| Reverse cash-and-carry | Sell inventory, buy futures. Possible only for holders of inventory, so it does not enforce a lower bound |
| Roll | Closing an expiring contract and opening a later one |
| Roll component | $(S_t - F_t)/F_t$ per period for a position that buys the nearby at $F_t$; positive in backwardation |
| Collateral component | Interest earned on the cash backing a fully collateralized futures position |
| Calendar spread | Long one contract month, short another. Its P&L depends only on the change in curve slope |
| Lease rate | For gold and silver, the rate at which metal can be lent. It plays the role of the convenience yield |
| Contract multiplier | Units per contract; dollar P&L per contract = price change × multiplier × (dollars per quotation unit) |

### Contract specifications used in this chapter

[FACT; CME Group contract specifications and rulebook chapters; ch16-S01 to S06, VERIFIED-SECONDARY via search excerpts on 2026-10-19. Confirm against the live CME pages before trading.]

| Code | Contract | Contract unit (multiplier) | Price quotation | \$ P&L per 1.00 quote move |
|---|---|---|---|---|
| CL | NYMEX Light Sweet Crude Oil (WTI), physically delivered at Cushing, OK | 1,000 barrels | \$ per barrel | \$1,000 |
| NG | NYMEX Henry Hub Natural Gas | 10,000 MMBtu | \$ per MMBtu | \$10,000 |
| GC | COMEX Gold | 100 troy ounces | \$ per troy ounce | \$100 |
| SI | COMEX Silver | 5,000 troy ounces | \$ per troy ounce | \$5,000 |
| HG | COMEX Copper | 25,000 pounds | \$ per pound | \$25,000 |
| ZC | CBOT Corn | 5,000 bushels | **cents** per bushel | \$50 per 1 cent |

The CME corn quotation unit (cents per bushel, with a quarter-cent tick) is the long-standing exchange convention, but in this environment it was confirmed only indirectly (a source giving the tick as one-quarter of a cent) *(verification pending against the CME ZC contract-spec page)*. The other five rows were confirmed by search excerpts of CME pages, rulebook chapters, or broker summaries of them.

Two traps carry most of the cost. First, **corn is quoted in cents**. A move from 452'2 to 468'4 is 16.25 cents, worth \$812.50 per contract, not \$81,250. Grain quotes also use eighths in some displays: 452'2 means 452 and 2/8 cents. Second, **natural gas and copper have large multipliers relative to their prices**. A 10-cent move in Henry Hub is \$1,000 per contract. A 10-cent move in copper is \$2,500.

CME also lists steel (hot-rolled coil) and lumber futures. Their contract specifications are not used in this chapter *(verification pending)*. Example 16.7 hedges only the copper component of construction cost for that reason.

---

## 16.4 Equations and derivations

### 16.4.1 Cost of carry with storage and convenience yield

**Cash-and-carry (upper bound).** At $t = 0$ borrow $S$ at continuous rate $r$, buy one unit, pay storage, and sell one futures contract for delivery at $T$ at price $F$. At $T$ deliver the unit, receive $F$, repay $S e^{rT}$ and pay storage $U_T$. The position has no risk and no net investment, so its payoff must be non-positive:

$$F - S e^{rT} - U_T \le 0 \quad\Rightarrow\quad F \le F^* = S e^{rT} + U_T.$$

With storage as a proportional yield $u$, $F^* = S e^{(r+u)T}$. Converting a dollar storage cost to a yield:

$$S e^{(r+u)T} = S e^{rT} + U_T \;\Rightarrow\; u = \frac{1}{T}\ln\!\Big(1 + \frac{U_T}{S e^{rT}}\Big).$$

**Reverse cash-and-carry (no enforceable lower bound).** To push $F$ up toward $F^*$ from below, someone must sell spot and buy futures. Only an existing inventory holder can do that. A holder who needs the barrel to run a refinery will not lend it out for the financing saving alone. So $F$ can sit far below $F^*$. We **define** the convenience yield $y$ by

$$F = S e^{(r + u - y)T} \quad\Longleftrightarrow\quad y = r + u - \frac{1}{T}\ln\frac{F}{S} = \frac{1}{T}\ln\frac{F^*}{F}.$$

The second form says that $y$ is the annualized log shortfall of the quoted futures price below full carry. It is an **implied** quantity, like an implied volatility, and it absorbs everything the model omits: risk premia, delivery-location frictions and credit costs.

### 16.4.2 Curve slope and the theory of storage

The annualized log slope between two contract months is

$$\text{slope} = \frac{\ln(F_{far}/F_{near})}{\Delta T} = r + u - y.$$

The theory of storage makes $y$ and $u$ functions of inventory. We use two [HYPOTHESIS] teaching forms, implemented in `x_commodities.py`:

$$y(x) = \frac{\theta}{x}, \qquad x = \frac{\text{inventory}}{\text{normal inventory}};$$

$$u(f) = u_0 + \kappa\,\frac{f}{1-f}, \qquad f = \text{fraction of working storage capacity filled}.$$

The first captures the convex fall of convenience yield as stocks rise, which Gorton, Hayashi and Rouwenhorst (2013) document empirically. The second captures the explosion of marginal storage cost as tanks approach full. Together they produce the "Working curve" in Figure 16.1 (described in words): the slope is negative (backwardation) at low inventory, rises through mild contango at normal inventory, flattens at full carry, and then steepens again near tank-tops because storage itself becomes scarce. The two tails behave differently. Backwardation is **unbounded**: nothing forces $y$ down when stocks run out. Contango is **bounded by full carry**, but full carry itself rises without limit when storage runs out. The April 2020 episode (§16.8.4) sits at the right-hand tail.

### 16.4.3 Roll-yield decomposition

Hold a fully collateralized long position in the contract that expires at the end of each period. At the start of period $t$, buy the nearby at $F_t$ and place $F_t$ in bills earning $i_t$ for the period. At expiry the contract converges to spot $S_{t+1}$. Wealth per unit of notional at period end is $F_t(1 + i_t) + (S_{t+1} - F_t)$, so the period return is

$$R_t = i_t + \frac{S_{t+1} - F_t}{F_t} = \underbrace{i_t}_{\text{collateral}} + \underbrace{\frac{S_{t+1} - S_t}{F_t}}_{\text{spot}} + \underbrace{\frac{S_t - F_t}{F_t}}_{\text{roll}}.$$

The decomposition is **exact** within each period: add and subtract $S_t$. The roll term is positive in backwardation ($F_t < S_t$) and negative in contango. Across $n$ periods, returns compound:

$$1 + R_{0,n} = \prod_{t=0}^{n-1}(1 + R_t) \neq 1 + \sum_t R_t.$$

The sums of the components do not add to the compounded total. The difference is an interaction term, which matters only over long horizons or in volatile markets. In logs, the excess return (before collateral) splits exactly across periods:

$$\sum_{t}\ln\frac{S_{t+1}}{F_t} = \underbrace{\ln\frac{S_n}{S_0}}_{\text{cumulative spot}} + \underbrace{\sum_t \ln\frac{S_t}{F_t}}_{\text{cumulative roll}}.$$

The spot term depends only on the start and end prices. The roll term depends on the **path of curve shape**, so it can be negative for years while spot ends where it started. Index providers define "roll yield" in several slightly different ways. This chapter uses the definition above and states it whenever a number is quoted.

### 16.4.4 Seasonal storage: intrinsic value

A storage operator buys gas in the injection season at $F_{buy}$, injects it with fuel loss $\phi$ (a fraction of injected volume), and sells it in winter at $F_{sell}$. Per **delivered** MMBtu:

$$\text{Margin} = F_{sell} - \frac{F_{buy}}{1-\phi} - c_{inj} - c_{wd} - R_{cap} - \frac{F_{buy}}{1-\phi}\, r\,\tau.$$

Here $c_{inj}$ and $c_{wd}$ are variable injection and withdrawal costs, $R_{cap}$ is capacity rent, and $\tau$ is the holding period in years (simple interest). This is the **intrinsic** value: the margin locked in by trading the two futures today. Storage also has **extrinsic** (option) value, because the operator can re-optimize injection and withdrawal as spreads move. Extrinsic value is not computed here.

### 16.4.5 Oil-to-RevPAR transmission

Write each link as a simple proportional elasticity. All elasticities are [HYPOTHESIS] and must be estimated for any real market.

$$\%\Delta\text{rigs} = \varepsilon_{rig}\,\%\Delta\text{oil}; \qquad \%\Delta D_{energy} = \varepsilon_{D}\,\%\Delta\text{rigs}; \qquad \%\Delta D = s\,\%\Delta D_{energy};$$

$$Occ_1 = Occ_0 \frac{1 + \%\Delta D}{1 + \%\Delta\text{supply}}; \qquad ADR_1 = ADR_0\,\big(1 + \eta\,(Occ_1/Occ_0 - 1)\big).$$

Here $s$ is the energy-linked share of room-nights, and $\eta$ is the elasticity of ADR to the proportional occupancy change. Then $RevPAR = Occ \times ADR$, and NOI follows from the operating statement (`hotel.operating_statement`, Chapter 11). Two caveats belong in every memo:

* **Lags.** Rig counts typically respond to oil prices with a delay of several months [HYPOTHESIS for this book's purposes; the lag length varies by episode and should be estimated]. Room-night demand responds to rigs and completion crews with a further delay.
* **Asymmetry.** At 80% occupancy a hotel cannot capture much more demand when oil rises. It can lose a lot when oil falls. NOI is therefore **concave** in oil near the top of the cycle.

### 16.4.6 A linear oil hedge of NOI

If NOI falls by $\Delta NOI$ for an oil move of $\Delta P$ dollars per barrel, the NOI's dollar sensitivity is $\beta = \Delta NOI/\Delta P$ (\$ per \$/bbl per year). The number of CL contracts that offsets one year of that sensitivity is

$$N = \frac{\beta}{1{,}000}.$$

The hedge is a short futures position at the **deferred** futures price, not at spot. In backwardation that price is lower than spot, so the hedge locks in less than today's price. Basis risk (Midland demand versus Cushing crude), timing risk (lags), and the concavity above make a linear futures hedge imperfect. Example 16.6 quantifies this.

### 16.4.7 Replacement cost and commodity inputs

Let hard cost $H$ have commodity-sensitive shares $w_i$ (lumber, steel, copper) with proportional price changes $\Delta p_i$. With full pass-through,

$$\Delta H = H\sum_i w_i\,\Delta p_i; \qquad RC = \text{Land} + H(1 + \text{soft \%}).$$

Soft costs are often budgeted as a percentage of hard cost, so a hard-cost shock carries soft costs with it. A hedge in futures covers only the component with a listed contract, and only if the developer, not the general contractor, bears the price risk.

---

## 16.5 Worked examples

All seven examples are reproduced in `tests/test_ch16_examples.py`. All prices and inputs in this section are [HYPOTHESIS] unless a source is cited.

### Example 16.1 — One book, six multipliers

**Given.** A commodity book holds the following positions, all opened and closed within the same week (prices hypothetical):

| Contract | Side | Contracts | Entry | Exit |
|---|---|---|---|---|
| CL (WTI) | Long | 3 | \$72.40/bbl | \$68.15/bbl |
| NG (Henry Hub) | Short | 2 | \$3.250/MMBtu | \$3.610/MMBtu |
| GC (gold) | Long | 4 | \$2,400.0/oz | \$2,452.3/oz |
| SI (silver) | Short | 1 | \$30.10/oz | \$29.45/oz |
| HG (copper) | Long | 2 | \$4.250/lb | \$4.115/lb |
| ZC (corn) | Long | 5 | 452'2 (452.25¢/bu) | 468'4 (468.50¢/bu) |

**Find.** P&L per line, total P&L, and entry notional.

**Solution.** P&L = side × (exit − entry) × multiplier × (\$ per quote unit) × contracts.

| Contract | Calculation | P&L | Entry notional |
|---|---|---|---|
| CL | $+1 \times (68.15 - 72.40) \times 1{,}000 \times 3$ | −\$12,750 | $72.40 \times 1{,}000 \times 3 = \$217{,}200$ |
| NG | $-1 \times (3.610 - 3.250) \times 10{,}000 \times 2$ | −\$7,200 | \$65,000 |
| GC | $+1 \times (2{,}452.3 - 2{,}400.0) \times 100 \times 4$ | +\$20,920 | \$960,000 |
| SI | $-1 \times (29.45 - 30.10) \times 5{,}000 \times 1$ | +\$3,250 | \$150,500 |
| HG | $+1 \times (4.115 - 4.250) \times 25{,}000 \times 2$ | −\$6,750 | \$212,500 |
| ZC | $+1 \times (468.50 - 452.25) \times 0.01 \times 5{,}000 \times 5$ | +\$4,062.50 | \$113,062.50 |
| **Total** | | **+\$1,532.50** | **\$1,718,262.50** |

**Check.** Corn: 16.25 cents × \$50 per cent per contract × 5 = \$4,062.50. If the corn move were read in dollars, the line would show \$406,250, a factor of 100 too large, and it would turn a \$1.5 thousand week into a fictitious \$0.4 million gain.

**Decision consequence.** Gold is 56% of the gross notional but the smallest number of contracts per dollar of price. Natural gas is 4% of gross notional, yet a 36-cent move cost \$7,200. Risk limits written in "contracts" are meaningless across commodities. Limits must be written in dollar notional, or better in dollar volatility (notional × volatility), and the quotation unit must be stored with every price in the risk system.

### Example 16.2 — Cost of carry, the full-carry bound, and the implied convenience yield

**Given.** WTI spot at Cushing \$70.00/bbl. Six-month financing rate $r = 4.5\%$ (continuous). Storage \$0.40/bbl/month, paid at delivery, so $U_T = \$2.40$ for $T = 0.5$. Three alternative quotes for the six-month futures: (a) \$68.50; (b) \$73.50; (c) \$75.00.

**Find.** Full carry $F^*$, the storage yield $u$, the implied convenience yield in each case, and any arbitrage.

**Solution.**

$S e^{rT} = 70.00 \times e^{0.0225} = 70.00 \times 1.022755 = \$71.5929$.

$F^* = 71.5929 + 2.40 = \$73.9929$.

$u = \frac{1}{0.5}\ln(1 + 2.40/71.5929) = 2 \ln(1.033523) = 6.595\%$.

Implied convenience yield $y = \frac{1}{T}\ln(F^*/F)$:

| Quote | $\ln(F/S)/T$ (curve slope vs spot) | $y$ | Curve shape |
|---|---|---|---|
| (a) \$68.50 | −4.33% | $2\ln(73.9929/68.50) = 15.43\%$ | Backwardation |
| (b) \$73.50 | +9.76% | $2\ln(73.9929/73.50) = 1.34\%$ | Contango, near full carry |
| (c) \$75.00 | +13.80% | $2\ln(73.9929/75.00) = -2.70\%$ | Contango above full carry |

Case (c) violates the bound. Buy spot at \$70.00 with borrowed money, store, and sell the futures at \$75.00. At $T$ deliver, receive \$75.00, repay \$71.5929 and pay \$2.40 storage. The profit is $75.00 - 73.9929 = \$1.0071$/bbl, or \$1,007 per contract.

**Check.** Identity: $y = r + u - \ln(F/S)/T$. For (a), $0.045 + 0.06595 + 0.04332 = 0.15427$. ✓

**Decision consequence.** A 15% convenience yield is not a forecast that oil will fall 4% in six months. It says that holders of crude value prompt barrels highly, which is the signature of tight inventory. Case (c) is "arbitrage" only for someone with storage space at \$0.40/bbl/month and financing at 4.5%. In a glut, the marginal tank costs much more than the average tank, so a curve can sit above *your* full carry and still be in equilibrium for the marginal storer (Example 16.4). Before calling a curve mispriced, find out whose storage cost defines the bound.

### Example 16.3 — Roll yield: losing money while spot is unchanged

**Given.** A fully collateralized long position rolls the one-month WTI contract each month for four months. Bills earn 0.40% per month. Spot path and the nearby futures price at the start of each month:

| Month $t$ | $S_t$ | $F_t$ (nearby, contango case) | $F_t$ (backwardation case) |
|---|---|---|---|
| 0 | 70.00 | 71.40 | 68.60 |
| 1 | 71.00 | 72.20 | 69.80 |
| 2 | 69.50 | 71.00 | 68.10 |
| 3 | 70.50 | 71.60 | 69.40 |
| 4 | 70.00 | — | — |

**Find.** The per-month spot, roll and collateral components, and the four-month compounded total return in each case.

**Solution (contango).** Month 0: spot $= (71.00 - 70.00)/71.40 = +1.4006\%$; roll $= (70.00 - 71.40)/71.40 = -1.9608\%$; collateral $+0.40\%$; total $-0.1602\%$.

| Month | Spot | Roll | Collateral | Total |
|---|---|---|---|---|
| 0 | +1.4006% | −1.9608% | +0.40% | −0.1602% |
| 1 | −2.0776% | −1.6620% | +0.40% | −3.3396% |
| 2 | +1.4085% | −2.1127% | +0.40% | −0.3042% |
| 3 | −0.6983% | −1.5363% | +0.40% | −1.8346% |
| Sum | +0.0331% | −7.2718% | +1.60% | |

Compounded total: $\prod(1 + R_t) - 1 = -5.553\%$. Compounded excess (no collateral): $-7.077\%$. Spot change: 0.00%.

Log check: cumulative spot $\ln(70/70) = 0$; cumulative roll $\sum\ln(S_t/F_t) = -7.340\%$; log excess $= -7.340\%$, and $e^{-0.07340} - 1 = -7.077\%$, which matches the compounded excess. ✓

**Solution (backwardation).** Same spot path, futures below spot:

| Month | Spot | Roll | Collateral | Total |
|---|---|---|---|---|
| 0 | +1.4577% | +2.0408% | +0.40% | +3.8985% |
| 1 | −2.1490% | +1.7192% | +0.40% | −0.0298% |
| 2 | +1.4684% | +2.0558% | +0.40% | +3.9242% |
| 3 | −0.7205% | +1.5850% | +0.40% | +1.2646% |

Compounded total $+9.309\%$; compounded excess $+7.608\%$; cumulative log roll $+7.332\%$.

**Decision consequence.** The same spot path gives −5.6% in contango and +9.3% in backwardation over four months. The difference is entirely the curve. For Item 3, the partner's chart of spot prices is not evidence about the strategy's return. The right question is: *in which inventory regime will we hold it?* In a glut, a long rolling position pays the storers. Its expected return is spot drift + expected roll + bill rate, and expected roll is negative when contango is persistent. If the goal is to hedge the fund's exposure to inflation in construction or operating costs, Example 16.7 shows a more targeted hedge.

### Example 16.4 — Inventory and curve slope: a calendar-spread trade on an inventory surprise

**Given.** Teaching parameters for the Working curve [HYPOTHESIS]: $r = 4.5\%$, $u_0 = 3\%$, $\kappa = 0.005$, $\theta = 0.06$. Front-month WTI is \$70.00. The one-month calendar spread (second month minus front) is approximated as $F_{near}(e^{\text{slope}/12} - 1)$.

(a) Compute the slope and the one-month spread at four inventory states: Tight ($x = 0.60$, $f = 0.35$); Normal ($x = 1.00$, $f = 0.55$); Glut ($x = 1.50$, $f = 0.80$); Tank-tops ($x = 1.90$, $f = 0.97$).

(b) A desk holds 10 one-month spreads: short front, long second month (it profits if contango widens). A weekly inventory report surprises upward: $x$ moves from 0.95 to 1.10 and $f$ from 0.55 to 0.62. Estimate the spread P&L.

**Solution (a).** Slope $= r + u(f) - y(x)$:

| State | $y = \theta/x$ | $u = u_0 + \kappa f/(1-f)$ | Slope | 1-month spread |
|---|---|---|---|---|
| Tight | 10.00% | 3.269% | −2.231% | −\$0.130 |
| Normal | 6.00% | 3.611% | +2.111% | +\$0.123 |
| Glut | 4.00% | 5.000% | +5.500% | +\$0.322 |
| Tank-tops | 3.158% | 19.167% | +20.509% | +\$1.207 |

**Solution (b).** Before: $y = 0.06/0.95 = 6.316\%$, $u = 3.611\%$, slope $= 1.795\%$, spread $= 70(e^{0.01795/12} - 1) = \$0.1048$. After: $y = 0.06/1.10 = 5.455\%$, $u = 0.03 + 0.005 \times 0.62/0.38 = 3.816\%$, slope $= 2.861\%$, spread $= \$0.1671$. Change $= +\$0.0623$/bbl. P&L $= 0.0623 \times 1{,}000 \times 10 = +\$623$.

**Check.** At tank-tops, the slope (20.5%) exceeds normal full carry ($r + u_0 = 7.5\%$) by 13 percentage points. That is not an arbitrage. It is the price of the scarce marginal tank.

**Decision consequence.** The calendar spread isolates the inventory view from the price-level view, and its P&L is small per contract. Ten spreads earn \$623 on a surprise that moved inventory 15% relative to normal. Spread trading requires size, and size in the front month brings delivery and liquidity risk near expiry. The model's convexity matters more than its point estimates. Near normal inventory the slope barely responds. Near tank-tops a small additional inflow moves the spread by dollars, not cents. A desk short contango spreads (long front, short deferred) into a filling storage hub is short this convexity.

### Example 16.5 — Seasonal storage: summer-winter natural gas

**Given.** A storage operator controls 2,000,000 MMBtu of deliverable working gas capacity. July Henry Hub futures \$2.90/MMBtu; January futures \$3.95. Fuel loss on injection 2%. Injection and withdrawal costs \$0.04 each per MMBtu. Capacity rent \$0.30/MMBtu (the operator's opportunity cost of leasing the space to a third party). Financing 5% simple for six months.

**Find.** Intrinsic margin per delivered MMBtu, total intrinsic value, and the futures hedge in contracts. Then repeat with January at \$3.55.

**Solution.**

Purchase cost per delivered unit: $2.90/0.98 = \$2.9592$.

Financing: $2.9592 \times 0.05 \times 0.5 = \$0.0740$.

Margin $= 3.95 - 2.9592 - 0.04 - 0.04 - 0.30 - 0.0740 = \$0.5368$/MMBtu.

Total: $0.5368 \times 2{,}000{,}000 = \$1{,}073{,}673$.

Hedge: buy July gas for $2{,}000{,}000/0.98 = 2{,}040{,}816$ MMBtu, which is 204.08 contracts, so **204 long July** NG contracts. Sell 2,000,000 MMBtu of January, which is **200 short January** contracts.

With January at \$3.55 the raw spread is \$0.65, and the margin falls to \$0.1368/MMBtu, or \$273,673 in total.

**Check.** The raw spread of \$1.05 is not the margin. Fuel, variable costs, rent and financing absorb \$0.513 of it, or 49%.

**Decision consequence.** The hedge is asymmetric in contracts (204 versus 200) because of fuel loss. A desk that hedges 200-for-200 is left with a small open long. When the spread compresses by 40 cents, intrinsic value falls by 75%, because the costs are fixed. Seasonal spreads are the market's price for storage capacity. When new storage is built or a mild winter is forecast, the spread compresses toward the cost of the marginal capacity.

### Example 16.6 — Oil to RevPAR to value: the Midland hotel (Item 1)

**Given.** The 120-room hotel from §16.1. Year-0 occupancy 80%, ADR \$160. Operating assumptions (USALI-style, Chapter 11): other revenue 8% of rooms revenue; rooms expense \$32 per occupied room; other departmental expense ratio 75%; undistributed expenses \$1,100,000 fixed plus 6% of total revenue; management fee 3% of total revenue; franchise fees 11% of rooms revenue; property tax \$260,000; insurance \$140,000; FF&E reserve 4% of total revenue.

Transmission elasticities [HYPOTHESIS; labeled teaching values, not estimates]: $\varepsilon_{rig} = 1.0$, $\varepsilon_D = 0.8$, energy-linked share $s = 0.50$, $\eta = 0.5$. New supply: submarket room supply rises 4% as a hotel started during the boom opens. Oil shock: −45%, from \$80 to \$44. Cap rate before the shock 9.5%; after 10.5%. Loan at 65% LTV of the pre-shock value, 7.0%, 25-year amortization.

**Find.** RevPAR, NOI, DSCR and value after the shock; the oil sensitivity of NOI; and a one-year hedge in CL contracts and its outcome.

**Solution.**

*Transmission.*

* Rigs: $1.0 \times (-45\%) = -45\%$.
* Energy demand: $0.8 \times (-45\%) = -36\%$.
* Total demand: $0.50 \times (-36\%) = -18\%$.
* Occupancy: $0.80 \times 0.82/1.04 = 0.6308$, a change of −21.15%.
* ADR: $160 \times (1 + 0.5 \times (-0.2115)) = \$143.08$.
* RevPAR: from \$128.00 to $0.6308 \times 143.08 = \$90.25$, a change of **−29.5%**.

*Operating statement* (`hotel.operating_statement`):

| Line | Before | After |
|---|---|---|
| Rooms revenue | \$5,606,400 | \$3,952,885 |
| Total revenue | \$6,054,912 | \$4,269,116 |
| GOP | \$3,133,953 | \$1,791,710 |
| EBITDA | \$1,935,602 | \$828,819 |
| FF&E reserve (4%) | \$242,196 | \$170,765 |
| **NOI** | **\$1,693,405** | **\$658,054** |
| NOI margin | 28.0% | 15.4% |

NOI falls 61.1% on a 29.5% revenue decline. The marginal flow-through is $\Delta NOI/\Delta\text{Revenue} = 1{,}035{,}351/1{,}785{,}796 = 58.0\%$.

*Value and debt.* Value before $= 1{,}693{,}405/0.095 = \$17.83$ million. After $= 658{,}054/0.105 = \$6.27$ million, a fall of 64.8%. Loan $= 0.65 \times 17.83 = \$11.59$ million; annual debt service at 7.0%/25 years $= \$982{,}688$. DSCR falls from **1.72x** to **0.67x**. The loan exceeds the post-shock value.

*Oil sensitivity and hedge.* $\beta = 1{,}035{,}351/(80 - 44) = \$28{,}760$ of annual NOI per \$1/bbl. One year of NOI sensitivity requires $N = 28{,}760/1{,}000 = 28.8$, so **29 short CL contracts** in the 12-month contract.

The 12-month futures trade at \$74, not \$80 (backwardation). If oil falls to \$44 and the hedge contract expires at that price, the hedge earns $29 \times (74 - 44) \times 1{,}000 = \$870{,}000$. That covers 84% of the \$1,035,351 first-year NOI loss. It covers none of the \$11.6 million value loss, which reflects many years of lower NOI and a higher cap rate. If instead oil rises to \$100, the hedge loses $29 \times (100 - 74) \times 1{,}000 = \$754{,}000$, paid in daily variation margin, while NOI gains little because the hotel is already at 80% occupancy.

**Check.** Revenue change from the statement: $4{,}269{,}116/6{,}054{,}912 - 1 = -29.49\%$, matching the RevPAR change because other revenue is proportional to rooms revenue. ✓

**Decision consequence.** The seller's 9.5% cap rate prices an asset whose NOI moves about 2.1 times as much as revenue (−61.1% against −29.5%), and half of whose room-nights are energy-linked. Three conclusions follow. (1) Underwrite through-cycle NOI, not the T-12 at \$80 oil, and require DSCR to survive the oil-down case. At 65% LTV this hotel cannot cover debt service (DSCR 0.67x) in the first year of a −45% oil shock. (2) A linear futures hedge is the wrong shape. NOI is concave in oil: it has little upside and a large downside. The matching hedge is a **long put** (or put spread) on 12-month WTI, whose cost is known in advance and which creates no margin calls. Chapter 18 prices such options. (3) The hedge covers one year of the income loss. It does not cover the capital loss. The more effective protection is lower leverage and a purchase price that already reflects a mid-cycle oil price. The hedge is a supplement to price discipline, not a substitute for it.

### Example 16.7 — Commodity inputs, replacement cost, and a copper hedge (Item 2)

**Given.** The 150-unit apartment project. Hard cost \$27.0 million. Land \$2.5 million. Soft costs 18% of hard cost. Commodity-sensitive shares of hard cost [HYPOTHESIS]: lumber 8%, steel 5%, copper (wire, plumbing, HVAC) 2%. A cost shock with full pass-through: lumber +60%, steel +25%, copper +30%. Copper at \$4.25/lb when the budget was set.

**Find.** The change in hard cost, replacement cost before and after (total and per unit), and a copper hedge in HG contracts, with its outcome.

**Solution.**

$\Delta H = 27{,}000{,}000 \times (0.08 \times 0.60 + 0.05 \times 0.25 + 0.02 \times 0.30) = 27{,}000{,}000 \times 0.0665 = \$1{,}795{,}500$.

$RC_0 = 2{,}500{,}000 + 27{,}000{,}000 \times 1.18 = \$34{,}360{,}000$, or \$229,067 per unit.

$RC_1 = 2{,}500{,}000 + 28{,}795{,}500 \times 1.18 = \$36{,}478{,}690$, or \$243,191 per unit. That is an increase of **6.17%**.

Copper exposure: $0.02 \times 27{,}000{,}000 = \$540{,}000$, which is $540{,}000/4.25 = 127{,}059$ lb, or 5.08 contracts. Use **5 long HG** contracts.

If copper rises 30%: hedge gain $= 5 \times 25{,}000 \times 4.25 \times 0.30 = \$159{,}375$, against a cost increase of $540{,}000 \times 0.30 = \$162{,}000$.

**Check.** Of the \$1.80 million hard-cost increase, copper is only \$162,000 (9%). Lumber, at \$1.296 million, is 72% of it.

**Decision consequence.** Two decisions follow. For the **developer**, the hedgeable component (copper) is a small part of the commodity risk. Most of the risk sits in lumber and steel, and in labor, which has no futures market. The main protection is contractual: a guaranteed maximum price (GMP) contract with a creditworthy general contractor, or early buyout of the lumber package. A copper hedge layered on top of a GMP contract that already passes copper risk to the contractor is a **speculation**, not a hedge (Chapter 1, §1.7). For an **owner of existing apartments** in the same market, a 6.2% rise in replacement cost raises the rent that new supply needs to pencil. That delays competing starts. Rising input prices are a modest tailwind for existing assets bought below replacement cost, provided demand holds. In Midland, demand also depends on oil, so the two channels can move in opposite directions.

---

## 16.6 CRE application: energy exposure in Texas and Permian real estate

### 16.6.1 Mapping the exposure

The Permian Basin economy is unusually concentrated. In an energy metro, oil prices affect real estate through several channels with different lags:

| Channel | Lag (qualitative) | Most exposed property type |
|---|---|---|
| Rig and completion activity → crew travel | Months | Limited- and select-service hotels; extended stay |
| Energy employment → household formation | Months to a year | Multifamily, especially Class B/C |
| Energy employment → office demand | One to several years (lease terms) | Office (Midland, Houston) |
| Royalty and wage income → retail sales | Months | Neighborhood retail |
| Municipal sales-tax revenue → public services, property tax | One to two years | All, via tax rates and services |
| Commodity inputs → replacement cost | Months | Development, all types |

The hotel's exposure is the most direct and the most levered. Its rates reprice nightly, and its cost structure is mostly fixed. Multifamily reprices over the lease term, so its revenue reacts more slowly but just as surely.

### 16.6.2 Multifamily transmission: a short calculation

Hypothetical inputs [HYPOTHESIS]: energy jobs are 30% of metro employment; an oil shock cuts energy employment 25%; each lost energy job costs 0.5 non-energy jobs (a local multiplier); renter demand moves one-for-one with employment; new supply adds 3%; starting occupancy 95%; effective rent responds with an elasticity of 0.5 to the proportional occupancy change.

* Employment change $= -0.25 \times 0.30 \times (1 + 0.5) = -11.25\%$.
* Occupancy $= 0.95 \times 0.8875/1.03 = 81.86\%$, a change of −13.83%.
* Effective rent change $= 0.5 \times (-13.83\%) = -6.92\%$.
* Revenue run-rate change $= (0.8186 \times 0.9308)/0.95 - 1 = -19.8\%$ once leases have repriced.

Compare the hotel: RevPAR −29.5% within months. The multifamily revenue decline is smaller and arrives over a lease cycle. That buys time to cut expenses and talk to lenders, but the decline is not small. Concession-heavy lease-up in a new building can make it worse, because the new supply competes directly on price.

### 16.6.3 The "diversified demand" claim

Item 1's memorandum says demand is diversified. Test the claim with segmentation data, not adjectives:

1. Obtain STR segmentation (transient, group, contract) and the property's top-20 accounts by room-nights. Classify each account as energy-linked or not.
2. Check the **contract** segment. Pipeline and midstream construction crews book large blocks for the life of a project. When the project ends, those room-nights disappear regardless of the oil price.
3. Compare the T-12 ADR with the ADR of the same hotel in the last oil downturn, if the hotel existed then.
4. Count the rooms delivered and under construction in the submarket since the last trough.

If half the room-nights are energy-linked, $s = 0.50$ in Example 16.6 is not a stress assumption. It is the base case.

### 16.6.4 Hedging at the portfolio level

A fund with several Permian assets has an aggregate oil exposure that it can estimate as the sum of the asset-level $\beta$s. That aggregate can be hedged more cheaply than each asset separately. The cost of the hedge must be judged against the alternatives, which are often better:

* **Lower leverage.** Removes default risk rather than offsetting one year of income.
* **Geographic diversification.** Pairs Permian assets with assets in markets where lower oil prices help demand, such as markets with large consumer or airline-dependent travel [INFERENCE: lower fuel costs reduce household and airline costs; the size of the effect is not estimated here].
* **Purchase-price discipline.** Underwriting at a mid-cycle oil price builds the hedge into the basis at zero premium.

---

## 16.7 When the relationship fails

1. **Location and quality basis.** The NYMEX WTI contract delivers at Cushing, Oklahoma. A Permian producer sells at Midland, and pipeline constraints can open a wide spread between the two. A hedge in CL hedges Cushing, not Midland. The same issue arises with gas: Henry Hub is in Louisiana, and regional hubs can decouple from it when pipelines are full.
2. **Storage itself becomes scarce.** The theory of storage treats storage cost as roughly constant. Near tank-tops it is not, and the curve can show contango far beyond any "normal" full carry (§16.8.4). A desk that sells contango because it exceeds historical full carry is selling the convexity of storage cost.
3. **Inventory data are incomplete or mismeasured.** Official inventories cover some locations and grades. Floating storage, pipeline fill, and inventories held by consumers are often missing. A curve can backwardate while reported inventories look ample, because the reported tanks are in the wrong place or hold the wrong grade (Drill D155).
4. **Convenience yield is not one number.** It differs by location, grade and holder. The implied $y$ is a residual, and it absorbs risk premia and frictions.
5. **Expected returns are not given by the curve.** The futures price differs from the expected spot price by a risk premium that can change sign. A backwardated curve does not predict falling spot prices, and a contango curve does not predict rising ones.
6. **Gold and silver behave as financial assets.** Above-ground stocks are huge relative to annual production, so the theory of storage has little bite. The gold curve is usually close to full financing carry less a small lease rate, and its spot price responds to real rates, the dollar and central-bank demand more than to physical flows [INFERENCE; not tested here].
7. **Agricultural crop years break continuity.** Old-crop and new-crop contracts are different commodities in economic terms. A smooth carry model across the harvest is wrong.
8. **The oil–real estate link changes with the industry.** Shale drilling productivity, the shift from rig counts to completion crews, remote work in the oilfield, and operator consolidation change the room-nights per rig. Elasticities estimated in 2014–16 may not hold today. They must be re-estimated, not assumed.
9. **Hedges create liquidity risk.** A short futures hedge pays when oil falls and requires cash margin when oil rises. Metallgesellschaft's 1993 losses on rolling energy hedges are the classic case of a hedge that was arguably sound in economic value but was funded wrongly (Chapter 1, §1.7).

---

## 16.8 Historical episode: the 2014–16 oil collapse and the Permian, with April 2020 as a coda

### 16.8.1 Date and environment

[FACT] In June 2014 WTI averaged about \$105/bbl on a monthly basis, and Brent futures peaked at \$115.06 on 19 June 2014. By December 2014 WTI had fallen to about \$59/bbl. The EIA attributed the decline to weakening global demand, robust supply from rising U.S. production, fewer supply disruptions, and OPEC's decision to maintain production (EIA, *Today in Energy* and 2014 financial review; ch16-S10, VERIFIED-SECONDARY).

[FACT] Prices kept falling into early 2016. The Canada Energy Regulator, citing EIA data, reports a daily WTI spot low of US\$26.68 per barrel in January 2016, a 13-year low. WTI averaged about \$43/bbl in 2016 and ended the year near \$53 (CER 2016 review; EIA; ch16-S11, VERIFIED-SECONDARY). Sources disagree on the date and level of the exact daily trough (January versus February 2016, and spot versus futures) *(verification pending against FRED series DCOILWTICO)*. The text uses only "below \$30 in early 2016".

### 16.8.2 What happened to Texas and the Permian

[FACT] The Federal Reserve Bank of Dallas reported in March 2016 that Texas oil and gas employment fell 19.4% in 2015, as oil prices dropped 66% and the rig count fell nearly 75% from mid-2014. It reported that growth was weaker in metros with larger energy shares (Midland, Odessa, Houston, Corpus Christi), while Austin, Dallas and San Antonio continued to grow (Dallas Fed news release, 31 March 2016; ch16-S12, VERIFIED-SECONDARY). In January 2016 the Dallas Fed expected the Permian Basin and Eagle Ford regions to see steeper job declines in 2016 (ch16-S13, VERIFIED-SECONDARY).

[FACT] A Moody's analysis reported in *The Bond Buyer* estimated that the Midland–Odessa area lost about 14,500 jobs in 2015. Moody's downgraded the City of Midland one notch, citing its reliance on sales tax in a low-oil-price environment (ch16-S14, VERIFIED-SECONDARY; trade press reporting a rating action).

[FACT] Hotels: STR identified 39 of its 630 U.S. hotel tracts as primarily driven by oil and gas, with 20 of them accounting for most rooms and demand, including Midland/Odessa. In those 20 submarkets, demand fell 4.4% in 2015 while supply rose 4.1%. Through the first quarter of 2016 demand fell 8.8% and supply rose 3.7%. RevPAR was down 14.2% over the trailing 12 months and 18.4% in the first quarter of 2016 (STR, reported in trade press, May 2016; ch16-S15, VERIFIED-SECONDARY). La Quinta's FY2017 Form 10-K stated that RevPAR in the markets STR defines as oil tracts worsened significantly through the second half of 2015 and into 2016 (ch16-S16, VERIFIED-SECONDARY).

[FACT] Local press reported that in Odessa 14 hotels opened or began construction in 2013 and 2014 (ch16-S17, VERIFIED-SECONDARY; local press). Submarket-level Midland and Odessa STR occupancy and RevPAR for 2015–16 are not used here *(verification pending: STR subscriber data)*.

### 16.8.3 What was knowable, interpretations, and what the case establishes

**Knowable in mid-2014.** It was public that U.S. production was rising rapidly and that Permian hotel supply was growing. The EIA's own forecast in May 2014 was for WTI to average about \$92/bbl in the fourth quarter of 2014 (ch16-S10, VERIFIED-SECONDARY), so the official forecast did not anticipate the collapse. What was not knowable was OPEC's decision in late 2014 not to cut output, or the speed at which shale productivity would improve.

**Interpretations.** [INFERENCE] The hotel data fit the transmission model of §16.4.5. A demand shock of −4% to −9% met supply growth of about +4%, and RevPAR fell 14–18%: a demand-driven occupancy loss amplified by ADR cuts. One alternative reading is that much of the damage came from supply started at the peak, so the oil shock exposed overbuilding rather than causing it. A second is that the RevPAR decline was moderate compared with the oil decline, because non-energy demand and the lag structure cushioned the first year. The data above cannot separate these readings. The aggregate for 20 submarkets also hides dispersion: the most energy-dependent hotels likely fell much further than the average [INFERENCE; not documented here].

**What the case establishes.** Oil-price shocks transmit to energy-market hotel performance within quarters, and contemporaneous supply growth amplifies them. Statewide Texas data can hide sharp metro-level divergence.

**What it does not establish.** It does not give a stable elasticity of RevPAR to oil. The 2015 decline combined an oil shock, a supply wave and a lag. Nor does it show that Permian real estate is a bad investment. Assets bought at trough pricing in 2016 had a different risk profile from those bought at the 2014 peak.

### 16.8.4 Coda: 20 April 2020 — when storage runs out

[FACT] On 20 April 2020, the day before its expiration, the NYMEX WTI May 2020 contract fell from \$17.73 to settle at **−\$37.63 per barrel**, the first negative settlement in the contract's history (CFTC interim staff report and press release, November 2020; ch16-S18, VERIFIED-SECONDARY). The EIA attributed the move to low liquidity and limited available storage. It estimated Cushing working storage capacity at 76 million barrels and Cushing inventories at about 60 million barrels as of 17 April 2020, of which about 2 million were in transit. That implies tank farms about 76% full, and the EIA noted that some physically unfilled capacity may already have been leased or committed (EIA, *Today in Energy*; ch16-S19, VERIFIED-SECONDARY). The June contract settled at a positive price the same day (ch16-S20, VERIFIED-SECONDARY; level not quoted).

At the CL multiplier, a long holder of one May contract lost $(−37.63 − 17.73) \times 1{,}000 = −\$55{,}360$ on the day, which is 3.1 times the contract's notional value at the prior settlement of \$17.73 (Problem 16.9).

**Interpretations.** [INFERENCE] In the language of §16.4.2, the expiring contract sat at the extreme right of the Working curve. A long who could not take delivery at Cushing had to sell to someone with storage, and the marginal storage cost was high enough to make the barrel's value negative. CFTC Commissioner Berkovitz criticized the interim report as incomplete, and in particular said it had not analyzed whether storage scarcity or other factors caused the collapse (ch16-S18, VERIFIED-SECONDARY). The causal weight of storage, of liquidity in the final trading days, and of positions held by retail-oriented products remains disputed.

**What it establishes.** Futures prices are bounded below by zero only if storage or disposal is free. A position that cannot take delivery must exit before expiry, and its exit price depends on who holds storage.

**CRE connection.** In April 2020 hotels in energy markets faced the pandemic and an oil collapse at once. Any attempt to attribute their 2020 losses to oil alone would be confounded. That is a reminder to identify the channel before estimating it.

---

## 16.9 Decision exercise: Thursday's agenda

Use `desk/investment_memos/decision_record_template.md`. Your record must address all three items.

**Item 1 (hotel).** Using Example 16.6, state:

1. Your through-cycle NOI and the oil price it assumes. Show the cap rate you apply and the value that results.
2. The maximum price at which DSCR stays above 1.20x in the −45% oil case on a 55% LTV loan at 7.0%/25 years.
3. Whether you would hedge, with what instrument (futures, puts, or none), for how long, and at what cost. Say what the hedge does **not** cover.
4. The segmentation evidence you require before bidding, and which result would make you walk away.

**Item 2 (apartments).** State whether replacement cost after the input shock (\$243,191 per unit) is above or below the developer's projected stabilized value per unit. Say who bears commodity-price risk under the construction contract, and whether a copper hedge would be a hedge or a speculation in that structure.

**Item 3 (commodity allocation).** Answer the partner with a return decomposition. Spot, roll and collateral: which of them are you being paid for, in which inventory regime? Suggest a better-targeted alternative if the objective is protection against construction-cost inflation.

**Rubric** (detail in `problems/solutions/ch16_solutions.md`, §Decision exercise).

| Criterion | Full credit | Partial | None |
|---|---|---|---|
| Through-cycle underwriting | NOI underwritten at an explicit mid-cycle oil price; downside case computed; value range not a point | Downside computed but T-12 used for price | T-12 capitalized at seller's cap rate |
| Leverage | Loan sized to the stress DSCR; recognizes the 65% LTV default in Ex 16.6 | Recognizes the DSCR fall but keeps leverage | Ignores it |
| Hedge design | Matches hedge shape to exposure (puts for concave NOI); states basis, lag and margin risks; hedges income, not value | Proposes futures with stated limits | Calls the hedge "protection" without limits, or hedges notional rather than NOI sensitivity |
| Segmentation | Requires account-level data; flags contract/project business | Asks for STR data generally | Accepts "diversified" |
| Replacement cost | Correct RC; identifies who bears input risk; GMP logic | Correct RC only | Treats RC as a value floor |
| Commodity allocation | Decomposes into spot/roll/collateral; links roll to inventory; rejects the spot-chart evidence | Mentions roll qualitatively | Accepts the spot chart |
| Abstention | Treats "pass at the asking price" as a legitimate outcome for Item 1 | — | Assumes a deal must be done |

There is no single correct answer. A memo that passes on the hotel at \$17.8 million, offers at a through-cycle price, and declines the commodity allocation can earn full credit. So can one that buys with puts and lower leverage, if it shows the numbers.

---

## 16.10 Frequent analytical errors

1. **Reading the curve as a forecast.** Backwardation reflects scarce inventory, not a prediction that prices will fall.
2. **Assuming a rolling futures position earns spot.** It earns spot + roll + collateral. In persistent contango, the roll term can exceed the spot gain.
3. **Treating full carry as a hard ceiling.** It is a ceiling only for someone who has storage at the assumed cost. Near tank-tops the marginal cost of storage, and the ceiling, rise without limit.
4. **Treating the convenience yield as observable.** It is a residual implied by quoted prices and assumed costs. Change the storage-cost assumption and you change $y$.
5. **Wrong multiplier or quotation unit.** Corn in cents, natural gas at 10,000 MMBtu, copper at 25,000 lb. Store units with every price.
6. **Writing risk limits in contracts.** One NG contract and one GC contract are very different risks. Use dollar notional and dollar volatility.
7. **Ignoring fuel loss, rent and financing in storage spreads.** The raw seasonal spread overstates the storage margin.
8. **Capitalizing peak-cycle NOI in an energy market.** A T-12 at high oil prices is not stabilized NOI.
9. **Hedging a concave exposure with a linear instrument without saying so.** A short futures hedge on a hotel near full occupancy loses on the upside more than the hotel gains.
10. **Hedging value with an income hedge.** A one-year futures hedge offsets one year of NOI. The capital loss comes from many years of lower NOI and a higher cap rate.
11. **Assuming the hedge and the exposure share a location.** Cushing is not Midland, and Henry Hub is not your gas hub.
12. **Hedging a cost the contractor already bears.** Under a GMP contract, a developer's copper hedge is a speculation.

---

## 16.11 Connections to other chapters

* Chapter 1 (§1.7): hedges that become speculations; Metallgesellschaft's rolling hedge.
* Chapter 4: commodity prices as a cyclical and inflation driver.
* Chapter 5: energy prices in headline versus core inflation, and why central banks look through supply shocks.
* Chapter 8: replacement cost as a supply ceiling, and the Texas 1980s energy and real estate bust (§8.9).
* Chapter 11: hotel operating leverage, flow-through, and USALI statements used in Example 16.6.
* Chapter 12: distress and workouts when DSCR falls below 1.0x.
* Chapter 13: concentration risk and hedging at the portfolio level (Example 13.3, three Texas assets).
* Chapter 14: futures notional and margin for equity indices; the same mechanics apply here.
* Chapter 15: FX carry, the financial analogue of commodity carry.
* Chapter 18 (Derivatives, Volatility, and Convexity): pricing the puts proposed in Example 16.6.
* Chapter 21: margin and liquidity stress for the hedges in Example 16.6 and Problem 16.7.
* Chapter 23: the 2020 episode and the 1980s Texas energy and real estate cycle.

---

## 16.12 One-page reference sheet

**Core identity.** A futures curve is the price of storage. Slope $= r + u - y$.

| Formula | Expression |
|---|---|
| Full carry (upper bound) | $F^* = S e^{(r+u)T}$ or $S e^{rT} + U_T$ |
| Dollar storage → yield | $u = \frac1T \ln(1 + U_T/(S e^{rT}))$ |
| Implied convenience yield | $y = r + u - \frac1T\ln(F/S) = \frac1T \ln(F^*/F)$ |
| Annualized curve slope | $\ln(F_{far}/F_{near})/\Delta T$ |
| Cash-and-carry profit | $F - F^*$ per unit if $F > F^*$ |
| Rolling return (per period) | $R_t = i_t + \frac{S_{t+1}-S_t}{F_t} + \frac{S_t - F_t}{F_t}$ |
| Log split (excess) | $\sum \ln(S_{t+1}/F_t) = \ln(S_n/S_0) + \sum\ln(S_t/F_t)$ |
| Storage margin per delivered unit | $F_{sell} - \frac{F_{buy}}{1-\phi} - c_{inj} - c_{wd} - R_{cap} - \frac{F_{buy}}{1-\phi} r\tau$ |
| Oil → occupancy | $Occ_1 = Occ_0 (1 + s\,\varepsilon_D\,\varepsilon_{rig}\,\%\Delta oil)/(1 + \%\Delta supply)$ |
| NOI oil hedge (CL contracts) | $N = (\Delta NOI/\Delta P)/1{,}000$ |
| Replacement cost shock | $\Delta H = H \sum w_i \Delta p_i$; $RC = Land + H(1+\text{soft})$ |
| Futures P&L | side × Δprice × multiplier × \$/quote unit × contracts |

**Multipliers.** CL 1,000 bbl · NG 10,000 MMBtu · GC 100 oz · SI 5,000 oz · HG 25,000 lb · ZC 5,000 bu (quoted in cents: \$50 per cent).

**Curve regimes.** Low inventory → backwardation, positive roll, high convenience yield, price spikes possible. Normal → mild contango. Glut → contango near full carry, negative roll. Tank-tops → contango beyond normal carry, front-month collapse risk.

**Rules of thumb (to be tested, not trusted).** Hotel NOI in an energy market moves about twice as much as revenue in percentage terms. Multifamily revenue reacts over a lease cycle. Hedge income with options when the exposure is concave. A copper hedge covers little of construction-cost risk.

---

## References for this chapter

All sources are listed in `references/sources_ch16.md` with verification status.

* Brennan, M. J. (1958). "The Supply of Storage." *American Economic Review*, 48(1), 50–72.
* Gorton, G. B., Hayashi, F., and Rouwenhorst, K. G. (2013). "The Fundamentals of Commodity Futures Returns." *Review of Finance*, 17(1), 35–105.
* Kaldor, N. (1939). "Speculation and Economic Stability." *Review of Economic Studies*, 7, 1–27.
* Working, H. (1949). "The Theory of Price of Storage." *American Economic Review*, 39, 1254–1262.
* CME Group. Contract specifications for NYMEX Light Sweet Crude Oil, NYMEX Henry Hub Natural Gas, COMEX Gold, COMEX Silver (Rulebook ch. 112), COMEX Copper (Rulebook ch. 111), and CBOT Corn. https://www.cmegroup.com (accessed via search excerpts, 2026-10-19).
* U.S. Commodity Futures Trading Commission (2020). *Interim Staff Report: Trading in NYMEX WTI Crude Oil Futures Contract Leading up to, on, and around April 20, 2020*, and Release 8315-20; Statement of Commissioner Dan M. Berkovitz, 23 November 2020.
* U.S. Energy Information Administration. *Today in Energy* articles on the 2014 price decline and on Cushing storage in April 2020.
* Federal Reserve Bank of Dallas. News releases, 12 January 2016 and 31 March 2016.
* Canada Energy Regulator (2017). "2016 Review: Oil prices hit 13-year low in January 2016, double by end of year." Market Snapshot.
* STR, U.S. oil-and-gas submarket hotel performance (May 2016), as reported in trade press; La Quinta Holdings, Form 10-K for fiscal 2017.
* Culp, C. L., and Miller, M. H. (1995). "Metallgesellschaft and the Economics of Synthetic Storage." *Journal of Applied Corporate Finance*, 7(4), 62–76.
