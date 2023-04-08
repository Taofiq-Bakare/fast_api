"""

This module contains the model for the HD Description table.

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
"""

from datetime import datetime
from sqlmodel import SQLModel, Field, ForeignKey
from equipment_types_model import EquipmentTypes


class HdDescription(SQLModel, table=True):
    """

    A class to create the SQLModel model for the hd_description table."""

    __tablename__ = "hd_description"

    hd_tag_id: str = Field(
        max_length=30, description="The unique tag ID of the HD.", primary_key=True
    )
    equipment_type_id: int = Field(
        foreign_key="equipment_types.equipment_type_id",
        description="The ID of the equipment type associated with the HD.",
    )
    hd_description: str = Field(description="The description of the HD.")
    hd_type: str = Field(max_length=30, description="The type of the HD.")
    maintenance_interval: int = Field(description="The maintenance interval of the HD.")
    maintenance_duration: float = Field(
        description="The maintenance duration of the HD."
    )
    maximum_flow_rate: float = Field(description="The maximum flow rate of the HD.")
    minimum_flow_rate: float = Field(description="The minimum flow rate of the HD.")
    added_date: datetime = Field(
        default=datetime.utcnow, description="The date when the HD was added."
    )
    updated_date: datetime = Field(
        default=datetime.utcnow, description="The date when the HD was last updated."
    )
    types_of_maintenance: str = Field(description="The types of maintenance of the HD.")

    # define the foreign key relationship
    equipment_type: EquipmentTypes = ForeignKey(equipment_type_id)
