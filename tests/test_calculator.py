import unittest
from src.calculator import *




class CalculatorTest(unittest.TestCase):

    def test_sum_when_adding_numbers_should_return_expected_sum(self):
        assert sum(2, 3) == 5
        self.assertEqual(sum(-1, 1), 0)

    def test_subtract_when_subtracting_numbers_should_return_expected_difference(self):
        assert subtract(5, 3) == 2
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply_when_multiplying_numbers_should_return_expected_product(self):
        assert multiply(2, 3) == 6
        self.assertEqual(multiply(-1, 5), -5)

    def test_divide_when_dividing_numbers_should_return_expected_quotient(self):
        assert divide(6, 3) == 2
        self.assertEqual(divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            divide(5, 0)