from random import shuffle
from player import Player, Card

#Deck is a class that should not have instances and is used to generate random deck of cards and deal it to players
#I would also like to use it to evaluate each round winner.

class Deck():
    def __init__(self) -> None:
        raise ValueError('This class should not be instantiated')
    _deck = []
    ranks = list(range(2, 11)) + ['j', 'Q', 'K', 'A']
    
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
                player_1.deck.append(card)
            else: player_2.deck.append(card)
    
    @classmethod
    def round(cls,player_1: Player,player_2: Player, cards):
        card_1 = player_1.current_card
        card_2 = player_2.current_card
        cards += [card_1, card_2]
        print(f'{player_1}\n{player_2}')
        if cls.__card_won(card_1, card_2):
            cls.__winner_of_the_round(player_1, cards)
        elif cls.__card_won(card_2, card_1):
            cls.__winner_of_the_round(player_2, cards)
        else:
            cls.__war(player_1, player_2, cards)


    @classmethod
    def __war(cls, player_1: Player, player_2: Player, cards):
        input('War!')
        cards += [player_1.deck.pop(), player_1.deck.pop(), player_1.deck.pop(), player_2.deck.pop(), player_2.deck.pop(), player_2.deck.pop()]
        cls.round(player_1, player_2, cards)

    
    @classmethod
    def __card_won(cls, card_1: Card, card_2: Card):
        return cls.ranks.index(card_1['rank']) > cls.ranks.index(card_2['rank'])
            
    @classmethod 
    def __winner_of_the_round(cls, player: Player, cards): 
        print(f'{player.name} won!!')       
        player.win_cards(cards)
        
    
        
        