"""
Simple calculator module for basic arithmetic operations.
"""


class Calculator:
    """A simple calculator class with basic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Calculate base raised to exponent."""
        return base ** exponent


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    print("Calculator Demo")
    print("=" * 40)
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 5 = {calc.divide(20, 5)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")


if __name__ == "__main__":
    main()
