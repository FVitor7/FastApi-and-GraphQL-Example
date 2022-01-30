from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from .models import Address, User, engine


def create_address(
    user_id: int, city: str, cep: str, district: str, street: str, number: str
):
    address = Address(
        user_id=user_id,
        city=city,
        cep=cep,
        district=district,
        street=street,
        number=number,
    )

    with Session(engine) as session:
        session.add(address)
        session.commit()
        session.refresh(address)

    return address


def get_address(
    id: int = None,
    cep: str = None,
    limit: int = 5,
):

    query = select(Address).options(joinedload("*"))

    if id:
        query = query.where(Address.id == id)
    if cep:
        query = query.where(Address.cep == cep)
    if limit:
        query = query.limit(limit)

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def create_user(name: str, email: str, cpf: str, birth_date: str):
    user = User(name=name, email=email, cpf=cpf, birth_date=birth_date)

    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    return user


def get_users(
    id: int = None,
    name: str = None,
    email: str = None,
    limit: int = 5,
):
    query = select(User).options(joinedload("*"))

    if id:
        query = query.where(User.id == id)
    if name:
        query = query.where(User.name == name)
    if email:
        query = query.where(User.email == email)
    if limit:
        query = query.limit(limit)

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result
