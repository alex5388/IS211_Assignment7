import random


class Die():
    def __init__(self):
        self.die_number = 0

    def roll(self):
        self.die_number = random.randint(1,6)

    def get_die_number(self):
        return self.die_number


class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0
        self.turn = True


    def addtoFinal(self):
        self.score = self.score + self.turn_score

    def addtoTurn(self, points):
        self.turn_score = self.turn_score + points

    def reset(self):
        self.turn_score = 0

    def reset_turn(self):
        self.turn = True

    def hold_or_roll(self, die):
            while self.turn:
                choose = input("Pick 'r' to roll the die or 'h' to hold.")
                if choose == 'r':
                    die.roll()
                    if die.get_die_number() == 1:
                        #self.reset()
                        print("----{} rolled a {}.".format(self.name, die.get_die_number()))
                        print("You lost your TURN-SCORE points. Your OVERALL SCORE is {}. It's now the next player's turn...".format(self.score))
                        self.turn = False
                        self.reset()
                    elif die.get_die_number() > 1:
                        self.addtoTurn(die.get_die_number())
                        print("----{} rolled a {} and your TURN-SCORE is {}.".format(self.name, die.get_die_number(), self.turn_score))

                elif choose == 'h':
                    self.addtoFinal()
                    print("{} chose to hold, your OVERALL SCORE is currently {}. It's now the next player's turn...".format(self.name, self.score))
                    if self.score >= 100:
                        print("YOU'VE WON!!! game over...")
                        exit()
                    self.reset()
                    self.turn = False




def main():

    die = Die()
    player1 = Player('Player 1')
    player2 = Player('Player 2')

    game = True


    while game:
        player1.hold_or_roll(die)
        player1.reset_turn()
        player2.hold_or_roll(die)
        player2.reset_turn()




if __name__=="__main__":
    main()



