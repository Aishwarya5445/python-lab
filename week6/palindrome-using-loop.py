s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
