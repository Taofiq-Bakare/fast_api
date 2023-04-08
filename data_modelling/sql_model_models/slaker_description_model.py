"""
A module to create the SQLModel models for the slaker_description table.



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

"""

from datetime import datetime
from sqlmodel import SQLModel, Field, ForeignKey
from equipment_types_model import EquipmentTypes


class SlakerDescription(SQLModel, table=True):
    """
    A SQLModel model for the slaker_description table."""

    __tablename__ = "slaker_description"

    slaker_tag_id: str = Field(
        max_length=30, description="The unique tag ID of the slaker.", primary_key=True
    )
    equipment_type_id: int = Field(
        foreign_key="equipment_types.equipment_type_id",
        description="The ID of the equipment type associated with the slaker.",
    )
    slaker_description: str = Field(description="The description of the slaker.")
    slaker_type: str = Field(max_length=30, description="The type of the slaker.")
    maximum_capacity: float = Field(description="The maximum capacity of the slaker.")
    minimum_capacity: float = Field(description="The minimum capacity of the slaker.")
    maintenance_interval: int = Field(
        description="The maintenance interval of the slaker."
    )
    maintenance_duration: float = Field(
        description="The maintenance duration of the slaker."
    )
    added_date: datetime = Field(
        default=datetime.utcnow, description="The date when the slaker was added."
    )
    updated_date: datetime = Field(
        default=datetime.utcnow,
        description="The date when the slaker was last updated.",
    )
    types_of_maintenance: str = Field(
        max_length=30, description="The types of maintenance of the slaker."
    )

    # define the foreign key relationship
    equipment_type: EquipmentTypes = ForeignKey(equipment_type_id)
