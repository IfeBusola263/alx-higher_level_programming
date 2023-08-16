-- The Script creates a new User and sets the privileges
-- The syntax create a new user
CREATE USER IF NOT EXISTS user_0d_1;
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@'localhost';
