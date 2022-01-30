from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Relationship
)

# Criar engine do banco
engine = create_engine('sqlite:///database.db')

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    cpf:str
    birth_date: str

    address: List['Address'] = Relationship(back_populates='user')


class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key='user.id')
    user: Optional[User] = Relationship(back_populates='address')
    city: str
    cep: str
    district: str
    street: str
    number: str


SQLModel.metadata.create_all(engine)