from random import shuffle
from player import Player

#Deck is a class that should not have instances and is used to generate random deck of cards and deal it to players
#I would also like to use it to evaluate each round winner.

class Deck():
    def __init__(self) -> None:
        raise ValueError('This class should not be instantiated')
    _deck = []
    
    
    @staticmethod
    def __generate_deck():
        deck = []
        ranks = list(range(2, 11)) + ['j', 'Q', 'K', 'A']
        for suit in ['diamonds', 'clubs', 'hearts', 'spades']:
            for rank in ranks:
                deck.append({'suit': suit, 'rank': rank}) 

        shuffle(deck) 
        return deck

    @classmethod
    def deal_cards(cls, player_1: Player, player_2: Player):
        cls._deck = cls.__generate_deck()
        for index, card in enumerate(cls._deck):
            if index % 2 == 0:
                player_1.set_deck(card)
            else: player_2.set_deck(card)
        
        
    
        
        