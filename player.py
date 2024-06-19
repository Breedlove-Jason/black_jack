from deck import Deck


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = [deck.deal(), deck.deal()]

    def calc_cards(self):
        return sum(card.value for card in self.hand)

    def ace_adjust(self):
        while self.calc_cards() > 21:
            for card in self.hand:
                if card.rank == "A":
                    card.value = 1

    def hit(self, deck):
        self.hand.append(deck.deal())
        self.ace_adjust()
        return self.hand

    def stay(self):
        return self.calc_cards()

    def __str__(self):
        cards = ", and a ".join(str(card) for card in self.hand)
        return f"{self.name} has a {cards} for a total of {self.calc_cards()}"
