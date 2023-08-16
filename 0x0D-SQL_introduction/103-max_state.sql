-- The script finds the average of temperatures
-- The syntax below finds the average of temperature of multiple
-- entires of different cities
SELECT state, MAX(value) AS "max_temp" FROM temperatures GROUP BY state, ORDER BY state;
