# program on Python Built-in Functions
# Input and Output
name = input("Enter your name: ")
print("Hello,", name)
# type()  
age = 19
print("Type of age:", type(age))
# len() 
print("Length of your name:", len(name))
# abs() 
num = -100
print("Absolute value:", abs(num))
# max() and min()
lst1 = [20,21,33,5,26,29]
print("Maximum number:", max(lst1))
print("Minimum number:", min(lst1))
# sum()
print("Sum of numbers:", sum(lst1))
# sorted()
print("Sorted list:", sorted(lst1))
# round() 
value = 12.5678
print("Rounded value:", round(value, 3))
# pow() 
print("2 to the power 3:", pow(2, 3))
# range() 
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)
# bin()
num1=10
binary_value = bin(num1)
print("Number before converting into binary:", num1)
print("Binary value:", binary_value)
#dict
student= [("id",515), ("name", "Aishu"), ("marks", 85)]
result = dict(student)
result1 = list(student)
print(result)
print(result1)
#filter
num2 = [11,22,33,44,55,66,77,88,99]
res = filter(lambda x: x % 2 != 0, num2)
print("using filter:",list(res))

