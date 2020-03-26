import unittest

from deck import Deck
from card import Card

class TestDeckInitialization(unittest.TestCase):

	def test_deck_initialization_is_as_expected(self):
		expected_deck = [Card('7', 'clubs'), Card('7', 'diamonds'), Card('7', 'hearts'), Card('7', 'spades'),
						Card('8', 'clubs'), Card('8', 'diamonds'), Card('8', 'hearts'), Card('8', 'spades'),
						Card('9', 'clubs'), Card('9', 'diamonds'), Card('9', 'hearts'), Card('9', 'spades'),
						Card('10', 'clubs'), Card('10', 'diamonds'), Card('10', 'hearts'), Card('10', 'spades'),
						Card('J', 'clubs'), Card('J', 'diamonds'), Card('J', 'hearts'), Card('J', 'spades'),
						Card('Q', 'clubs'), Card('Q', 'diamonds'), Card('Q', 'hearts'), Card('Q', 'spades'),
						Card('K', 'clubs'), Card('K', 'diamonds'), Card('K', 'hearts'), Card('K', 'spades'),
						Card('A', 'clubs'), Card('A', 'diamonds'), Card('A', 'hearts'), Card('A', 'spades')]
		
		test_deck = Deck()

		self.assertEqual(getattr(test_deck,'cards'),expected_deck)

class TestDeckStrRepresentation(unittest.TestCase):

	def test_deck_str_is_as_expected(self):
		expected_string = '7c 7d 7h 7s 8c 8d 8h 8s 9c 9d 9h 9s 10c 10d 10h 10s Jc Jd Jh Js Qc Qd Qh Qs Kc Kd Kh Ks Ac Ad Ah As'

		test_deck = Deck()

		self.assertEqual(str(test_deck),expected_string)

class TestDeckDealingOfCards(unittest.TestCase):

	def test_deck_deal_method_returns_first_8_cards_from_deck_and_then_puts_them_in_its_end(self):
		test_deck = Deck()
		
		expected_list_of_cards = getattr(test_deck,'cards')[:8]
		
		first_eight_cards_from_deck = test_deck.deal()

		self.assertEqual(first_eight_cards_from_deck,expected_list_of_cards)

if __name__ == '__main__':
	unittest.main()