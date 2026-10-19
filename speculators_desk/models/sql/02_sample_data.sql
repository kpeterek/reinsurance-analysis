-- SIMULATED DATA for exercises. Not historical. Do not cite.

INSERT INTO properties VALUES
 (1, 'Subject Hotel (sim)', 'hotel', 'TX-I35-secondary', 82, NULL),
 (2, 'Comp Hotel A (sim)',  'hotel', 'TX-I35-secondary', 95, NULL),
 (3, 'Warehouse (sim)',     'industrial', 'Sunbelt-metro', NULL, 140000);

INSERT INTO hotel_monthly VALUES
 (1,'2025-10',31,2542,1830,214110.0,0.690,119.00),
 (1,'2025-11',30,2460,1600,184000.0,0.640,116.00),
 (1,'2025-12',31,2542,1450,162400.0,0.580,112.00),
 (1,'2026-01',31,2542,1500,169500.0,0.600,114.00),
 (1,'2026-02',28,2296,1560,180960.0,0.680,117.00),
 (1,'2026-03',31,2542,1910,229200.0,0.760,121.00);

INSERT INTO transactions VALUES
 (1, NULL, '2026-03-15', 5200000, 495000, 'trailing', 3300000, 0,       'simulated', 0),
 (2, NULL, '2026-05-02', 6100000, 560000, 'trailing', 3900000, 750000,  'simulated', 0),
 (3, NULL, '2026-06-20', 4700000, 470000, 'trailing', 2900000, 0,       'simulated', 0),
 (4, NULL, '2026-08-09', 7400000, 690000, 'stabilized', 4600000, 0,     'simulated', 0);

INSERT INTO instruments VALUES
 ('ES',  'equity_index_future', 50,     'USD', 'E-mini S&P 500 (USD 50 x index)'),
 ('ZN',  'treasury_future',     1000,   'USD', '10-Year T-Note future (USD 1,000 x price points)'),
 ('GC',  'commodity_future',    100,    'USD', 'Gold (100 troy oz)'),
 ('EURUSD','fx',                1,      'USD', 'EUR/USD spot, quantity in EUR');

INSERT INTO market_prices VALUES
 ('ES','2026-10-12',5000.00,'simulated'),('ES','2026-10-13',4985.25,'simulated'),
 ('ES','2026-10-14',4940.00,'simulated'),('ES','2026-10-15',4962.50,'simulated'),
 ('ES','2026-10-16',4910.75,'simulated'),
 ('GC','2026-10-12',2400.0,'simulated'),('GC','2026-10-13',2412.5,'simulated'),
 ('GC','2026-10-14',2430.0,'simulated'),('GC','2026-10-15',2421.0,'simulated'),
 ('GC','2026-10-16',2445.0,'simulated'),
 ('EURUSD','2026-10-12',1.0850,'simulated'),('EURUSD','2026-10-13',1.0810,'simulated'),
 ('EURUSD','2026-10-14',1.0790,'simulated'),('EURUSD','2026-10-15',1.0760,'simulated'),
 ('EURUSD','2026-10-16',1.0720,'simulated');

INSERT INTO positions VALUES
 (1,'ES',      3,       5000.00,'2026-10-12',4900.00,'T-001'),
 (2,'GC',     -2,       2400.00,'2026-10-12',2460.00,'T-002'),
 (3,'EURUSD',  2000000, 1.0850, '2026-10-12',1.0700, 'T-003');
