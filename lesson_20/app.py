from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

metadata = MetaData()
engine = create_engine('postgresql+psycopg2://Somwlin:1548@localhost/auth_n_post')
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "author"
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(255), nullable=False, unique=True)


class Article(Base):
    __tablename__ = 'article'
    id = Column('id', Integer(), primary_key=True)
    article_name = Column('article_name', String(255))
    content = Column('content', String(255))


Base.metadata.create_all(engine)
