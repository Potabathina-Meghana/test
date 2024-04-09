import unittest

def convert_kilometers_to_miles(kilometers):
    conv_fac = 0.621371
    miles = kilometers * conv_fac
    return miles

class TestKilometersToMilesConversion(unittest.TestCase):

    def test_positive_kilometers(self):
        kilometers = 10
        expected_miles = 6.21371
        self.assertAlmostEqual(convert_kilometers_to_miles(kilometers), expected_miles, places=5)

    def test_negative_kilometers(self):
        kilometers = -10
        expected_miles = -6.21371
        self.assertAlmostEqual(convert_kilometers_to_miles(kilometers), expected_miles, places=5)

    def test_zero_kilometers(self):
        kilometers = 0
        expected_miles = 0
        self.assertAlmostEqual(convert_kilometers_to_miles(kilometers), expected_miles, places=5)

if __name__ == '__main__':
    unittest.main()
