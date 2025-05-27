# functions in python

# function with no parameter and no return value
def display_hello_world():
    print("Hello, World!")

display_hello_world()

# function with parameter and no return value
def sum(num1, num2):
    add = num1 + num2
    print("The sum is ", add)

a=10
b=21
sum(a, b)

# function with parameter and return value
def fact(num):
    if num == 0:
        return 1
    else:
        i=1
        result=1
        while i<=num:
            result = result*i
            i=i+1
    return result

num = int(input("Enter a number: "))
result = fact(num)
print("Factorial of", num, "is", result)           
