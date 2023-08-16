-- The script converts the the database to UTF-8
-- the syntax below converts the DB, Table and name column to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- IF EXISTS (SELECT * FROM information_schema.tables
-- WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table') THEN
ALTER TABLE first_table CONVERT TO CHARACTER
SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY
name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- END IF;
