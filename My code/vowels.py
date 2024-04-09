import unittest

def count_vowels(ip_str):
    vowels = 'aeiou'
    ip_str = ip_str.casefold()
    count = {}.fromkeys(vowels, 0)
    for char in ip_str:
        if char in count:
            count[char] += 1
    return count

class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels('Hello, have you tried our tutorial section yet?'), {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3})

    def test_count_vowels_empty_string(self):
        self.assertEqual(count_vowels(''), {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test_count_vowels_no_vowels(self):
        self.assertEqual(count_vowels('rhythms'), {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test_count_vowels_all_vowels(self):
        self.assertEqual(count_vowels('aeiou'), {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})
        # Print the count of vowels after running the tests

    print(count_vowels('Hello, have you tried our tutorial section yet?'))


if __name__ == '__main__':
    unittest.main()
    
    