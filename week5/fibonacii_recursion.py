def fibonacci_rec(n):
    if n <= 1:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

n = int(input("Enter number of terms: "))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci_rec(i), end=" ")