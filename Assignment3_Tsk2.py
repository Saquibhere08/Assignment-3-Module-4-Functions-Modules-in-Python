'''

Problem Statement: Write a Python program that:
1. Asks the user for a number as input.
2. Uses the math module to calculate the:
o Square root of the number
o Natural logarithm (log base e) of the number
o Sine of the number (in radians)
3.Displays the calculated results.
'''
import math


number = float(input("Enter a number: "))

# results using math module
sqrt_value = math.sqrt(number)
log_value = math.log(number)
sine_value = math.sin(number)


print(f"Square root of {number} is {sqrt_value}")
print(f"Natural logarithm of {number} is {log_value}")
print(f"Sine of {number} (in radians) is {sine_value}")
