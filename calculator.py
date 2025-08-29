"""
Simple calculator module for Nova CI-Rescue demo.
This module contains intentional bugs for testing purposes.
"""

def add(a, b):
    """Add two numbers together."""
    # BUG: Incorrect addition for negative numbers
    if a < 0 or b < 0:
        return a - b  # This is wrong!
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    # BUG: Incorrect multiplication when one number is zero
    if a == 0 or b == 0:
        return 1  # This is wrong!
    return a * b

def divide(a, b):
    """Divide a by b."""
    # BUG: No division by zero check
    return a / b

def power(a, b):
    """Calculate a raised to the power of b."""
    # BUG: No check for negative powers or large exponents
    # BUG: Wrong calculation for power of 0
    if a == 0:
        return 1  # This is wrong! 0^anything should be 0 (except 0^0)
    return a ** b

def square_root(a):
    """Calculate the square root of a."""
    # BUG: No check for negative numbers
    return a ** 0.5

def factorial(n):
    """Calculate the factorial of n."""
    # BUG: No check for negative numbers or non-integers
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    # BUG: No check for negative numbers
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def average(numbers):
    """Calculate the average of a list of numbers."""
    # BUG: No check for empty list
    return sum(numbers) / len(numbers)
