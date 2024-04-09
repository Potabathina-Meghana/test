import unittest

def check_number_sign(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"

class TestNumberSignCheck(unittest.TestCase):

    def test_positive_number(self):
        num = 6
        self.assertEqual(check_number_sign(num), "Positive")

    def test_negative_number(self):
        num = -7
        self.assertEqual(check_number_sign(num), "Negative")
        print(check_number_sign(num))

    def test_zero(self):
        num = 0
        self.assertEqual(check_number_sign(num), "Zero")

    def test_decimal_positive_number(self):
        num = 3.14
        self.assertEqual(check_number_sign(num), "Positive")

    def test_decimal_negative_number(self):
        num = -2.5
        self.assertEqual(check_number_sign(num), "Negative")

if __name__ == '__main__':
    unittest.main()
