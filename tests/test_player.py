import sys
sys.path.append('../')
from player import Player

def test_Player():
    player = Player('David')
    player.deck = [{'suit': 'diamonds', 'rank': 1}]
    player.win_cards([1, 2])
    assert player.deck == [1, 2, {'suit': 'diamonds', 'rank': 1}]
    assert player.current_card == {'suit': 'diamonds', 'rank': 1}
    assert player.deck == [1, 2]