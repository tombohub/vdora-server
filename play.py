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
    def koko(self, mama):
        def lili(mama):
            bibi = 'laka'
            print(f'ovoe je moja {mama}')

        lili(mama)
        print(f'mama je sada {bibi}')


ko = Momo()

bobo = 'kikila'
ko.koko(bobo)
