import unittest

def find_largest_number(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3

class TestLargestNumber(unittest.TestCase):

    def test_first_number_largest(self):
        num1 = 15
        num2 = 10
        num3 = 12
        self.assertEqual(find_largest_number(num1, num2, num3), num1)

    def test_second_number_largest(self):
        num1 = 8
        num2 = 20
        num3 = 15
        self.assertEqual(find_largest_number(num1, num2, num3), num2)

    def test_third_number_largest(self):
        num1 = 7
        num2 = 9
        num3 = 25
        self.assertEqual(find_largest_number(num1, num2, num3), num3)

    def test_equal_numbers(self):
        num1 = 10
        num2 = 10
        num3 = 10
        self.assertEqual(find_largest_number(num1, num2, num3), num1)

if __name__ == '__main__':
    unittest.main()
