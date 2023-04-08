"""
A module to create the SQLModel models for the rb_description table.


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

"""


from datetime import datetime
from sqlmodel import SQLModel, Field, ForeignKey
from equipment_types_model import EquipmentTypes


class RecoveryBoilerDescription(SQLModel, table=True):
    """
    A class to create the SQLModel model for the recovery_boiler_description table."""

    __tablename__ = "recovery_boiler_description"

    recovery_boiler_tag_id: str = Field(
        max_length=30,
        description="The unique tag ID of the recovery boiler.",
        primary_key=True,
    )
    equipment_type_id: int = Field(
        foreign_key="equipment_types.equipment_type_id",
        description="The ID of the equipment type associated with the recovery boiler.",
    )
    recovery_boiler_description: str = Field(
        description="The description of the recovery boiler."
    )
    recovery_boiler_type: str = Field(
        max_length=30, description="The type of the recovery boiler."
    )
    maintenance_interval: int = Field(
        description="The maintenance interval of the recovery boiler."
    )
    maintenance_duration: float = Field(
        description="The maintenance duration of the recovery boiler."
    )
    maximum_flow_rate: float = Field(
        description="The maximum flow rate of the recovery boiler."
    )
    minimum_flow_rate: float = Field(
        description="The minimum flow rate of the recovery boiler."
    )
    added_date: datetime = Field(
        default=datetime.utcnow,
        description="The date when the recovery boiler was added.",
    )
    updated_date: datetime = Field(
        default=datetime.utcnow,
        description="The date when the recovery boiler was last updated.",
    )
    types_of_maintenance: str = Field(
        description="The types of maintenance of the recovery boiler."
    )

    # define the foreign key relationship
    equipment_type: EquipmentTypes = ForeignKey(equipment_type_id)
