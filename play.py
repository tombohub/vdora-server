from typing import List
from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Momo:
    name: str


@dataclass
class Kaka:
    bobo: List[Momo]


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


def koko(mo: User):
    mo.friends.
