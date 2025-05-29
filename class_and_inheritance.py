# basic class
class A:
    def display_name():
        print("This is class A")


class B(A):  # class B inherits from class A, single level inheritance
    def print_name():
        print("This is class B")

class C(B):  # class C is derived from class B, multi-level inheritance
    def print_data():
        print("This is class C")

class Sum:
    #constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        result= self.num1 + self.num2
        return result
        
# obj = A
# obj.display_name()

# obj2 = B
# obj2.print_name()
# obj2.display_name()

obj3 = C
# obj3.print_data()
# obj3.print_name()
obj3.display_name()

# obj4 = Sum(1,3)
# print(obj4.add())
