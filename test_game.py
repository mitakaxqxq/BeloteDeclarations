import unittest

from player import Player
from team import Team
from game import Game

class TestGame(unittest.TestCase):

	def test_raises_exception_when_first_argument_is_not_of_correct_type(self):

		exc = None

		try:
			game = Game([Player('Ivan'),Player('Peter')],Team("Mecheta",[Player('Ivan'),Player('Peter')]))
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Invalid first argument - it must be of Team type')

	def test_raises_exception_when_second_argument_is_not_of_correct_type(self):

		exc = None

		try:
			game = Game(Team("Mecheta",[Player('Ivan'),Player('Peter')]),[Player('Ivan'),Player('Peter')])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Invalid second argument - it must be of Team type')

	def test_raises_exception_when_team_names_are_equal(self):

		exc = None

		try:
			game = Game(Team("Mecheta",[Player('Ivan'),Player('Peter')]),Team("Mecheta",[Player('Ivan'),Player('Peter')]))
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Team names must be different!')

	def test_raises_exception_when_both_teams_have_the_same_player(self):

		exc = None

		try:
			game = Game(Team("Mecheta",[Player('Ivan'),Player('Peter')]),Team("Kotenca",[Player('Ivan'),Player('Gosho')]))
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Player can not be in two teams!')

	def test_if_get_order_returns_the_players_in_desired_order_when_initializiting_game(self):

		game = Game(Team("Mecheta",[Player('Ivan'),Player('Peter')]),Team("Kotenca",[Player('Kamen'),Player('Gosho')]))
		
		expected = [Player('Ivan'),Player('Kamen'),Player('Peter'),Player('Gosho')]

		result = game.get_order()

		self.assertTrue(expected == result,'Initial order of players is correct')

	def test_if_rotate_method_rotates_the_players_in_desired_order(self):

		game = Game(Team("Mecheta",[Player('Ivan'),Player('Peter')]),Team("Kotenca",[Player('Kamen'),Player('Gosho')]))
		
		expected = [Player('Kamen'),Player('Peter'),Player('Gosho'),Player('Ivan')]

		game.rotate_players()

		result = game.get_order()

		self.assertTrue(expected == result,'Rotation of players is correct')


if __name__ == '__main__':
	unittest.main()