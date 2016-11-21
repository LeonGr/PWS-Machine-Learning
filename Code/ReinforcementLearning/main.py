from time import clock
from QLearningPlayer import QLearningPlayer
from Player import Player
from TicTacToe import TicTacToe
from ConnectFour import ConnectFour


def train(games):
	# Set timer
	startTime = clock()

	# Train computer
	for i in range(int(games)):
		if i % 1000 == 0: print(i)
		game = ConnectFour(p1, p2)
		game.play_game()

	deltaTime = clock() - startTime
	m, s = divmod(deltaTime, 60)
	print("It took " + str(int(m)) + " minutes and " + str(s) + " seconds to play " + str(games) + " games")

# Assign the players
p1 = QLearningPlayer()
p2 = QLearningPlayer()

# Do your own stuff
train(int(1e6))

# Let the computer play againt a real player
p1 = Player()
p2.epsilon = 0

while True:
	game = ConnectFour(p1, p2)
	game.play_game()
