s = input("Enter a string: ")

# Illustrating 'in' operator
if 'a' in s:
    print("'a' is present in the string")
else:
    print("'a' is not present in the string")

# Counting lowercase characters
count = 0
for ch in s:
    if ch.islower():
        count += 1

print("Number of lowercase characters:", count)
