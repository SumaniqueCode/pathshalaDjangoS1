class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        sum = self.num1+self.num2
        print("The sum of ", self.num1, "and ", self.num2, "is", sum)
    
    def sub(self):
        diff = self.num1-self.num2
        print("The sum of ", self.num1, "and ", self.num2, "is", diff)
    
    def mul(self):
        prod = self.num1*self.num2
        print("The sum of ", self.num1, "and ", self.num2, "is", prod)
    
    def div(self):
        num1=self.num1
        num2= self.num2
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            quotient = num1/num2
            print("The quotient of ", num1, "and ", num2, "is", quotient)

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
calculator = Calculator(num1, num2)
calculator.add()
calculator.sub()
calculator.mul()
calculator.div()