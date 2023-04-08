-- A description table for the high density concentrators
-- There are different types of high density concentrators with the following properties:
-- 1. equipment_type_id: The id of the equipment(foriegn key to equipment table)
-- 2. hd_tag_id: The id of the hd tag(primary key)
-- 3. hd_description: The description of the hd(text)
-- 4. hd_type: The type of the hd
-- 5. maintenance_interval: The maintenance interval of the hd in days(int)
-- 6. maintenance_duration: The maintenance duration of the hd in hours(int)
-- 7. maximum_flow_rate: The maximum flow rate of the hd in lps(float)
-- 8. minimum_flow_rate: The minimum flow rate of the hd in lps(float)
-- 9. added_date: The date the hd was added
-- 10. updated_date: The date the hd was updated
-- 11. types_of_maintenance: The types of maintenance the hd can do
--

CREATE TABLE hd_description (
hd_tag_id VARCHAR(30) NOT NULL PRIMARY KEY,
equipment_type_id INT NOT NULL references equipment_types(equipment_type_id),
hd_description TEXT NOT NULL,
hd_type VARCHAR(30) NOT NULL,
maintenance_interval INT NOT NULL,
maintenance_duration FLOAT NOT NULL,
maximum_flow_rate FLOAT NOT NULL,
minimum_flow_rate FLOAT NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
types_of_maintenance VARCHAR(30) NOT NULL
);
