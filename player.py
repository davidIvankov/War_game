#Player is a blueprint to create players of the game and store their information.
from typing import TypedDict

class Card(TypedDict):
    suit: str
    rank: int | str
class Player():
    def __init__(self, name):
        if not name:
            raise ValueError('Name is missing')
        self.name = name
        self.deck = []
        self._current_card = ''
        
    @property
    def current_card(self):
        self._current_card = self.deck.pop()
        return self._current_card

    def win_cards(self, cards):
        self.deck = cards + self.deck
        
    def __str__(self):
        return f'{self.name}: {self._current_card}'