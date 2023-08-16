-- The script prints the temperatures between July and August for top 3 cities
-- The syntax below prints the avaerages between July and August
SELECT city, AVG(value) AS "avg_temp" FROM temperatures WHERE month in (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
