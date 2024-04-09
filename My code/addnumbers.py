import unittest

class TestAddition(unittest.TestCase):
    def test_positive_numbers(self):
        num1 = 1.5
        num2 = 6.3
        expected_sum = 7.8
        print(expected_sum)
        self.assertEqual(num1 + num2, expected_sum)

    def test_negative_numbers(self):
        num1 = -1.5
        num2 = -6.3
        expected_sum = -7.8
        print(expected_sum)
        self.assertEqual(num1 + num2, expected_sum)

    def test_mixed_numbers(self):
        num1 = -1.5
        num2 = 6.3
        expected_sum = 4.8
        print(expected_sum)
        self.assertEqual(num1 + num2, expected_sum)

    def test_zero(self):
        num1 = 0
        num2 = 0
        expected_sum = 0
        print(expected_sum)
        self.assertEqual(num1 + num2, expected_sum)

    def test_decimal_numbers(self):
        num1 = 1.5
        num2 = 2.5
        expected_sum = 4.0
        print(expected_sum)
        self.assertEqual(num1 + num2, expected_sum)

if __name__ == '__main__':
    unittest.main()
