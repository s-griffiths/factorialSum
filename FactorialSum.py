# FactorialSum.py
# User enters a whole number between 1 and 20, the program outputs
# the sum of the factorials of all the numbers from 1 to the user's
# input number.


# Function that returns the factorial of a number supplied as an argument.
def factorial(number):
    factorial = 1
    for i in range(1,number + 1):
        factorial *= i
    return factorial


# Prompts the user for a whole number between 1 and 20.
# If the number does not fall in the range (1-20) the user will receive the prompt
# until an appropriate number is provided.
number = int(input("Enter a whole number between 1 and 20: "))
while number < 1 or number > 20:
    number = int(input("The number MUST be between 1 and 20: "))

# Sets the variable that will be used to sum the factorials to 0
factorialSum = 0

# Steps through the factorials of 1 to the user's number, adding them together.
for i in range(1, number + 1):
    factorialSum += factorial(i)

# Prints the sum of the factorials of all the numbers from 1 to the user's number
print("The sum of the factorials of all the numbers from 1 to", number, "is", str(factorialSum) + ".")
