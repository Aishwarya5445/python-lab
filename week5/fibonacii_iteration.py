def fibonacci_iter(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci_iter(n)