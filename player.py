from deck import Deck


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = [deck.deal(), deck.deal()]

    def calc_cards(self):
        return sum(card.value for card in self.hand)

    def __str__(self):
        return f"{self.name} has {self.hand[0]} and {self.hand[1]} for a total of {self.calc_cards()}"


deck = Deck()
deck.shuffle()
player = Player("Player 1", deck)
dealer = Player("Dealer", deck)
print(player)
print(dealer)
