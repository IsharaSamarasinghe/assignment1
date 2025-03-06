# Simple Calculator in Python

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display results
print("\nResults:")
print(f"Addition: {sum_result}")
print(f"Subtraction: {difference}")
print(f"Multiplication: {product}")
print(f"Division: {quotient}")
