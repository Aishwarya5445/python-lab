s = input("Enter a string: ")

# Illustrating 'in' operator (checking uppercase 'A')
if 'A' in s:
    print("'A' is present in the string")
else:
    print("'A' is not present in the string")

# Counting uppercase characters
count = 0
for ch in s:
    if ch.isupper():
        count += 1

print("Number of uppercase characters:", count)
