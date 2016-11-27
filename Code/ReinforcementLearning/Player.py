import json, time

class Player(object):
	def __init__(self):
		self.species = "human"

	def startGame(self):
		pass

	def move(self, board):
                x = int(input("x: "))
                y = int(input("y: "))
                # def get_last_move():
                    # print('do you evne go gheree?')
                    # with open("static/test.json", "r") as jsonFile:
                        # data = json.load(jsonFile)

                    # if (data["last_move"] is not None):
                        # x = data["last_move"][0]
                        # y = data["last_move"][1]

                        # print(data["last_move"] is None)
                        # print(data["last_move"] is False)
                        # print(data["last_move"] is not None)
                        # data["last_move"] = None
                        # print(data["last_move"] is None)
                        # print(data["last_move"] is False)
                        # print(data["last_move"] is not None)

                        # with open("static/test.json", "w") as jsonFile:
                            # jsonFile.write(json.dumps(data))

                        # print(str([x, y]))
                        # return [x, y]

                # get_last_move()

                return [x, y]


	def reward(self, value, board):
		pass

	def available_moves(self, board):
		moves = []
		for y in range(len(board)):
			for x in range(len(board[y])):
				if not board[y][x]:
					moves.append([x, y])
		# for x in range(7):
		# 	if not board[0][x]:
		# 		moves.append(x)

		return moves
