"""
CREATE TABLE fiberline_description (
fiberline_tag_id VARCHAR(30) NOT NULL,
equipment_type_id INT NOT NULL references equipment_types(equipment_type_id),
fiberline_description TEXT NOT NULL,
fiberline_type VARCHAR(30) NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
maximum_capacity INT NOT NULL,
minimum_capacity INT NOT NULL,
PRIMARY KEY (fiberline_tag_id)
);

"""

"""_summary_
"""

from datetime import datetime
from sqlmodel import SQLModel, Field, ForeignKey
from equipment_types_model import EquipmentTypes


class FiberlineDescription(SQLModel, table=True):
    """
    A class to create the SQLModel model for the fiberline_description table.

    """

    __tablename__ = "fiberline_description"

    fiberline_tag_id: str = Field(
        max_length=30, description="The unique tag ID of the fiberline."
    )
    equipment_type_id: int = Field(
        foreign_key="equipment_types.equipment_type_id",
        description="The ID of the equipment type associated with the fiberline.",
    )
    fiberline_description: str = Field(description="The description of the fiberline.")
    fiberline_type: str = Field(max_length=30, description="The type of the fiberline.")
    added_date: datetime = Field(
        default=datetime.utcnow, description="The date when the fiberline was added."
    )
    updated_date: datetime = Field(
        default=datetime.utcnow,
        description="The date when the fiberline was last updated.",
    )
    maximum_capacity: int = Field(description="The maximum capacity of the fiberline.")
    minimum_capacity: int = Field(description="The minimum capacity of the fiberline.")

    # define the foreign key relationship
    equipment_type: EquipmentTypes = ForeignKey(equipment_type_id)
