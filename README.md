# Belote Declarations

Belote is one of the most famous card games in Bulgaria. This project is partially belote - the game's scoring is what makes it different from the original.

# Setup

Download the repository and run the game with the command ```python3 belote.py```

# Program explanation

The program imitates a game of belote where the scores are generated only from the declarations of the players.

When you run the game you will have to input the names of the two teams and the players from each team. For example:

```
python3 belote.py

Team 1 name: Mecheta
Team 2 name: Koteta

"Mecheta" players: Marto, Rado
"Koteta" players: Gosho, Pesho
```

The two teams alternate when declaring. And after each round, the first player from the last round becomes last.
When a game is won by a team, a random player from this team starts the first round of the next game.

The points from one round are calculated by summing the points from the declarations of each team. For example, if 'Marto' has tierce (20) and 'Rado' has quarte (50), their result from the round is 70 points.
**NOTE: In the real game of Belote, these points are divided by 10. For this task it is not necessary!!!**

The program finishes when one of the teams win 2 games.

One game is won by the first team that scores more than 150 points. If both of the teams have more than 150 points, the game is won by the team who has more points. If the points are equal, the game continues until one of the teams shoot ahead.

After each round, the points from the current round are written into the `results.txt` file.

```
     Mecheta     |     Koteta
=================================
20               | 100
20 + 50          | 100 + 0
```

This is how it is marked when a game is won by a team:

```
     Mecheta     |     Koteta
=================================
20               | 100
20 + 20          | 100 + 20
40 + 50          | 120 + 0
90 + 100         | 120 + 50
190              | 170
=================================
       (1)       |      (0)
=================================
```

After each round, the contract of the round, the cards and the announcements of each player are written in `data.json` file.
Let's say we have this round:

```
Marto: ["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"]  # team Mecheta
Gosho: ["7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad"]  # team Koteta
Rado: ["7d", "8c", "9d", "10d", "Js", "Qs", "Kd", "Ac"]  # team Mecheta
Pesho: ["7h", "8h", "9h", "10h", "Jc", "Qh", "Ks", "Ah"]  # team Koteta
```

```json
{
  "game 1": {
    "round 1": {
      "contract": "Hearts",
      "Mecheta": {
        "Marto": {
          "cards:": ["7s", "8s", "9s", "10c", "Jd", "Qh", "Kh", "As"],
          "announcements": ["belote"],
          "points": 20
        },
        "Rado": {
          "cards:": ["7d", "8c", "9d", "10d", "Js", "Qs", "Kd", "Ac"],
          "announcements": [],
          "points": 0
        }
      },
      "Koteta": {
        "Gosho": {
          "cards:": ["7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad"],
          "announcements": [],
          "points": 0
        },
        "Pesho": {
          "cards:": ["7h", "8h", "9h", "10h", "Jc", "Qd", "Ks", "Ah"],
          "announcements": ["quarte"],
          "points": 50
        }
      }
    }
    // rest of the rounds here ....
  }
}
```
