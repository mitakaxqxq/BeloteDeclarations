from player import Player

class Team:

	def __init__(self,name,players):
		self.validate_players(name,players)

		self.__name = name
		self.__players = players

	def get_name(self):
		return self.__name

	def get_players(self):
		return self.__players

	def get_player1(self):
		return self.__players[0]

	def get_player2(self):
		return self.__players[1]

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

	def get_highest_announcement(self):
		player1_announcements = self.__players[0].get_announcements_representation()
		player2_announcements = self.__players[1].get_announcements_representation()

		for announcement in player1_announcements:
			if announcement[0].get_value() == announcement[1].get_value():
				player1_announcements.remove(announcement)

		for announcement in player2_announcements:
			if announcement[0].get_value() == announcement[1].get_value():
				player2_announcements.remove(announcement)

		max_announcement = []

		if player1_announcements ==[]:
			player1_announcements.append([])

		if player2_announcements ==[]:
			player2_announcements.append([])
		

		for elem1 in player1_announcements:
			for elem2 in player2_announcements:
				if elem1 ==[] and elem2 == []:
					continue
				if len(elem2) > len(elem1):
					if len(elem2) > len(max_announcement):
						max_announcement = elem2
				elif len(elem2) < len(elem1):
					if len(elem1) > len(max_announcement):
						max_announcement = elem1
				elif elem1[-1].get_value()>elem2[-1].get_value():
					if max_announcement == []:
						max_announcement = elem1
					elif elem1[-1].get_value()>max_announcement[-1].get_value():
						max_announcement = elem1
				else:
					if max_announcement == []:
							max_announcement = elem2
					elif elem2[-1].get_value() > max_announcement[-1].get_value():
						max_announcement = elem2

		return max_announcement
