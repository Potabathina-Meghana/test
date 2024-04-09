import unittest

def calculate_square_root(num):
    if num < 0:
        raise ValueError("Square root of a negative number is not defined.")
    return num ** 0.5

class TestSquareRoot(unittest.TestCase):

    def test_positive_number(self):
        num = 9
        expected_result = 3.0
        print(expected_result)
        self.assertAlmostEqual(calculate_square_root(num), expected_result, places=2)

    def test_negative_number(self):
        num = -9
        with self.assertRaises(ValueError):
            calculate_square_root(num)

    def test_zero(self):
        num = 0
        expected_result = 0.0
        self.assertAlmostEqual(calculate_square_root(num), expected_result, places=2)

    def test_decimal_number(self):
        num = 2.25
        expected_result = 1.5
        self.assertAlmostEqual(calculate_square_root(num), expected_result, places=2)

if __name__ == '__main__':
    unittest.main()
