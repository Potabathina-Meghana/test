import unittest
import cmath

def quadratic_solver(a, b, c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    
    # find solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    
    return sol1, sol2

class TestQuadraticSolver(unittest.TestCase):

    def test_real_roots(self):
        a = 1
        b = 5
        c = 6
        expected_roots = (-3+0j), (-2+0j)
        print(expected_roots)
        self.assertEqual(quadratic_solver(a, b, c), expected_roots)

    def test_complex_roots(self):
        a = 1
        b = 2
        c = 5
        expected_roots = (-1-2j), (-1+2j)  # Corrected order of roots
        self.assertEqual(quadratic_solver(a, b, c), expected_roots)

if __name__ == '__main__':
    unittest.main()
