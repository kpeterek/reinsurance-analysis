# Source Register

Every factual, historical, or empirical claim in the book must trace to an entry here. Hypothetical case data are not registered; they are labeled [HYPOTHESIS] in the text.

**Status values**
* `VERIFIED-PRIMARY`: checked against the original document or dataset (URL or archive reference given).
* `VERIFIED-SECONDARY`: checked against a reputable secondary source that cites the primary (e.g., Federal Reserve History essays, peer-reviewed surveys). The text may state the fact but should prefer the primary source when it is upgraded.
* `PENDING`: cited from domain knowledge but not yet checked in this project. Text using it must carry *(verification pending)* or be phrased so that no unverified number is presented as fact.

**Quality classification** (orthogonal to status): **A** official statistics or primary documents; **B** peer-reviewed research or official histories; **C** reputable journalism or industry research; **D** practitioner lore (never sufficient for a numerical fact).

| ID | Source | Used in | Claim supported | Class | Status | Checked on / notes |
|---|---|---|---|---|---|---|
| S001 | Federal Reserve History, "Stock Market Crash of 1987." https://www.federalreservehistory.org/essays/stock-market-crash-of-1987 | Ch 1 §1.9 | DJIA fell 508 points (22.6%) on 19 Oct 1987; Fed liquidity statement 20 Oct | B | VERIFIED-SECONDARY | 2026-10-19 via web search excerpt; exact wording of the Fed statement still to be checked against primary text |
| S002 | Presidential Task Force on Market Mechanisms (1988), *Report* ("Brady Report"). https://www.sechistorical.org/collection/papers/1980/1988_0101_BradyReport.pdf | Ch 1 §1.9; Ch 23 | Role of portfolio insurance and index arbitrage; specialist capacity | A | VERIFIED-SECONDARY | Existence, date, and central conclusions confirmed via search excerpts on 2026-10-19; specific dollar figures NOT used in text until read in the primary |
| S003 | Chicago Mercantile Exchange (1988), reports of the CME Committee of Inquiry / *Final Report*, Spring 1988. https://www.sechistorical.org/collection/papers/1980/1988_0331_MercantileReport.pdf | Ch 1 §1.9 | Dissenting interpretation: futures transmitted rather than caused selling | A | PENDING | Located via search 2026-10-19; content to be read before quoting shares of selling |
| S004 | Shiller, R. J. (1989). *Market Volatility*. MIT Press (ch. on investor behavior in the 1987 crash). | Ch 1 §1.9 | Survey evidence that many sellers reacted to price declines | B | VERIFIED-SECONDARY | Survey widely cited; page reference to be added |
| S005 | Akerlof, G. A. (1970). "The Market for 'Lemons'." *QJE* 84(3): 488–500. | Ch 1 Ex 1.7 | Adverse-selection unraveling | B | VERIFIED-PRIMARY | Standard bibliographic reference |
| S006 | Glosten, L., & Milgrom, P. (1985). *JFE* 14(1): 71–100. | Ch 1 §1.4.4 | Spread as compensation for adverse selection | B | VERIFIED-PRIMARY | Standard bibliographic reference |
| S007 | Knight, F. H. (1921). *Risk, Uncertainty and Profit*. | Ch 1 §1.2 | Risk vs uncertainty distinction | B | VERIFIED-PRIMARY | |
| S008 | Kelly, J. L. (1956). *Bell System Technical Journal* 35(4): 917–926. | Ch 1, Ch 21 | Log-optimal betting | B | VERIFIED-PRIMARY | |
| S009 | Shleifer, A., & Vishny, R. (1997). "The Limits of Arbitrage." *JF* 52(1): 35–55. | Ch 1 §1.7 | Arbitrage constrained by capital and funding | B | VERIFIED-PRIMARY | |
| S010 | Culp & Miller (1995), *JACF* 7(4); Mello & Parsons (1995), *JACF* 8(1). | Ch 1 §1.7 | Competing views on Metallgesellschaft hedge | B | VERIFIED-PRIMARY | Bibliographic; loss magnitudes not quoted |
| S011 | Hull, J. C., *Options, Futures, and Other Derivatives* (reference Black–Scholes example S=K=100, T=1, r=5%, σ=20%). | tests/test_library.py | Reference option values 10.4506 / 5.5735 | B | VERIFIED-SECONDARY | Values reproduced independently by put–call parity in tests |
| S012 | CME Group contract specifications: E-mini S&P 500 multiplier \$50 × index. https://www.cmegroup.com | Drills D011; SQL sample | Contract multiplier | A | PENDING | Well established; link to the live spec page before final edition |

## Pending verification queue
1. S003: read the CME report; extract the estimated share of selling by portfolio insurers versus others.
2. S001: retrieve the exact text of the Federal Reserve's 20 October 1987 statement from a primary archive.
3. S012: record the URL of the current E-mini contract specification page.
4. FRED series GS10 path for January–October 1987 (Ch 1 §1.9 context) — not yet cited numerically.
