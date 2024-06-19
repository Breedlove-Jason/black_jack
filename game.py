from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player 1", self.deck)
        self.dealer = Player("Dealer", self.deck)
        self.game_loop = True

    def player_turn(self):
        while self.player.calc_cards() < 21:
            print(self.player)
            choice = input("Do you want to hit or stay? ").lower()
            if choice == "hit":
                self.player.hit(self.deck)
            elif choice == "stay":
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Bust! You lose.")
            self.game_loop = False

    def dealer_turn(self):
        while self.dealer.calc_cards() < 17:
            self.dealer.hit(self.deck)
        print(self.dealer)

    def win_check(self):
        player_score = self.player.calc_cards()
        dealer_score = self.dealer.calc_cards()

        if player_score > 21:
            print("Bust! You lose.")
        elif dealer_score > 21:
            print("Dealer busts! You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")
