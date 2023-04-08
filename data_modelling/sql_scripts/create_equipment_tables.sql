-- A script to create tables for the equipment database
-- We have the following equipment types:
-- 1. Fiber lines
-- 2. Tanks
-- 3. Evaporators
-- 4. High density concentrators
-- 5. Recovery boilers
-- 6. Slakers

-- Create a table to store the equipment types

CREATE TABLE equipment_typess (
equipment_type_id INT NOT NULL,
equipment_types_name VARCHAR(50) NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
PRIMARY KEY (equipment_type_id)
);
