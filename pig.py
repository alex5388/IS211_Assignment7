import random


class Player():


    turn = True

    def __init__(self):
        self.seed = 0
        self.score = 0



    def roll(self):
        self.seed = random.randint(1, 6)
        return self.seed

    def hold_or_roll(self):
        while Player.turn == True:
            choose = input("Press 'r' for roll and 'h' to hold.")
            if choose == 'r':

                print("Rolling...")
                print(self.score)
                turn_score =+ self.roll()
                print(turn_score)


            elif choose == 'h':
                print("You received {} points".format(Player.turn_score))


class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0


def main():
    player1 = Player()
    player2 = Player()
    Game(player1, player2)
    player1.hold_or_roll()



if __name__ == "__main__":
    main()