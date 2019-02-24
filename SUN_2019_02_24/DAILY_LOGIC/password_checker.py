import getpass


class CheckPassword:

    def __init__(self):
        self.level = 0
        self.statements = {
            5: 'Strong',
            4: 'Normal',
            3: 'Normal',
            2: 'Weak',
            1: 'Weak',
            0: 'Very Weak',
        }
        self.input_password = getpass.getpass('Enter password: ')
        self.check()
        print("Your Password [{pwd}] is {level}.".format(pwd='*' * self.input_password.__len__(),
                                                         level=self.statements[self.level]))

    def check(self):
        self.level += self.n_length(self.input_password)
        self.level += self.n_lower_chars(self.input_password)
        self.level += self.n_upper_chars(self.input_password)
        self.level += self.hasNumbers(self.input_password)
        self.level += self.hasPunctuationMark(self.input_password)

    def n_length(self, string):
        if string.__len__() == 0:
            print("Empty Password")
            exit()
        elif string.__len__() < 8:
            return 0
        return 1

    def n_lower_chars(self, string):
        if sum(1 for str in string if str.islower()) < 1:
            return 0
        return 1

    def n_upper_chars(self, string):
        if sum(1 for str in string if str.isupper()) < 1:
            return 0
        return 1

    def hasNumbers(self, string):
        if sum(1 for str in string if str.isdigit()) < 1:
            return 0
        return 1

    def hasPunctuationMark(self, string):
        mark = '!@#$%^&*()?'
        if sum(1 for str in string if str in mark) < 1:
            return 0
        return 1


pwd = CheckPassword()
