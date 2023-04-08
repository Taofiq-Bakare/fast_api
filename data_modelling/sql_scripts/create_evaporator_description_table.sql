-- A script to create the table for the evaporator description
-- There are different types of evaporators with the following properties:
-- 1. equipment_type_id: The id of the equipment(foriegn key to equipment table)
-- 2. evaporator_tag_id: The id of the evaporator tag(primary key)
-- 3. evaporator_description: The description of the evaporator(text)
-- 4. evaporator_type: The type of the evaporator
-- 5. washing_interval: The washing interval of the evaporator in days(int)
-- 6. washing_duration: The washing duration of the evaporator in hours(int)
-- 7. maximum_flow_rate: The maximum flow rate of the evaporator in lps(float)
-- 8. minimum_flow_rate: The minimum flow rate of the evaporator in lps(float)
-- 9. added_date: The date the evaporator was added
-- 10. updated_date: The date the evaporator was updated
-- 11. types_of_washing: The types of washing the evaporator can do


CREATE TABLE evaporator_description (
evaporator_tag_id VARCHAR(30) NOT NULL PRIMARY KEY,
equipment_type_id INT NOT NULL references equipment_types(equipment_type_id),
evaporator_description TEXT NOT NULL,
evaporator_type VARCHAR(30) NOT NULL,
washing_interval INT NOT NULL,
washing_duration FLOAT NOT NULL,
maximum_flow_rate FLOAT NOT NULL,
minimum_flow_rate FLOAT NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
types_of_washing VARCHAR(30) NOT NULL
);
