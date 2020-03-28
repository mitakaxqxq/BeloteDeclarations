from player import Player

class Team:

	def __init__(self,name,players):
		self.validate_players(name,players)

		self.__name = name
		self.__players = players

	@staticmethod
	def validate_players(name,players):
		if not isinstance(name,str):
			raise TypeError('Team name must be of string type!')
		
		for player in players:
				if not isinstance(player,Player):
					raise TypeError('You have to add list of Players!')
		
		if len(players) != 2:
			raise TypeError('You have to add exactly two players!')

		if players[0].get_name() == players[1].get_name():
			raise TypeError('Players names must be different!')