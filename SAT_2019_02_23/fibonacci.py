class Fibonacci:

    def __init__(self):
        end = int(input("Enter position of your fibonacci: "))
        for length in range(0, end + 1):
            print(length + 1, ":", self.fibonacci(length))

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)


fibo = Fibonacci()
