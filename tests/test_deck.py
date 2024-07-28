import sys
sys.path.append('../')
from player import Player
from deck import Deck

p_1 = Player('ja')
p_2 = Player('s')
def test_deal_cards(): 
    Deck.deal_cards(p_1, p_2)
    assert len(p_1.deck) is 26
    
    
    