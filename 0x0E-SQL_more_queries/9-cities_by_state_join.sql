-- Display records of cities and states
-- Order of display is cities.id, city, state
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
