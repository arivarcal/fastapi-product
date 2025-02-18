
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class CustomerBase(SQLModel):
    ci: str = Field(default=None)
    name: str = Field(default=None)
    address: str | None = Field(default=None)

# Modelo para crear una nueva tarea (hereda de CustomerBase)
class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass
