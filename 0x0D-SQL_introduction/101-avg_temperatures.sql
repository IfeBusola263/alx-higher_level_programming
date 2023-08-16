-- The script finds the average of temperatures
-- The syntax below finds the average of temperature of multiple
-- entires of different cities
SELECT city, AVG(value) AS "avg_temp" FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
