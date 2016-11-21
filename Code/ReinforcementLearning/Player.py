class Player(object):
	def __init__(self):
		self.species = "human"

	def startGame(self):
		pass

	def move(self, board):
		return int(input("x: "))

	def reward(self, value, board):
		pass

	def available_moves(self, board):
		moves = []
		#for y in range(len(board)):
		#	for x in range(len(board[y])):
		#		if not board[y][x]:
		#			moves.append([x, y])
		for x in range(7):
			if not board[0][x]:
				moves.append(x)

		return moves
