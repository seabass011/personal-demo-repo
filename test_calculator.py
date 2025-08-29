"""
Comprehensive tests for the calculator module.
These tests will initially fail due to intentional bugs in the code.
"""

import pytest
from calculator import (
    add, subtract, multiply, divide, power,
    square_root, factorial, fibonacci, average
)

class TestBasicArithmetic:
    """Test basic arithmetic operations."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5
        assert add(-10, 15) == 5

    def test_subtract(self):
        assert subtract(10, 3) == 7
        assert subtract(5, 10) == -5

    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 100) == 0

class TestDivision:
    """Test division operations."""

    def test_divide_normal(self):
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_by_zero(self):
        """This should fail initially due to missing error handling."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

class TestPower:
    """Test power operations."""

    def test_power_positive(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        """This should fail initially due to missing error handling."""
        assert power(2, -1) == 0.5

    def test_power_large_exponent(self):
        """This might cause overflow issues."""
        result = power(2, 100)
        assert result == 2**100

class TestSquareRoot:
    """Test square root operations."""

    def test_square_root_positive(self):
        assert abs(square_root(9) - 3) < 0.0001
        assert abs(square_root(16) - 4) < 0.0001

    def test_square_root_zero(self):
        assert square_root(0) == 0

    def test_square_root_negative(self):
        """This should fail initially due to missing error handling."""
        with pytest.raises(ValueError):
            square_root(-4)

class TestFactorial:
    """Test factorial operations."""

    def test_factorial_positive(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120

    def test_factorial_negative(self):
        """This should fail initially due to missing error handling."""
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_non_integer(self):
        """This should fail initially due to missing error handling."""
        with pytest.raises(ValueError):
            factorial(2.5)

class TestFibonacci:
    """Test Fibonacci sequence."""

    def test_fibonacci_base_cases(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_sequence(self):
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8

    def test_fibonacci_negative(self):
        """This should fail initially due to missing error handling."""
        # Note: This might cause infinite recursion
        fibonacci(-1)

class TestAverage:
    """Test average calculations."""

    def test_average_normal(self):
        assert average([1, 2, 3, 4, 5]) == 3
        assert average([10, 20, 30]) == 20

    def test_average_single_element(self):
        assert average([5]) == 5

    def test_average_empty_list(self):
        """This should fail initially due to missing error handling."""
        with pytest.raises(ZeroDivisionError):
            average([])

class TestEdgeCases:
    """Test various edge cases."""

    def test_large_numbers(self):
        assert add(1000000, 2000000) == 3000000

    def test_floating_point(self):
        assert abs(add(1.5, 2.5) - 4.0) < 0.0001

    def test_mixed_types(self):
        """Test with different number types."""
        assert add(1, 2.5) == 3.5
