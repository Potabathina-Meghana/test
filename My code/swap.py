import unittest

def swap_variables(x, y):
    # create a temporary variable and swap the values
    temp = x
    x = y
    y = temp
    return x, y

class TestSwapVariables(unittest.TestCase):

    def test_swap_integers(self):
        x = 5
        y = 10
        expected_result = (10, 5)
        self.assertEqual(swap_variables(x, y), expected_result)

    def test_swap_strings(self):
        x = "hello"
        y = "world"
        expected_result = ("world", "hello")
        self.assertEqual(swap_variables(x, y), expected_result)

    def test_swap_mixed_types(self):
        x = 5
        y = "world"
        expected_result = ("world", 5)
        self.assertEqual(swap_variables(x, y), expected_result)

if __name__ == '__main__':
    unittest.main()
