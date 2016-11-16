class TicTacToe:
	def __init__(self, player1, player2):
		self.board = [[0 for x in range(3)] for y in range(3)]
		self.player1, self.player2 = player1, player2

	def play_game(self):
		# Let this function handle the gameplay
		pass

	def print_board(self):
		printed_board = []

		for row in self.board:
			printed_row = []
			for entry in row:
				if entry == 0:
					printed_row.append('   ')
				elif entry == 1:
					printed_row.append(' X ')
				elif entry == -1:
					printed_row.append(' O ')
			printed_board.append(printed_row)

		print(printed_board[0][0] + '|' + printed_board[0][1] + '|' + printed_board[0][2])
		print("-----------")
		print(printed_board[1][0] + '|' + printed_board[1][1] + '|' + printed_board[1][2])
		print("-----------")
		print(printed_board[2][0] + '|' + printed_board[2][1] + '|' + printed_board[2][2])
