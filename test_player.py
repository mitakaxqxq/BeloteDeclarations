import unittest

from card import Card
from player import Player

class TestPlayer(unittest.TestCase):

    def test_raise_exception_when_player_name_is_not_of_string_type(self):

        exc = None

        try:
            player = Player(123)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Player name must be of string type!')

    def test_raises_exception_when_a_player_has_different_number_of_eight_cards_in_hand(self):

        list_of_cards = [Card('7', 'clubs'), Card('7', 'diamonds'), Card('7', 'hearts'), Card('7', 'spades'),
                        Card('8', 'clubs'), Card('8', 'diamonds'), Card('8', 'hearts')]

        player = Player('Ivan')

        exc = None

        try:
            player.set_hand(list_of_cards)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'You must add exactly eight cards!')

    def test_when_a_player_name_is_equal_to_another_player(self):

        player1 = Player('Ivan')
        player2 = Player('Ivan')

        self.assertTrue(player1 == player2, 'Players are equal')

    def test_if_get_name_method_returns_correctly_name_of_player(self):

        player = Player('Ivan')

        expected = 'Ivan'
        result = player.get_name()

        self.assertTrue(expected == result, 'Names are equal')


    def test_if_get_hand_method_returns_correctly_hand_of_player(self):

        list_of_cards = [Card('7', 'clubs'), Card('7', 'diamonds'), Card('7', 'hearts'), Card('7', 'spades'),
                        Card('8', 'clubs'), Card('8', 'diamonds'), Card('8', 'hearts'),Card('8', 'spades')]
        
        player = Player('Ivan')
        player.set_hand(list_of_cards)

        expected = [Card('7', 'clubs'), Card('7', 'diamonds'), Card('7', 'hearts'), Card('7', 'spades'),
                        Card('8', 'clubs'), Card('8', 'hearts'), Card('8', 'diamonds'),Card('8', 'spades')]

        self.assertTrue(expected == player.get_hand(), 'Lists are equal')

    def test_if_get_announcements_representation_returns_correctly(self):

        player = Player("Ivan")
        player.set_hand([Card('J','diamonds'),Card('K','diamonds'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])
        
        result = player.get_announcements_representation()

        expected = [[Card('10','clubs'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades')]]

        self.assertEqual(result,expected)

    def test_if_get_announced_announcements_returns_correctly(self):

        player = Player("Ivan")
        player.set_hand([Card('J','diamonds'),Card('K','diamonds'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])
        
        result = player.get_announced_announcements()

        expected = ['carre']

        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()