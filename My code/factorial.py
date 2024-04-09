import unittest

def factorial(num):
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

class TestFactorial(unittest.TestCase):
    
    def test_factorial_of_positive_number(self):
        num = 7
        expected_result = 5040
        self.assertEqual(factorial(num), expected_result)
    
    def test_factorial_of_zero(self):
        num = 0
        expected_result = 1
        self.assertEqual(factorial(num), expected_result)
    
    def test_factorial_of_negative_number(self):
        num = -5
        self.assertIsNone(factorial(num))

if __name__ == '__main__':
    unittest.main()
