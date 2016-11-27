from time import clock
from QLearningPlayer import QLearningPlayer
from Player import Player
from TicTacToe import TicTacToe
from ConnectFour import ConnectFour

import json

test_games_results = {'Player1wins': 0, 'Player2wins': 0, 'Ties': 0}

def train(games):
        # Set timer
        startTime = clock()

        # Train computer
        for i in range(1, games + 1):
            if i % 1000 == 0:
                print(i)

            game = TicTacToe(p1, p2)
            game.play_game()

        deltaTime = clock() - startTime
        m, s = divmod(deltaTime, 60)
        with open("static/test.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data["trained"] = 'done'
        data["time"] = "It took " + str(int(m)) + " minutes and " + str(s) + " seconds to play " + str(games) + " games"

        with open("static/test.json", "w") as jsonFile:
            jsonFile.write(json.dumps(data))

        print("It took " + str(int(m)) + " minutes and " + str(s) + " seconds to play " + str(games) + " games")

# Assign the players
p1 = QLearningPlayer()
p2 = QLearningPlayer()

# Do your own stuff
def start_training(amount):
    train(int(amount))

# Let the computer play againt a real player

def test_games(games):
    for i in range(games):
        game = TicTacToe(p1, p2)
        game.play_game()
        for thing in test_games_results:
            test_games_results[thing] += game.score[thing]
    global result
    result = 'The results of ' + str(games) + ' games played was ' + str(test_games_results)
    print(result)

# test_games(int(1e3))

def start_playing(ai_start=False):
    print('start playing')
    p1 = Player()
    p2.epsilon = 0
    global game
    game = TicTacToe(p1, p2)
    game.start_game(ai_start)
