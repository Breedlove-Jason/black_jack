from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player 1", self.deck)
        self.dealer = Player("Dealer", self.deck)
        self.game_loop = True

