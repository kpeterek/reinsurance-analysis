-- The Speculator's Desk: research and risk database (SQLite dialect; portable to PostgreSQL
-- with minor type changes). Sample data in 02_sample_data.sql are SIMULATED and labeled so.

CREATE TABLE IF NOT EXISTS properties (
    property_id   INTEGER PRIMARY KEY,
    name          TEXT NOT NULL,
    property_type TEXT NOT NULL CHECK (property_type IN ('hotel','multifamily','office','retail','industrial','land')),
    market        TEXT NOT NULL,
    rooms_or_units INTEGER,
    rentable_sf   INTEGER
);

-- Monthly hotel operating data (STR-style): one row per property per month.
CREATE TABLE IF NOT EXISTS hotel_monthly (
    property_id     INTEGER NOT NULL REFERENCES properties(property_id),
    month           TEXT NOT NULL,              -- 'YYYY-MM'
    days            INTEGER NOT NULL,
    rooms_available INTEGER NOT NULL,           -- room-nights available in the month
    rooms_sold      INTEGER NOT NULL,
    room_revenue    REAL NOT NULL,
    comp_occ        REAL,                       -- competitive set occupancy (decimal)
    comp_adr        REAL,
    PRIMARY KEY (property_id, month)
);

-- CRE transactions (comparable sales) with financing detail.
CREATE TABLE IF NOT EXISTS transactions (
    txn_id         INTEGER PRIMARY KEY,
    property_id    INTEGER REFERENCES properties(property_id),
    close_date     TEXT NOT NULL,
    price          REAL NOT NULL,
    noi_at_sale    REAL,                        -- forward or trailing: see noi_basis
    noi_basis      TEXT CHECK (noi_basis IN ('trailing','forward','stabilized')),
    loan_amount    REAL,
    pip_or_capex_required REAL DEFAULT 0,
    source         TEXT NOT NULL,               -- e.g., 'simulated', 'CoStar', 'county deed'
    verified       INTEGER NOT NULL DEFAULT 0
);

-- Daily market prices for public instruments.
CREATE TABLE IF NOT EXISTS market_prices (
    symbol   TEXT NOT NULL,
    dt       TEXT NOT NULL,                     -- 'YYYY-MM-DD'
    close    REAL NOT NULL,
    source   TEXT NOT NULL,
    PRIMARY KEY (symbol, dt)
);

-- Instrument metadata: contract multipliers, quote conventions.
CREATE TABLE IF NOT EXISTS instruments (
    symbol      TEXT PRIMARY KEY,
    asset_class TEXT NOT NULL,
    multiplier  REAL NOT NULL DEFAULT 1,        -- e.g., ES = 50 USD per index point
    quote_ccy   TEXT NOT NULL DEFAULT 'USD',
    description TEXT
);

-- Hypothetical portfolio positions for the risk dashboard.
CREATE TABLE IF NOT EXISTS positions (
    position_id INTEGER PRIMARY KEY,
    symbol      TEXT NOT NULL REFERENCES instruments(symbol),
    quantity    REAL NOT NULL,                  -- contracts or units; negative = short
    entry_price REAL NOT NULL,
    entry_date  TEXT NOT NULL,
    stop_price  REAL,
    thesis_id   TEXT
);
