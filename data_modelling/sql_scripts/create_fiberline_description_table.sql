-- A table to store the description of the fiber lines
-- There are five types of fiber lines
-- With the following properties:
-- 1. equipment_id: The id of the equipment(foriegn key to equipment table)
-- 2. fiberline_tag_id: The id of the fiberline tag(primary key)
-- 3. fiberline_description: The description of the fiberline(text)
-- 4. fiberline_type: The type of the fiberline
-- 5. added_date: The date the fiberline was added
-- 6. updated_date: The date the fiberline was updated
-- 7. maximum_capacity: The maximum capacity of the fiberline
-- 8. minimum_capacity: The minimum capacity of the fiberline

CREATE TABLE fiberline_description (
fiberline_tag_id VARCHAR(30) NOT NULL,
equipment_type_id INT NOT NULL references equipment_types(equipment_type_id),
fiberline_description TEXT NOT NULL,
fiberline_type VARCHAR(30) NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
maximum_capacity INT NOT NULL,
minimum_capacity INT NOT NULL,
PRIMARY KEY (fiberline_tag_id)
);

-- Path: data_modelling\create_fiberline_description_table.sql
