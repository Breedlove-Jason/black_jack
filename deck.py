from card import Card, values, suits
import random


class Deck:
    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in values:
                self.cards.append(Card(rank, suit))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
deck.print_deck()

deck.shuffle()
deck.print_deck()
