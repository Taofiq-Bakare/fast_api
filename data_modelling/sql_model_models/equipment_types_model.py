"""
A module to create the SQLModel models for the database tables.


CREATE TABLE equipment_types (
equipment_type_id SERIAL NOT NULL PRIMARY KEY,
equipment_types_name VARCHAR(50) NOT NULL,
added_date TIMESTAMP NOT NULL,
updated_date TIMESTAMP NOT NULL,
);

"""

import os
from datetime import datetime
from sqlmodel import SQLModel, Field


class EquipmentTypes(SQLModel, table=True):
    """
    A class to create the SQLModel model for the equipment_types table.
    """

    __tablename__ = "equipment_types"

    equipment_type_id: int = Field(
        default=None,
        primary_key=True,
        description="The unique ID of the equipment type.",
    )
    equipment_types_name: str = Field(
        max_length=50, description="The name of the equipment type."
    )
    added_date: datetime = Field(
        default=datetime.utcnow,
        description="The date when the equipment type was added.",
    )
    updated_date: datetime = Field(
        default=datetime.utcnow,
        description="The date when the equipment type was last updated.",
    )


# test the model


# if __name__ == "__main__":
#     DATABASE_URL = os.getenv("DATABASE_URL")
#     engine = create_engine(DATABASE_URL, echo=True)
#     SQLModel.metadata.create_all(engine)

#     with Session(engine) as session:
#         equipment_type_1 = EquipmentTypes(
#             # equipment_type_id=1,
#             equipment_types_name="test1 equipment type",
#             added_date=datetime.utcnow(),
#             updated_date=datetime.utcnow(),
#         )
#         session.add(equipment_type_1)
#         session.commit()
#         session.refresh(equipment_type_1)

#         print(equipment_type_1)
