from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


metadata = MetaData()
engine = create_engine('postgresql+psycopg2://Somwl:1548@localhost/users_info')
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "user_information"
    id = Column("id", Integer(),  primary_key=True)
    user_name = Column("user", String(255), nullable=False, unique=True)
    email = Column("email", String(255), nullable=False, unique=True)
    age = Column("age", Integer(), nullable=False)


Base.metadata.create_all(engine)

