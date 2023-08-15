-- The Script displays all the entry in the database except rows with name as NULL
-- The syntax displays all the entires in the table
SELECT score, name  FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
