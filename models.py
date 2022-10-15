from enum import Enum
from typing import List, Optional
from strenum import StrEnum
from db.models import Role

from pydantic import BaseModel


class UserCredit(BaseModel):
    login: str
    password: str


class User(BaseModel):
    id: int

    role: Role
    first_name: str
    second_name: str
