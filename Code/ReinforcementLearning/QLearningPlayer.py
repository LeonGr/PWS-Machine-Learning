class QLearningPlayer:
	def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
		self.q = {} # (state, action) keys: Q values
		self.epsilon = epsilon # Chance of random exploration
		self.alpha = alpha # Learning rate
		self.gamma = gamma # Discount factor

	def startGame(self):
		self.last_board = [[0 for x in range(3)] for y in range(3)]
		self.last_move = None

	def getQ(self, state, action):
		# encourage exploration; "optimistic" 1.0 initial values
		if self.q.get((state, action)) is None:
			self.q[(state, action)] = 1.0
		return self.q.get((state, action))

	def move(self, board):
		pass

	def reward(self, value, board):
		pass

	def learn(self, state, action, reward, result_state):
		pass
