import unittest

from deck import Deck
from card import Card
from magic_strings import *

class TestDeck(unittest.TestCase):

	def test_deck_initialization_is_as_expected(self):
		expected_deck = [Card(seven, clubs), Card(seven, diamonds), Card(seven, hearts), Card(seven, spades),
						Card(eight, clubs), Card(eight, diamonds), Card(eight, hearts), Card(eight, spades),
						Card(nine, clubs), Card(nine, diamonds), Card(nine, hearts), Card(nine, spades),
						Card(ten, clubs), Card(ten, diamonds), Card(ten, hearts), Card(ten, spades),
						Card(jack, clubs), Card(jack, diamonds), Card(jack, hearts), Card(jack, spades),
						Card(queen, clubs), Card(queen, diamonds), Card(queen, hearts), Card(queen, spades),
						Card(king, clubs), Card(king, diamonds), Card(king, hearts), Card(king, spades),
						Card(ace, clubs), Card(ace, diamonds), Card(ace, hearts), Card(ace, spades)]
		
		test_deck = Deck()

		self.assertEqual(test_deck.get_cards(),expected_deck)

	def test_deck_str_is_as_expected(self):
		expected_string = '7c 7d 7h 7s 8c 8d 8h 8s 9c 9d 9h 9s 10c 10d 10h 10s Jc Jd Jh Js Qc Qd Qh Qs Kc Kd Kh Ks Ac Ad Ah As'

		test_deck = Deck()

		self.assertEqual(str(test_deck),expected_string)

	def test_deck_deal_method_returns_first_8_cards_from_deck_and_then_puts_them_in_its_end(self):
		test_deck = Deck()
		
		expected_list_of_cards = test_deck.get_cards()[:8]
		
		first_eight_cards_from_deck = test_deck.deal()

		self.assertEqual(first_eight_cards_from_deck,expected_list_of_cards)

if __name__ == '__main__':
	unittest.main()