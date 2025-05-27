# basic class
class A:
    def display_name():
        print("This is class A")


class B(A):  # class B inherits from class A
    def print_name():
        print("This is class B")


class C(B):  # class C is derived from class B
    def print_data():
        print("This is class C")


obj = A
obj.display_name()

obj2 = B
obj2.print_name()
obj2.display_name()

obj3 = C
obj3.print_data()
obj3.print_name()
obj3.display_name()
