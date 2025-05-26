# conditions
num1 = int(input("Enter first number\t"))
num2 = int(input("Second number\t"))
num3 = int(input("Third number\t"))

if num1 > num2:
    if num1>num3:
        print(num1, "is greater than", num2)
elif num2>num1 and num2>num3:
    print(num2, "is greater than", num1)
else:
    print(num3, "is greater than", num1)
    
# else:
#     print(num1, "is less than", num2)
    
#for odd even
# if num1==0:
#     print(num1, "is zero")
# elif num1%2==0:
#     print(num1, "is even number")
# else:
#     print(num1, "is odd number")
