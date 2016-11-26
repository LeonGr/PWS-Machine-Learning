from flask import Flask, render_template
app = Flask(__name__)

from time import clock
from QLearningPlayer import QLearningPlayer
from Player import Player
from TicTacToe import TicTacToe
from ConnectFour import ConnectFour

test_games_results = {'Player1wins': 0, 'Player2wins': 0, 'Ties': 0}

def train(games):
	# Set timer
	startTime = clock()

	# Train computer
	for i in range(1, games + 1):
		if i % 1000 == 0: print(i)
		game = TicTacToe(p1, p2)
		game.play_game()

	deltaTime = clock() - startTime
	m, s = divmod(deltaTime, 60)
	print("It took " + str(int(m)) + " minutes and " + str(s) + " seconds to play " + str(games) + " games")

# Assign the players
p1 = QLearningPlayer()
p2 = QLearningPlayer()

# Do your own stuff
train(int(1e3))

# Let the computer play againt a real player
# p1 = Player()
p1.epsilon = 0
p2.epsilon = 1

result = None

def test_games(games):
    for i in range(games):
        game = TicTacToe(p1, p2)
        game.play_game()
        for thing in test_games_results:
            test_games_results[thing] += game.score[thing]
    global result
    result = ('The results of ' + str(games) + ' games played was ' + str(test_games_results))

test_games(int(1e3))

@app.route("/")
def hello():
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
