class ConnectFour:
	def __init__(self, player1, player2):
		self.board = [[0 for x in range(7)] for y in range(6)]
		self.player1, self.player2 = player1, player2
		self.turn = 1

	def play_game(self):
		# Let this function handle the gameplay
		# Initialize players
		self.player1.startGame()
		self.player2.startGame()
		while True:
			if self.turn is 1:
				player, other_player = self.player1, self.player2
			else:
				player, other_player = self.player2, self.player1

			if player.species is "human":
				self.print_board()
				print(self.board)

			# Ask for players move
			move = player.move(self.board)
			# Place move
			if not self.place_turn(move):
				break

			# See if the game has ended
			if self.player_wins(self.turn):
				player.reward(1, self.board)
				other_player.reward(-1, self.board)
				break
			if self.board_full(): # Tie
				player.reward(0.5, self.board)
				other_player.reward(0.5, self.board)
				break
			other_player.reward(0, self.board)
			self.turn *= -1

	def place_turn(self, x):
		for y in range(len(self.board) - 1, -1, -1):
			if not self.board[y][x]:
				self.board[y][x] = self.turn
				return True
		return False

	def player_wins(self, turn):
		# check horizontal spaces
		for y in range(6):
			for x in range(4):
				if self.board[y][x] == self.board[y][x + 1] == self.board[y][x + 2] == self.board[y][x + 3] == turn:
					return True

		# check vertical spaces
		for x in range(7):
			for y in range(3):
				if self.board[y][x] == self.board[y + 1][x] == self.board[y + 2][x] == self.board[y + 3][x] == turn:
					return True

		## check / diagonal spaces
		for x in range(4):
			for y in range(3, 6):
				if self.board[x][y] == self.board[y - 1][x + 1] == self.board[y - 2][x + 2] == self.board[y - 3][x + 3] == turn:
					return True

		## check \ diagonal spaces
		for x in range(4):
			for y in range(3):
				if self.board[y][x] == self.board[y + 1][x + 1] == self.board[y + 2][x + 2] == self.board[y + 3][x + 3] == turn:
					return True

		return False

	def board_full(self):
		for row in self.board:
			for cell in row:
				if cell == 0:
					return False
		return True

	def print_board(self):
		for row in self.board:
			printed_row = ''
			for x in range(len(row)):
				entry = row[x]
				if entry == 0:
					printed_row += '   '
				elif entry == 1:
					printed_row += ' X '
				elif entry == -1:
					printed_row += ' O '

				if x < len(row) - 1:
					printed_row += '|'
			print(printed_row)
