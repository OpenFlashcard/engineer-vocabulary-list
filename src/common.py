from typing import List
from items import Item
from datetime import datetime


class Field:
    def __init__(self, name: str, value: List[Item]) -> None:
        self.name = name
        self.value = value


class Card:
    def __init__(self, fields: List[Field]) -> None:
        self.fields = fields


class Deck:
    def __init__(self, name: str, cards: List[Card]) -> None:
        self.name = name
        code = datetime.now
        self.id = '_'.join([name, code])
        self.cards = cards
