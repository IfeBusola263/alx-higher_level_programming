-- The script create Table
-- The syntax creates a table and sets the attributes and constraints
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
