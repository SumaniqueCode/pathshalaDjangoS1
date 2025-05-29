

num1=0
num2=20

try:
    if num1==0:
        raise ZeroDivisionError("Error: Division by zero is not allowed")
    result = num1 / num2
    print(result)
except ZeroDivisionError as e:
    print(e)