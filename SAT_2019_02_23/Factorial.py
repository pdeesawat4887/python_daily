class Factorial:

    def __init__(self):
        end = int(input("Enter position of your Factorial: "))
        if end < 0:
            print('Please insert positive number.')
            factorial = Factorial()
        elif end == 0:
            print(1)
        for length in range(0, end + 1):
            print(length, ":", self.Factorial(length))

    def Factorial(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return n
        else:
            return self.Factorial(n - 1) * n


factorial = Factorial()
