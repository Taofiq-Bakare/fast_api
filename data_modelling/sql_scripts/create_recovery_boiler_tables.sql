-- A table to create tables for the recovery boilers
-- There are different types of recovery boilers with the following properties:
-- 1. equipment_type_id: The id of the equipment(foriegn key to equipment table)
-- 2. recovery_boiler_tag_id: The id of the recovery boiler tag(primary key)
-- 3. recovery_boiler_description: The description of the recovery boiler(text)
-- 4. recovery_boiler_type: The type of the recovery boiler
-- 5. maintenance_interval: The maintenance interval of the recovery boiler in days(int)
-- 6. maintenance_duration: The maintenance duration of the recovery boiler in hours(int)
-- 7. maximum_flow_rate: The maximum flow rate of the recovery boiler in lps(float)
-- 8. minimum_flow_rate: The minimum flow rate of the recovery boiler in lps(float)
-- 9. added_date: The date the recovery boiler was added
-- 10. updated_date: The date the recovery boiler was updated
-- 11. types_of_maintenance: The types of maintenance the recovery boiler can do
--

CREATE TABLE recovery_boiler_description (
recovery_boiler_tag_id VARCHAR(30) NOT NULL PRIMARY KEY,
equipment_type_id INT NOT NULL references equipment_types(equipment_type_id),
recovery_boiler_description TEXT NOT NULL,
recovery_boiler_type VARCHAR(30) NOT NULL,
maintenance_interval INT NOT NULL,
maintenance_duration FLOAT NOT NULL,
maximum_flow_rate FLOAT NOT NULL,
minimum_flow_rate FLOAT NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
types_of_maintenance VARCHAR(30) NOT NULL
);
