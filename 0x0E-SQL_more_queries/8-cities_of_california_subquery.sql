-- Cities in califonia
-- The syntax uses subquery
SELECT id, name FROM cities WHERE state_id =(
SELECT id FROM states WHERE name = "California")
ORDER BY id;