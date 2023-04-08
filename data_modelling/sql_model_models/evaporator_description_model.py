"""
A module to create the SQLModel models for the evaporator_description table.

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

"""

from datetime import datetime
from sqlmodel import SQLModel, Field, ForeignKey
from equipment_types_model import EquipmentTypes


class EvaporatorDescription(SQLModel, table=True):

    """
    A class to create the SQLModel model for the evaporator_description table."""

    __tablename__ = "evaporator_description"

    evaporator_tag_id: str = Field(
        max_length=30,
        description="The unique tag ID of the evaporator.",
        primary_key=True,
    )
    equipment_type_id: int = Field(
        foreign_key="equipment_types.equipment_type_id",
        description="The ID of the equipment type associated with the evaporator.",
    )
    evaporator_description: str = Field(
        description="The description of the evaporator."
    )
    evaporator_type: str = Field(
        max_length=30, description="The type of the evaporator."
    )
    washing_interval: int = Field(description="The washing interval of the evaporator.")
    washing_duration: float = Field(
        description="The washing duration of the evaporator."
    )
    maximum_flow_rate: float = Field(
        description="The maximum flow rate of the evaporator."
    )
    minimum_flow_rate: float = Field(
        description="The minimum flow rate of the evaporator."
    )
    added_date: datetime = Field(
        default=datetime.utcnow, description="The date when the evaporator was added."
    )
    updated_date: datetime = Field(
        default=datetime.utcnow,
        description="The date when the evaporator was last updated.",
    )
    types_of_washing: str = Field(description="The types of washing of the evaporator.")

    # define the foreign key relationship
    equipment_type: EquipmentTypes = ForeignKey(equipment_type_id)
