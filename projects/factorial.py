def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a non-negative integer: "))

result = factorial(num)

print("Factorial of {num} is result {result}")