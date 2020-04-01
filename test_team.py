import unittest

from player import Player
from team import Team
from card import Card
from magic_strings import *

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

	def test_if_get_name_returns_correctly_name(self):

		team = Team('Team1',[Player('Ivan'),Player('Petar')])

		expected = 'Team1'

		result = team.get_name()

		self.assertTrue(expected == result,'Names are equal')

	def test_if_get_players_returns_correctly_players(self):

		team = Team('Team1',[Player('Ivan'),Player('Petar')])

		expected = [Player('Ivan'),Player('Petar')]

		result = team.get_players()

		self.assertTrue(expected == result,'Lists of players are equal')

	def test_if_get_player1_returns_correctly_player1(self):

		team = Team('Team1',[Player('Ivan'),Player('Petar')])

		expected = Player('Ivan')

		result = team.get_player1()

		self.assertTrue(expected == result,'Players are equal')

	def test_if_get_player2_returns_correctly_player2(self):

		team = Team('Team1',[Player('Ivan'),Player('Petar')])

		expected = Player('Petar')

		result = team.get_player2()

		self.assertTrue(expected == result,'Players are equal')


	def test_if_get_highest_announcement_returns_correct_list(self):

		player1 = Player("Ivan")
		player1.set_hand([Card(jack,diamonds),Card(king,diamonds),Card(nine,diamonds),Card(queen,diamonds),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

		player2 = Player("Petar")
		player2.set_hand([Card(jack,diamonds),Card(king,diamonds),Card(nine,hearts),Card(queen,diamonds),Card(ten,hearts),Card(eight,hearts),Card(ten,diamonds),Card(ten,clubs)])

		team = Team('Team1',[player1,player2])

		result = team.get_highest_announcement()
		expected = [Card(jack,diamonds),Card(king,diamonds),Card(queen,diamonds),Card(ten,diamonds)]

if __name__ == '__main__':
	unittest.main()