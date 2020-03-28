import unittest

from player import Player
from team import Team

class TestTeam(unittest.TestCase):
	def test_raises_exception_when_team_name_is_not_string(self):

		exc = None

		try:
			team = Team(123,[])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Team name must be of string type!')

	def test_raises_exception_when_we_do_not_add_list_of_players(self):

		exc = None

		try:
			team = Team('Team1',[1,2])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'You have to add list of Players!')

	def test_raises_exception_when_we_do_not_add_list_of_two_players(self):

		exc = None

		try:
			team = Team('Team1',[Player('Ivan'),Player('Petar'),Player('Georgi')])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'You have to add exactly two players!')

	def test_raises_exception_when_we_add_list_of_two_players_with_the_same_name(self):

		exc = None

		try:
			team = Team('Team1',[Player('Ivan'),Player('Ivan')])
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Players names must be different!')


if __name__ == '__main__':
	unittest.main()