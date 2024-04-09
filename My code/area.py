import unittest

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

class TestTriangleArea(unittest.TestCase):

    def test_positive_sides(self):
        a = 5
        b = 6
        c = 7
        expected_result = 14.7  # Rounded to one decimal place
        print(expected_result)
        self.assertAlmostEqual(calculate_triangle_area(a, b, c), expected_result, places=1)

if __name__ == '__main__':
    unittest.main()
