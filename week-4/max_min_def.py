def find_min_max(a, b, c):
  maximum = max(a, b, c)
  minimum = min(a, b, c)
  return maximum,minimum  

num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
num3 = int(input("enter 3rd number:"))
min_num, max_num = find_min_max(num1, num2, num3)

print(f"The three numbers are: {num1}, {num2}, and {num3}")
print(f"The minimum number is: {min_num}")
print(f"The maximum number is: {max_num}")