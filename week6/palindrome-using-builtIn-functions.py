s = input("Enter a string: ")

rev = "".join(reversed(s))

if s == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
