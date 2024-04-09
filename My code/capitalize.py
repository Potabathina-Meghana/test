import unittest

def capitalize_first_letter(string):
    return string[0].upper() + string[1:]

class TestCapitalizeFirstLetter(unittest.TestCase):

    def test_capitalize_first_letter(self):
        my_string = "programiz is Lit"
        expected_result = "Programiz is Lit"
        result = capitalize_first_letter(my_string)
        print(result)  # Print the result inside the test method
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
   unittest.main()
