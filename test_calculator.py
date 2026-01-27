"""
Functional tests for the Calculator class.
"""
import pytest
from calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition functionality."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(-5, -3) == -8
    
    def test_subtraction(self):
        """Test subtraction functionality."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10, 10) == 0
        assert self.calc.subtract(-5, -3) == -2
    
    def test_multiplication(self):
        """Test multiplication functionality."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(-2, -3) == 6
    
    def test_division(self):
        """Test division functionality."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(9, 3) == 3
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(-10, 2) == -5
    
    def test_division_by_zero(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power functionality."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(10, 1) == 10
        assert self.calc.power(2, -1) == 0.5
