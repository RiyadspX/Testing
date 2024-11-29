class Calculator:
    """ This a calculator class
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if self.b == 0:
            raise ValueError('Cant divide by Zero')
        return self.a / self.b    
    def substract(self):
        return self.a - self.b
    def power(self):
        return self.a ** self.b

if __name__ == "__main__":
    calc = Calculator(10, 3)
    print(Calculator(10, 15).add())