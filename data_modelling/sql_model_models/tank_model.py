"""
create an SQLModel for the tank table

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


"""

from datetime import datetime
from sqlmodel import SQLModel, Field, ForeignKey
from equipment_types_model import EquipmentTypes


class TankDescription(SQLModel, table=True):

    """
    A SQLModel model for the tank_description table."""

    __tablename__ = "tank_description"

    tank_tag_id: str = Field(
        max_length=30, description="The unique tag ID of the tank.", primary_key=True
    )
    equipment_type_id: int = Field(
        foreign_key="equipment_types.equipment_type_id",
        description="The ID of the equipment type associated with the tank.",
    )
    tank_description: str = Field(description="The description of the tank.")
    tank_type: str = Field(max_length=30, description="The type of the tank.")
    added_date: datetime = Field(
        default=datetime.utcnow, description="The date when the tank was added."
    )
    updated_date: datetime = Field(
        default=datetime.utcnow, description="The date when the tank was last updated."
    )
    maximum_capacity: float = Field(description="The maximum capacity of the tank.")
    minimum_capacity: float = Field(description="The minimum capacity of the tank.")
    additional_capacity: float = Field(
        description="The additional capacity of the tank."
    )

    # define the foreign key relationship
    equipment_type: EquipmentTypes = ForeignKey(equipment_type_id)
