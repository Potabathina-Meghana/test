import unittest

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

class TestPrimeNumber(unittest.TestCase):

    def test_prime_number(self):
        prime_num = 29
        self.assertTrue(is_prime(prime_num))

    def test_non_prime_number(self):
        non_prime_num = 15
        self.assertFalse(is_prime(non_prime_num))

    def test_negative_number(self):
        negative_num = -7
        self.assertFalse(is_prime(negative_num))

    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_one(self):
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()
