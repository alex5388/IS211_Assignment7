import random


class Die():
    ''' Setup the game equipment '''
    def __init__(self):
        self.die_number = 0

    def roll(self):
        self.die_number = random.randint(1,6)

    def get_die_number(self):
        return self.die_number


class Player():
    ''' Player setup'''
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0
        self.turn = True


    def addtoFinal(self):
        ''' add turn score to the overall score'''
        self.score = self.score + self.turn_score

    def addtoTurn(self, points):
        ''' keep a running tally of turn score'''
        self.turn_score = self.turn_score + points

    def reset(self):
        ''' reset the turn score'''
        self.turn_score = 0

    def reset_turn(self):
        ''' reset who's turn it is'''
        self.turn = True

    def hold_or_roll(self, die):
            ''' main game setup. overall logic of the game '''
            while self.turn:    #run until the player ends their turn
                choose = input("Pick 'r' to roll the die or 'h' to hold.")
                if choose == 'r':
                    die.roll()
                    if die.get_die_number() == 1:
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
                elif choose == 'I win!!':
                    print("Secret Cheat Code Entered...You win...")
                    exit()




def main():

    ''' instantiate objects'''
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



