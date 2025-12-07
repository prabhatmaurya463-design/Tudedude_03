def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is: {result}")
