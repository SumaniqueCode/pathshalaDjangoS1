# initialization, condition, increment/decrement

# while loop
i = 1
while i <= 10:
    print(i)
    i = i + 1


# for loop
num = int(input("Enter the range: "))
sum = 0
for i in range(num):
    num2 = int(input("Enter the number to be added: "))
    sum = sum + num2
print(sum)

# nested loop
for j in range(5):
    for k in range(j):
        print(j, end=" ")
    print()
