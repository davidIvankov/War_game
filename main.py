from player import Player
from deck import Deck
#main file where game flow is established, now contains unpopulated functions that replace pseudocode.

def game_init():
    player_one = Player(input("Player one name: "))
    player_two = Player(input("Player two name: "))
    Deck.deal_cards(player_two, player_one)


def player_move(): ...
def result(player_one, player_two): ...
def war(): ...
def calculate_end(player_one_score, player_two_score): ...
def main():
    game_init()


if __name__ == "__main__":
    main()
