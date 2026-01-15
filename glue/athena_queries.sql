-- Preview data
SELECT *
FROM stock_bigdata_db.stock_market_events
LIMIT 10;

-- Average closing price per symbol
SELECT symbol, avg(close) as avg_close
FROM stock_bigdata_db.stock_market_events
GROUP BY symbol
ORDER BY avg_close DESC;

-- Total volume per symbol
SELECT symbol, sum(volume) as total_volume
FROM stock_bigdata_db.stock_market_events
GROUP BY symbol
ORDER BY total_volume DESC;

-- Highest price seen
SELECT symbol, max(high) as highest_price
FROM stock_bigdata_db.stock_market_events
GROUP BY symbol
ORDER BY highest_price DESC;
