import random
from deck import Deck 
from team import Team

class Game:

	def __init__(self,team1,team2):
		self.validate_values(team1,team2)

		self.__team1 = team1
		self.__team2 = team2

		self.__team1_score = 0
		self.__team1_score = 0

		self.__deck = Deck()
		
		self.__order = [self.__team1.get_player1(),self.__team2.get_player1(),self.__team1.get_player2(),self.__team2.get_player2()]

	def get_order(self):
		return self.__order

	def rotate_players(self):
		first_player = self.__order[0]
		self.__order.remove(first_player)
		self.__order.append(first_player)

	def select_announcement(self):
		announcements = ['clubs','diamonds','hearts','spades','no trumps','all trumps']
		index = random.randint(0,5)
		return announcements[index]

	def deal_cards(self):
		for player in self.__order:
			player.set_hand(self.__deck.deal())

	def play(self): #to do
		pass

	@staticmethod
	def validate_values(team1,team2):
		if not isinstance(team1,Team):
			raise TypeError('Invalid first argument - it must be of Team type')
		elif not isinstance(team2,Team):
			raise TypeError('Invalid second argument - it must be of Team type')
		elif team1.get_name() == team2.get_name():
			raise TypeError('Team names must be different!')

		team1_players = team1.get_players()
		team2_players = team2.get_players()
		
		for player in team1_players:
			if player in team2_players:
				raise ValueError('Player can not be in two teams!')