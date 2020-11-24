from typing import List
from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Momo:
    name: str


@dataclass
class Kaka:
    bobo: List[Momo]


class Momo:

    nono = ' nono'

    def koko(self):
        print(self.nono)


ko = Momo()

ko.koko()
