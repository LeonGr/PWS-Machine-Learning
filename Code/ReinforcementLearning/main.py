from QLearningPlayer import QLearningPlayer
from Player import Player
from TicTacToe import TicTacToe


# Assign the players
p1 = QLearningPlayer()
p2 = QLearningPlayer()

# Create the game
game = TicTacToe(p1, p2)
game.print_board()
