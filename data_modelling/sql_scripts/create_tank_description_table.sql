-- A script to create tables for the tanks
-- There are different types of tanks with the following properties:
-- 1. equipment_type_id: The id of the equipment(foriegn key to equipment table)
-- 2. tank_tag_id: The id of the tank tag(primary key)
-- 3. tank_description: The description of the tank(text)
-- 4. tank_type: The type of the tank
-- 5. added_date: The date the tank was added
-- 6. updated_date: The date the tank was updated
-- 7. maximum_capacity: The maximum capacity of the tank(float)
-- 8. minimum_capacity: The minimum capacity of the tank(float)
-- 9. additional_capacity: The additional capacity of the tank(float)

CREATE TABLE tank_description (
tank_tag_id VARCHAR(30) NOT NULL PRIMARY KEY,
equipment_type_id INT NOT NULL references equipment_types(equipment_type_id),
tank_description TEXT NOT NULL,
tank_type VARCHAR(30) NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
maximum_capacity FLOAT NOT NULL,
minimum_capacity FLOAT NOT NULL,
additional_capacity FLOAT NOT NULL
);
