def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

num = int(input("Enter a number: "))

if is_prime_recursive(num):
    print(" Prime number")
else:
    print(" not a  prime number")

    
    