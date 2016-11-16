class Player(Object):
	def __init__(self):
		self.species = "human"

	def available_moves(self, board):
		moves = []
		for y in range(len(board)):
			for x in range(len(board[y])):
				if not board[y][x]:
					moves.append([x, y])
		return moves
