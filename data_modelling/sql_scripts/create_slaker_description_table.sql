-- A description table for the slakers
-- There are different types of slakers with the following properties:
-- 1. equipment_type_id: The id of the equipment(foriegn key to equipment table)
-- 2. slaker_tag_id: The id of the slaker tag(primary key)
-- 3. slaker_description: The description of the slaker(text)
-- 4. slaker_type: The type of the slaker
--5. maximum_capacity: The maximum capacity of the slaker(float)
-- 6. minimum_capacity: The minimum capacity of the slaker(float)
-- 7. maintenance_interval: The maintenance interval of the slaker in days(int)
-- 8. maintenance_duration: The maintenance duration of the slaker in hours(int)
-- 9. added_date: The date the slaker was added
-- 10. updated_date: The date the slaker was updated
-- 11. types_of_maintenance: The types of maintenance the slaker can do
--
CREATE TABLE slaker_description (
slaker_tag_id VARCHAR(30) NOT NULL PRIMARY KEY,
equipment_type_id INT NOT NULL references equipment_types(equipment_type_id),
slaker_description TEXT NOT NULL,
slaker_type VARCHAR(30) NOT NULL,
maximum_capacity FLOAT NOT NULL,
minimum_capacity FLOAT NOT NULL,
maintenance_interval INT NOT NULL,
maintenance_duration FLOAT NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
types_of_maintenance VARCHAR(30) NOT NULL
);
