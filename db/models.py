from enum import Enum
from sqlalchemy import Column, Integer, Enum as Enum_s, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Role(Enum):
    user = 0
    dispatcher = 1
    driver = 2


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key = True)
    role = Column(Enum_s(Role), nullable = False)

    login = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)

    first_name = Column(Text)
    second_name = Column(Text)
    number = Column(Text)
