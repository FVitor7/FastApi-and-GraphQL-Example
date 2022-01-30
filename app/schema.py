from typing import Optional, List
import strawberry
from strawberry.fastapi import GraphQLRouter
from .db_function import create_user, get_users, create_address, get_address


@strawberry.type
class User:
    id: Optional[int]
    name: str
    email: str
    cpf: str
    birth_date: str
    address: List["Address"]


@strawberry.type
class Address:
    id: Optional[int]
    user: "User"
    city: str
    cep: str
    district: str
    street: str
    number: str


@strawberry.type
class Query:
    all_users: List[User] = strawberry.field(resolver=get_users)
    all_address: List[Address] = strawberry.field(resolver=get_address)


@strawberry.type
class Mutation:
    create_user: User = strawberry.field(resolver=create_user)
    create_address: Address = strawberry.field(resolver=create_address)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)
