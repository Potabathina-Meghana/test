import unittest
import itertools
import random
import io
import sys

def shuffle_deck():
    # make a deck of cards
    deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
    # shuffle the cards
    random.shuffle(deck)
    return deck

def draw_cards(deck, num_cards=5):
    return deck[:num_cards]

class TestShuffleDeck(unittest.TestCase):
    def test_deck_length(self):
        deck = shuffle_deck()
        self.assertEqual(len(deck), 52)  # Ensure the deck has 52 cards after shuffling

    def test_drawn_cards(self):
        deck = shuffle_deck()
        drawn_cards = draw_cards(deck)
        self.assertEqual(len(drawn_cards), 5)  # Ensure 5 cards are drawn
        for card in drawn_cards:
            self.assertIn(card, deck)  # Ensure each drawn card is in the original deck

    def test_unique_cards(self):
        deck = shuffle_deck()
        self.assertEqual(len(set(deck)), 52)  # Ensure all cards are unique after shuffling

    def test_print_output(self):
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Run the main program logic
        deck = shuffle_deck()
        print("You got:")
        for i in range(5):
            print(deck[i][0], "of", deck[i][1])

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the captured output
        output = captured_output.getvalue()

        # Print the captured output
        print("Output:")
        print(output)

if __name__ == '__main__':
    unittest.main()
