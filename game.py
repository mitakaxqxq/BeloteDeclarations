import random
from deck import Deck 
from team import Team
import json
from magic_strings import *

class Game:

    def __init__(self,team1,team2):
        self.validate_values(team1,team2)

        self.__team1 = team1
        self.__team2 = team2

        self.__team1_score = 0
        self.__team2_score = 0

        self.__deck = Deck()
        
        self.__order = [self.__team1.get_player1(),self.__team2.get_player1(),self.__team1.get_player2(),self.__team2.get_player2()]

        self.__contract = ''

        self.game_count = 0

    def get_order(self):
        return self.__order

    def rotate_players(self):
        first_player = self.__order[0]
        
        self.__order.remove(first_player)
        
        self.__order.append(first_player)

    def select_contract(self):
        index = random.randint(0,5)
        
        self.__contract = announcements[index]

    def deal_cards(self):
        for player in self.__order:
            player.set_hand(self.__deck.deal())

    def initialize_file_with_results(self):
        with open("results.txt","a+") as f:
            name_of_first_team=self.__team1.get_name()
            f.write("       ")
            f.write(name_of_first_team)
            f.write("               |               ")
            name_of_second_team=self.__team2.get_name()
            f.write("")
            f.write(name_of_second_team)
            f.write("     \n")
            f.write("============================================")
            f.write("     \n")

    def write_team_scores(self,score1,score2):

        with open("results.txt","a+") as f:
            str1 = str(self.__team1_score) + ' + ' + str(score1)
            str2 = str(self.__team2_score) + ' + ' + str(score2)
            f.write(str(str1))
            f.write("               |               ")
            f.write(str(str2))
            f.write("\n")

    def write_final_score(self,score1,score2):
        with open("results.txt","a+") as f:
            str1 = str(self.__team1_score)
            str2 = str(self.__team2_score)
            f.write(str(str1))
            f.write("                   |                   ")
            f.write(str(str2))
            f.write("\n")
            f.write("============================================")
            f.write("\n")

    def check_for_belote(self):
        self.__team1.get_player1().get_belotes(self.__contract)

        self.__team1.get_player2().get_belotes(self.__contract)

        self.__team2.get_player1().get_belotes(self.__contract)
        
        self.__team2.get_player2().get_belotes(self.__contract)

    def calculate_belotes_of_teams(self,team):
        if team == 1:
            list_of_announcements = self.__team1.get_player1().get_announced_announcements()+self.__team1.get_player2().get_announced_announcements()
            list_of_announcements = [elem for elem in list_of_announcements if elem == belote]
            length = len(list_of_announcements)
            return length*20
        elif team == 2:
            list_of_announcements = self.__team2.get_player1().get_announced_announcements()+self.__team2.get_player2().get_announced_announcements()
            list_of_announcements = [elem for elem in list_of_announcements if elem == belote]
            length = len(list_of_announcements)
            return length*20

    def calculate_score_of_teams(self,team):
        if team == 1:
            list_of_announcements = self.__team1.get_player1().get_announced_announcements()+self.__team1.get_player2().get_announced_announcements()
            new_score = 0
            list_of_announcements = [x for x in list_of_announcements if x != belote and x != carre]
            for announcement in list_of_announcements:
                new_score += announcements_values[announcement]

            return new_score

        elif team == 2:
            list_of_announcements = self.__team2.get_player1().get_announced_announcements()+self.__team2.get_player2().get_announced_announcements()
            new_score = 0
            list_of_announcements = [x for x in list_of_announcements if x != belote and x != carre]
            for announcement in list_of_announcements:
                new_score += announcements_values[announcement]

            return new_score

    def check_for_carres_in_teams(self,team):
        if team == 1:
            first_list = self.__team1.get_player1().get_announcements_representation()+self.__team1.get_player2().get_announcements_representation()
            first_list = [elem for elem in first_list if len(elem) == 4]
            carre_score = 0
            for elem in first_list:
                    if elem[0].get_value() == elem[1].get_value():
                        if elem[0].get_value() == ten or elem[0].get_value() == queen or elem[0].get_value() == king or elem[0].get_value() == ace:
                            carre_score = 100
                        elif elem[0].get_value() == nine:
                            carre_score = 150
                        else:
                            carre_score = 200
            return carre_score
        
        elif team == 2:
            first_list = self.__team2.get_player1().get_announcements_representation()+self.__team2.get_player2().get_announcements_representation()
            first_list = [elem for elem in first_list if len(elem) == 4]
            carre_score = 0
            for elem in first_list:
                    if elem[0].get_value() == elem[1].get_value():
                        if elem[0].get_value() == ten or elem[0].get_value() == queen or elem[0].get_value() == king or elem[0].get_value() == ace:
                            carre_score = 100
                        elif elem[0].get_value() == nine:
                            carre_score = 150
                        else:
                            carre_score = 200
            return carre_score

    def compare_team_announcements(self):
        team1_highest_announcement = self.__team1.get_highest_announcement()
        team2_highest_announcement = self.__team2.get_highest_announcement()

        if team1_highest_announcement == [] and team2_highest_announcement == []:
            return
        if len(team1_highest_announcement) > len(team2_highest_announcement):
            return 1
        elif len(team1_highest_announcement) < len(team2_highest_announcement):
            return 2
        else:
            if team1_highest_announcement[-1].get_value() > team2_highest_announcement[-1].get_value():
                return 1
            elif team1_highest_announcement[-1].get_value() < team2_highest_announcement[-1].get_value():
                return 2

    def play(self):

        current_round = 1

        self.__team1_score = 0
        self.__team2_score = 0

        self.game_count += 1

        while self.__team1_score <= 150 and self.__team2_score <= 150:
            self.__deck.shuffle_deck()
            self.deal_cards()
            self.select_contract()
            self.check_for_belote()

            round_points_team1 = 0
            round_points_team2 = 0

            if self.__contract == no_trumps:
                self.__team1.get_player1().announced_announcements = []
                self.__team1.get_player2().announced_announcements = []
                self.__team2.get_player1().announced_announcements = []
                self.__team2.get_player2().announced_announcements = []
                self.write_team_scores(round_points_team1,round_points_team2)
                result=self.round_dict_to_json(current_round,round_points_team1,round_points_team2)
                self.write_to_json_file(result)
                current_round += 1
                self.rotate_players()
                continue

            result = self.compare_team_announcements()

            if result == 1:
                round_points_team1 += self.calculate_score_of_teams(result)
            elif result == 2:
                round_points_team2 += self.calculate_score_of_teams(result)

            round_points_team1 += self.calculate_belotes_of_teams(1)
            round_points_team2 += self.calculate_belotes_of_teams(2)

            round_points_team1 += self.check_for_carres_in_teams(1)
            round_points_team2 += self.check_for_carres_in_teams(2)
            
            self.write_team_scores(round_points_team1,round_points_team2)
            
            self.__team1_score += round_points_team1
            self.__team2_score += round_points_team2

            result=self.round_dict_to_json(current_round,round_points_team1,round_points_team2)
            self.write_to_json_file(result)
            self.rotate_players()
            current_round += 1

        self.write_final_score(self.__team1_score,self.__team2_score)
        if self.__team1_score > self.__team2_score:
            return 1
        else:
            return 2

    def round_dict_to_json(self,current_round,round_points_team1,round_points_team2):
        round_dict = {f'Round {current_round}':
                            {
                                "Contract: ": self.__contract,
                                str(self.__team1.get_name()):
                                    {self.__team1.get_player1().get_name(): 
                                        {"Cards": str(self.__team1.get_player1().get_hand()),
                                        "announcement": str(self.__team1.get_player1().get_announced_announcements())}, 
                                    self.__team1.get_player2().get_name(): 
                                        {"Cards": str(self.__team1.get_player2().get_hand()),
                                        "announcement": str(self.__team1.get_player2().get_announced_announcements())}, 
                                    "Points": round_points_team1},
                                str(self.__team2.get_name()):
                                    {self.__team2.get_player1().get_name(): 
                                        {"Cards": str(self.__team2.get_player1().get_hand()),
                                    "announcement": str(self.__team2.get_player1().get_announced_announcements())}, 
                                    self.__team2.get_player2().get_name(): 
                                        {"Cards": str(self.__team2.get_player2().get_hand()),
                                    "announcement": str(self.__team2.get_player2().get_announced_announcements())}, 
                                    "Points": round_points_team2}
                            }
                    }

        return round_dict

    def write_to_json_file(self,round_dictionaries):
        with open('data.json', 'a+') as f:
            json_data = json.dumps({f"Game {self.game_count}" :round_dictionaries}, indent=4)
            f.write(json_data)
    
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

def main():
    pass

if __name__ == '__main__':
    main()