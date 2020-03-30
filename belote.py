from player import Player
from team import Team
from game import Game

def main():

    #unfortunately we ran out of time and the game has four major problems
    #1. it writes results only for the first team
    #2. it doesn't display how much each round the score has increased (i think i know where the problem is but it's deadline)
    #3. we didn't have enough time to create the to_json_file method
    #4. we didn't have enough time to write more tests for the methods in game.py
    #and one more thing - the results file is not formatted

    team1_name = input('Team 1 name: ')
    
    team2_name = input('Team 2 name: ')

    players_team1 = input(f'"{team1_name}" players: ')

    players_team2 = input(f'"{team2_name}" players: ')

    list_of_players_team1 = players_team1.split(', ')

    list_of_players_team2 = players_team2.split(', ')

    team1_player1 = Player(list_of_players_team1[0])
    team1_player2 = Player(list_of_players_team1[1])
    team2_player1 = Player(list_of_players_team2[0])
    team2_player2 = Player(list_of_players_team2[1])

    team1 = Team(team1_name,[team1_player1,team1_player2])

    team2 = Team(team2_name,[team2_player1,team2_player2])

    game = Game(team1,team2)

    game.initialize_file_with_results()

    winners = {1: 0, 2: 0}

    while winners[1] != 2 and winners[2] != 2:
        winners[game.play()] += 1

    if winners[1] == 2:
        print('Winner: ',team1)
    else:
        print('Winner: ',team2)

if __name__ == '__main__':
    main()
