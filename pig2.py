import random


class Player():
    round = False

    def __init__(self, turn):
        self.turn = turn
        self.score = 0
        self.overall_score = 0
        self.turn_score = 0

    def roll(self):
        self.seed = random.randint(1, 6)
        return self.seed

    def hold_or_roll(self):
        while self.round != True:

            choose = input("Press 'r' for roll and 'h' to hold.")
            if choose == 'r':
                self.turn_score = self.turn_score + self.roll()
                print("You rolled a {}".format(self.seed))
                if self.seed == 1:
                    print("Your turn is over")
                    self.round = True
                    self.turn_score = 0
                elif self.seed >= 2 and self.seed <= 6:
                    print("You have {} points for this turn so far".format(self.turn_score))
                if self.turn_score >= 100:
                    print("You won the Game!")
                    self.round = True


            elif choose == 'h':
                self.score = self.score + self.turn_score
                print(self.score)
                print("Your OVERALL SCORE is {}.".format(self.score))

                self.turn_score = 0
                self.round_end = True


def main():
    player1 = Player(True)
    player2 = Player(False)
    player1.hold_or_roll()
    player2.hold_or_roll()


if __name__ == "__main__":
    main()