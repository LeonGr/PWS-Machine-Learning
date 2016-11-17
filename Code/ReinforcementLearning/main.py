from time import clock
from QLearningPlayer import QLearningPlayer
from Player import Player
from TicTacToe import TicTacToe


# Assign the players
p1 = QLearningPlayer()
p2 = QLearningPlayer()

# Set timer
startTime = clock()

# Train the computer
for i in range(int(1e6)):
	if i % 1000 == 0: print(i)
	game = TicTacToe(p1, p2)
	game.play_game()

deltaTime = clock() - startTime
m, s = divmod(deltaTime, 60)
print("It took " + str(m) + " minutes and " + str(s) + " seconds to play 1 million games")

p1 = Player()
p2.epsilon = 0

while True:
	game = TicTacToe(p1, p2)
	game.play_game()
