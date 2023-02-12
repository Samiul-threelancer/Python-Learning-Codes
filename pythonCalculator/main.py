class Calculator():

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def summation(self):
        return self.number1+self.number2

    def substraction(self):
        return self.number1- self.number2

    def multi(self):
        return self.number1* self.number2

    def div(self):
        try:
            return self.number1 / self.number2
        except Exception as e:
            print(e)

while True:
    x= int(input("Give an integer: "))
    y= int(input("Give an integer: "))
    cal = Calculator(x, y)
    print(f"Summation: {cal.summation()} \nSubstraction:{cal.substraction()} \nMultiplication:{cal.multi()} \nDivision:{cal.div()}")
