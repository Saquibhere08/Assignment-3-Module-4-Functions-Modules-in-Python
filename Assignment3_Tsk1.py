'''
Write a Python program that:
1. Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2. Returns the calculated factorial.
3. Calls the function with a sample number and prints the output.
'''
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


sample_number = int(input("Enter a Number: "))
output = factorial(sample_number)
print(f"Factorial of {sample_number} is {output}")
