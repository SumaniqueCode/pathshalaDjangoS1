# polymorphism
class A:
    def display_name():
        print("This is class A")


class B(A):  # class B inherits from class A, single level inheritance
    def display_name():
        print("This is class B")


class C(B):  # class C is derived from class B, multi-level inheritance
    def display_name():
        print("This is class C")

    def sum(a, b=0, c=0, d=0):
        add = a + b + c + d
        return add
    
names = [A,B,C]
for name in names:
    name.display_name()

obj = B
obj.display_name()
obj = C
result = obj.sum(1)
result2 = obj.sum(1, 10, 11)
print(result)
print(result2)
