import unittest

def check_odd_or_even(num):
    if (num % 2) == 0:
        return "Even"
    else:
        return "Odd"

class TestOddEvenCheck(unittest.TestCase):

    def test_even_number(self):
        num = 6
        print(num)
        self.assertEqual(check_odd_or_even(num), "Even")

    def test_odd_number(self):
        num = 7
        print(num)
        self.assertEqual(check_odd_or_even(num), "Odd")

    def test_zero(self):
        num = 0
        self.assertEqual(check_odd_or_even(num), "Even")

    def test_negative_even_number(self):
        num = -4
        self.assertEqual(check_odd_or_even(num), "Even")

    def test_negative_odd_number(self):
        num = -5
        self.assertEqual(check_odd_or_even(num), "Odd")

if __name__ == '__main__':
    unittest.main()
