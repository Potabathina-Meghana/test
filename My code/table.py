# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

import unittest

def generate_multiplication_table(num):
    table = []
    for i in range(1, 11):
        table.append((num, i, num*i))
    return table

class TestMultiplicationTable(unittest.TestCase):
    
    def test_multiplication_table_for_12(self):
        num = 12
        expected_table = [(12, 1, 12), (12, 2, 24), (12, 3, 36), (12, 4, 48), (12, 5, 60), (12, 6, 72), (12, 7, 84), (12, 8, 96), (12, 9, 108), (12, 10, 120)]
        self.assertEqual(generate_multiplication_table(num), expected_table)
    
    def test_multiplication_table_for_5(self):
        num = 5
        expected_table = [(5, 1, 5), (5, 2, 10), (5, 3, 15), (5, 4, 20), (5, 5, 25), (5, 6, 30), (5, 7, 35), (5, 8, 40), (5, 9, 45), (5, 10, 50)]
        self.assertEqual(generate_multiplication_table(num), expected_table)
    
    def test_multiplication_table_for_0(self):
        num = 0
        expected_table = [(0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (0, 5, 0), (0, 6, 0), (0, 7, 0), (0, 8, 0), (0, 9, 0), (0, 10, 0)]
        self.assertEqual(generate_multiplication_table(num), expected_table)

if __name__ == '__main__':
    unittest.main()
