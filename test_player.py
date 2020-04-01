import unittest

from card import Card
from player import Player
from magic_strings import *

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

        list_of_cards = [Card(seven, clubs), Card(seven, diamonds), Card(seven, hearts), Card(seven, spades),
                        Card(eight, clubs), Card(eight, diamonds), Card(eight, hearts)]

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

        list_of_cards = [Card(seven, clubs), Card(seven, diamonds), Card(seven, hearts), Card(seven, spades),
                        Card(eight, clubs), Card(eight, diamonds), Card(eight, hearts),Card(eight, spades)]
        
        player = Player('Ivan')
        player.set_hand(list_of_cards)

        expected = [Card(seven, clubs), Card(seven, diamonds), Card(seven, hearts), Card(seven, spades),
                        Card(eight, clubs), Card(eight, diamonds), Card(eight, hearts),Card(eight, spades)]

        self.assertTrue(expected == player.get_hand(), 'Lists are equal')

    def test_if_get_announcements_representation_returns_correctly(self):

        player = Player("Ivan")
        player.set_hand([Card(jack,diamonds),Card(king,diamonds),Card(nine,diamonds),Card(queen,diamonds),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])
        
        result = player.get_announcements_representation()

        expected = [[Card(ten,clubs),Card(ten,diamonds),Card(ten,hearts),Card(ten,spades)]]

        self.assertEqual(result,expected)

    def test_if_get_announced_announcements_returns_correctly(self):

        player = Player("Ivan")
        player.set_hand([Card(jack,diamonds),Card(king,diamonds),Card(nine,diamonds),Card(queen,diamonds),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])
        
        result = player.get_announced_announcements()

        expected = [carre]

        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()