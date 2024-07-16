#Player is a blueprint to create players of the game and store their information.
class Player():
    def __init__(self, name):
        self.name = name
        self._deck = []

    def set_deck(self, card):
        self._deck.append(card)