"""
Unit tests for the calculator library
Added addition
Added subtraction
Added multiplication
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
        
    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
