import random
from deck import Deck 
from team import Team

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

    def get_order(self):
        return self.__order

    def rotate_players(self):
        first_player = self.__order[0]
        
        self.__order.remove(first_player)
        
        self.__order.append(first_player)

    def select_contract(self):
        announcements = ['clubs','diamonds','hearts','spades','no trumps','all trumps']
        index = random.randint(0,5)
        
        self.__contract = announcements[index]

    def deal_cards(self):
        for player in self.__order:
            player.set_hand(self.__deck.deal())

    def initialize_file_with_results(self):
        with open("results.txt","w") as f:
            name_of_first_team=self.__team1.get_name()
            f.write("       ")
            f.write(name_of_first_team)
            f.write("       |       ")
            name_of_second_team=self.__team2.get_name()
            f.write("")
            f.write(name_of_second_team)
            f.write("     \n")
            f.write("=================================")

    def write_team_scores(self,score1,score2,current_round):

        with open("results.txt","a+") as f:
            if current_round == 1:
                f.write("\n")
                f.write(str(score1))
                f.write("           |           ")
                f.write(str(score2))
                f.write("\n")
            
            else:
                str1 = str(self.__team1_score) + ' + ' + str(score1)

                str2 = str(self.__team2_score) + ' + ' + str(score2)

                f.write(str(str1))
                f.write("       |       ")
                f.write(str(str2))
                f.write("     \n")



    def check_for_belote(self):
        self.__team1.get_player1().get_belotes(self.__contract)

        self.__team1.get_player2().get_belotes(self.__contract)

        self.__team2.get_player1().get_belotes(self.__contract)
        
        self.__team2.get_player2().get_belotes(self.__contract)

    def calculate_score_of_teams(self,first=False,second=False):
        if first == True:
            list_of_announcements = self.__team1.get_player1().get_announced_announcements()+self.__team1.get_player2().get_announced_announcements()

            new_score = 0

            for announcement in list_of_announcements:
                if announcement == 'belote':
                    self.__team1_score += 20
                    new_score += 20

                if announcement == 'tierce':
                    self.__team1_score += 20
                    new_score += 20

                if announcement == 'quarte':
                    self.__team1_score += 50
                    new_score += 50

                if announcement == 'quinte':
                    self.__team1_score += 100
                    new_score += 100

            return new_score

        elif second == True:
            list_of_announcements = self.__team2.get_player1().get_announced_announcements()+self.__team2.get_player2().get_announced_announcements()

            new_score = 0

            for announcement in list_of_announcements:
                if announcement == 'belote':
                    self.__team1_score += 20
                    new_score += 20

                if announcement == 'tierce':
                    self.__team1_score += 20
                    new_score += 20

                if announcement == 'quarte':
                    self.__team1_score += 50
                    new_score += 50

                if announcement == 'quinte':
                    self.__team1_score += 100
                    new_score += 100

            return new_score

    def check_for_carres_in_team_one(self):
        first_list = self.__team1.get_player1().get_announcements_representation()+self.__team1.get_player2().get_announcements_representation()

        carre_score = 0
        for elem in first_list:
            if len(elem) > 2:
                if elem[0].get_value() == elem[1].get_value():
                    
                    if elem[0].get_value() == '10' or elem[0].get_value() == 'Q' or elem[0].get_value() == 'K' or elem[0].get_value() == 'A':
                        self.__team1_score += 100
                        carre_score = 100
                    
                    elif elem[0].get_value() == '9':
                        self.__team1_score += 150
                        carre_score = 150
                    
                    else:
                        self.__team1_score += 200
                        carre_score = 200

        return carre_score

    def check_for_carres_in_team_two(self):
        first_list = self.__team2.get_player1().get_announcements_representation()+self.__team2.get_player2().get_announcements_representation()

        carre_score = 0
        for elem in first_list:
            if len(elem) > 2:
                if elem[0].get_value() == elem[1].get_value():
                    
                    if elem[0].get_value() == '10' or elem[0].get_value() == 'Q' or elem[0].get_value() == 'K' or elem[0].get_value() == 'A':
                        self.__team2_score += 100
                        carre_score = 100
                    
                    elif elem[0].get_value() == '9':
                        self.__team2_score += 150
                        carre_score = 150
                    
                    else:
                        self.__team2_score += 200
                        carre_score = 200

        return carre_score


    def compare_team_announcements(self):
        team1_highest_announcement = self.__team1.get_highest_announcement()
        team2_highest_announcement = self.__team2.get_highest_announcement()
        if team1_highest_announcement == [] and team2_highest_announcement == []:
            return

        if len(team1_highest_announcement) > len(team2_highest_announcement):
            self.calculate_score_of_teams(first=True)


        elif len(team1_highest_announcement) < len(team2_highest_announcement):
            self.calculate_score_of_teams(second=True)

        else:
            if team1_highest_announcement[-1].get_value() > team2_highest_announcement[-1].get_value():
                self.calculate_score_of_teams(first=True)

            elif team1_highest_announcement[-1].get_value() < team2_highest_announcement[-1].get_value():
                self.calculate_score_of_teams(second=True)


    def play(self): #to do

        current_round = 1

        while self.__team1_score <= 150 and self.__team2_score <= 150:

            self.__deck.shuffle_deck()

            self.deal_cards()

            self.select_contract()
            
            game_contract = self.__contract

            self.check_for_belote()

            round_points_team1 = 0
            round_points_team2 = 0

            self.compare_team_announcements()
            
            round_points_team1 += self.check_for_carres_in_team_one()
            round_points_team2 += self.check_for_carres_in_team_two()

            self.write_team_scores(round_points_team1,round_points_team2,current_round)
            
            current_round += 1

            self.rotate_players()

        if self.__team1_score > self.__team2_score:
            return 1
        else:
            return 2


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