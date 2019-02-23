import random


class Random:

    def __init__(self):
        self.start_num = int(input("Start number with: "))
        self.end_num = int(input("End number with: "))
        self.random_number(self.start_num, self.end_num)

    def random_number(self, start, end):
        random_x = random.randint(start, end)
        print("Random Number is {num}".format(num=random_x))


random_number = Random()
