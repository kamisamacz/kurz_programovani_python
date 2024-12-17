class Number:
    def __init__(self, value):
        """Initialize the Number class with a numeric value."""
        if not isinstance(value, int):
            raise ValueError("Only integers are allowed.")
        self.value = value

    def set_value(self, value):
        """Set a new value for the number."""
        if not isinstance(value, int):
            raise ValueError("Only integers are allowed.")
        self.value = value

    def get_value(self):
        """Get the current value of the number."""
        return self.value

    def to_octal(self):
        """Convert the number to its octal representation."""
        return oct(self.value)

    def to_hexadecimal(self):
        """Convert the number to its hexadecimal representation."""
        return hex(self.value)

    def to_binary(self):
        """Convert the number to its binary representation."""
        return bin(self.value)


# Unit tests
import unittest


class TestNumber(unittest.TestCase):
    def test_initialization(self):
        num = Number(10)
        self.assertEqual(num.get_value(), 10)

    def test_set_value(self):
        num = Number(10)
        num.set_value(20)
        self.assertEqual(num.get_value(), 20)

    def test_invalid_initialization(self):

