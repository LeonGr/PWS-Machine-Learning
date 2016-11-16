from QLearningPlayer import QLearningPlayer
from Player import Player
from TicTacToe import TicTacToe


# Assign the players
p1 = QLearningPlayer()
p2 = QLearningPlayer()

# Train the computer
for i in range(int(5e3)):
	game = TicTacToe(p1, p2)
	game.play_game()

p1 = Player()

while True:
	game = TicTacToe(p1, p2)
	game.play_game()
