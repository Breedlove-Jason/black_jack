from game import Game
from art import art


class Main:

    def __init__(self):
        print(art)
        player_turn = Game().player_turn()
        dealer_turn = Game().dealer_turn()
        win_check = Game().win_check()


if __name__ == "__main__":
    main = Main()
