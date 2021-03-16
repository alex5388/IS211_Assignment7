import random


class Player():
    def __init__(self):
        self.score = 0
        self.turn_score = 0
        self.die_num = 0

    def roll(self):
        self.seed = random.randint(1, 6)
        return self.seed

    def hold_or_roll(self):
        while self.die_num != 1:

            choose = input("Press 'r' for roll and 'h' to hold.")
            if choose == 'r':
                self.turn_score = self.turn_score + self.roll()
                print("You rolled a {}".format(self.seed))
                print("Your turn score is {}".format(self.turn_score))

            elif choose == 'h':
                self.score = self.score + self.turn_score
                print(self.score)
                print("You received {} points toward your overall score of {}".format(self.turn_score, self.score))
        return self.turn_score == 0


class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        #self.player1.score = 0
        #self.player2.score = 0


def main():
    player1 = Player()
    player2 = Player()
    Game(player1, player2)
    player1.hold_or_roll()





if __name__ == "__main__":
    main()



