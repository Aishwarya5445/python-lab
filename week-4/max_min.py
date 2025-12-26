num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

minimum = 0
maximum = 0

if (num1 >= num2) and (num1 >= num3):
    maximum = num1
elif (num2 >= num1) and (num2 >= num3):
    maximum = num2
else:
    maximum = num3

if (num1 <= num2) and (num1 <= num3):
    minimum = num1
elif (num2 <= num1) and (num2 <= num3):
    minimum = num2
else:
    minimum = num3
print(f"The numbers entered are: {num1}, {num2}, {num3}")
print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")

