-- Named queries. Each begins with "-- name: <id>" so scripts/tests can load them individually.

-- name: hotel_t12_kpis
-- Trailing performance for one hotel: occupancy, ADR, RevPAR, and STR-style indices.
-- Note: indices computed from period totals, not averages of monthly indices.
SELECT
    h.property_id,
    MIN(h.month) AS first_month,
    MAX(h.month) AS last_month,
    SUM(h.rooms_sold) * 1.0 / SUM(h.rooms_available)                    AS occupancy,
    SUM(h.room_revenue) / SUM(h.rooms_sold)                             AS adr,
    SUM(h.room_revenue) / SUM(h.rooms_available)                        AS revpar,
    100.0 * (SUM(h.rooms_sold) * 1.0 / SUM(h.rooms_available))
          / (SUM(h.comp_occ * h.rooms_available) / SUM(h.rooms_available)) AS mpi
FROM hotel_monthly h
WHERE h.property_id = :property_id
GROUP BY h.property_id;

-- name: implied_cap_rates
-- Implied cap rate and LTV for comparable sales, separating PIP-encumbered trades.
SELECT
    txn_id,
    close_date,
    price,
    noi_at_sale,
    noi_basis,
    noi_at_sale / price                                  AS cap_on_price,
    noi_at_sale / (price + pip_or_capex_required)        AS cap_on_all_in,
    loan_amount / price                                  AS ltv,
    CASE WHEN pip_or_capex_required > 0 THEN 1 ELSE 0 END AS pip_encumbered,
    source,
    verified
FROM transactions
ORDER BY close_date;

-- name: position_pnl
-- Mark-to-market P&L using contract multipliers and the latest close.
WITH last_px AS (
    SELECT symbol, close
    FROM market_prices mp
    WHERE dt = (SELECT MAX(dt) FROM market_prices m2 WHERE m2.symbol = mp.symbol)
)
SELECT
    p.position_id,
    p.symbol,
    p.quantity,
    p.entry_price,
    lp.close                                                   AS last_price,
    (lp.close - p.entry_price) * p.quantity * i.multiplier     AS pnl_quote_ccy,
    ABS(lp.close * p.quantity * i.multiplier)                  AS gross_notional,
    CASE WHEN p.stop_price IS NULL THEN NULL
         ELSE (p.stop_price - p.entry_price) * p.quantity * i.multiplier END AS pnl_at_stop,
    i.quote_ccy
FROM positions p
JOIN instruments i ON i.symbol = p.symbol
JOIN last_px lp ON lp.symbol = p.symbol
ORDER BY p.position_id;

-- name: daily_returns
-- Simple daily returns by symbol using a window function.
SELECT
    symbol,
    dt,
    close,
    close / LAG(close) OVER (PARTITION BY symbol ORDER BY dt) - 1.0 AS ret
FROM market_prices
ORDER BY symbol, dt;
