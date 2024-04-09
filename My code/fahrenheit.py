import unittest

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

class TestTemperatureConversion(unittest.TestCase):

    def test_positive_celsius(self):
        celsius = 37.5
        expected_fahrenheit = 99.5
        self.assertAlmostEqual(celsius_to_fahrenheit(celsius), expected_fahrenheit, places=1)

    def test_negative_celsius(self):
        celsius = -10
        expected_fahrenheit = 14
        self.assertAlmostEqual(celsius_to_fahrenheit(celsius), expected_fahrenheit, places=1)

    def test_zero_celsius(self):
        celsius = 0
        expected_fahrenheit = 32
        self.assertAlmostEqual(celsius_to_fahrenheit(celsius), expected_fahrenheit, places=1)

    def test_decimal_celsius(self):
        celsius = 20.5
        expected_fahrenheit = 68.9
        self.assertAlmostEqual(celsius_to_fahrenheit(celsius), expected_fahrenheit, places=1)

if __name__ == '__main__':
    unittest.main()
