import random

class CowsBulls:

    def __init__(self):
        self.origin = str(random.randint(0,9999))
        print(self.origin)
        self.turn = 0
        self.playing()

    def playing(self):
        print("Enter {digit} digit for this problem.".format(digit=self.origin.__len__()))
        while True:
            user_guess = input("Enter the number: ")
            if user_guess.lower() == 'exit':
                break
            elif user_guess.__len__() > self.origin.__len__():
                print("Your digit more than answer length, Be carefully.")
                self.playing()
            cows, bulls = self.compare_number(self.origin, user_guess)
            self.turn += 1

            if bulls == self.origin.__len__():
                print("You win the game after {turn} turn(s)!!! The number was {origin}.".format(turn=self.turn, origin=self.origin))
                break
            print("You have {cw} cow(s), and {bl} bull(s).".format(cw=cows, bl=bulls))

    def compare_number(self, origin, usr_input):
        bulls = 0
        try:
            for i in range(len(origin)):
                if origin[i]==usr_input[i]:
                    bulls +=1
        except:
            print("Error length of digits")
            self.playing()
        cows = sum(1 for i in usr_input if i in list(origin))

        return cows, bulls

player1 = CowsBulls()