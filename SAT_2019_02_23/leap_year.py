class LeapYear:

    def __init__(self):
        while True:
            self.option = int(input("Enter option 1:[A.D.] or 2:[B.E.]: "))
            self.statement = {
                1: self.calculator_leap_year,
                2: self.buddhist_era
            }
            try:
                self.statement[self.option](int(input("Enter a year: ")))
            except KeyError as error:
                print("Please insert 1:[A.D.] or 2:[B.E.]: only.")


    def buddhist_era(self, input_year):
        self.calculator_leap_year(input_year - 543)

    def calculator_leap_year(self, input_year):
        if (input_year % 4) == 0:
            if (input_year % 100) == 0:
                if (input_year % 400) == 0:
                    print("{yrs} is a leap year".format(yrs=input_year))
                else:
                    print("{yrs} is not a leap year".format(yrs=input_year))
            else:
                print("{yrs} is a leap year".format(yrs=input_year))
        else:
            print("{yrs} is not a leap year".format(yrs=input_year))

        exit()


year = LeapYear()
