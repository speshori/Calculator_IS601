def addition(x1, x2):
    return x1 + x2

def subtraction(x1, x2):
    return x1 - x2

def division(x1, x2):
    return x1 / x2

def squareNumber(x1):
    return x1 * x1


class calculator:

    result = 0

    def __init__(self):
        self.result = 1
        pass

    def add(self, x1, x2):
        self.result = addition(x1, x2)
        return self.result

    def subtract(self, x1, x2):
        self.result = subtraction(x1, x2)
        return self.result

    def divide(self, x1, x2):
        self.result = division(x1, x2)
        return self.result

    def square(self, x1):
        self.result = squareNumber(x1)
        return self.result

