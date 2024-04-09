import unittest

def sort_words_alphabetically(input_str):
    words = [word.lower() for word in input_str.split()]
    words.sort()
    return words

class TestSortWordsAlphabetically(unittest.TestCase):

    def test_sort_words(self):
        input_str = "Hello this Is an Example With cased letters"
        expected_output = ['an', 'cased', 'example', 'hello', 'is', 'letters', 'this', 'with']
        self.assertEqual(sort_words_alphabetically(input_str), expected_output)

    def test_sort_words_empty_string(self):
        input_str = ""
        expected_output = []
        self.assertEqual(sort_words_alphabetically(input_str), expected_output)

    def test_sort_words_single_word(self):
        input_str = "Hello"
        expected_output = ['hello']
        self.assertEqual(sort_words_alphabetically(input_str), expected_output)

    def test_sort_words_with_punctuation(self):
        input_str = "Hello, this Is an Example With cased letters."
        expected_output = ['an', 'cased', 'example', 'hello,', 'is', 'letters.', 'this', 'with']
        self.assertEqual(sort_words_alphabetically(input_str), expected_output)

if __name__ == '__main__':
    print("Sorted words:")
    my_str = "Hello this Is an Example With cased letters"
    sorted_words = sort_words_alphabetically(my_str)
    for word in sorted_words:
        print(word)
    
    print("\nRunning unit tests...")
    unittest.main(argv=[''], exit=False)
