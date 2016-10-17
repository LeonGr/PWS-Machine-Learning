from copy import deepcopy

class Game:   
    def __init__(self, board=[[0 for x in range(3)] for y in range(3)], turn=1):
        self.board = board
        self.turn = turn

    def print_board(self):
        for row in self.board:
            print(row)

    def check_winner(self):
        for x in self.board:
            if sum(x) == 3 or sum(x) == -3:
                return self.turn

        scored1 = scored2 = 0
        for x in range(3):
            scored1 += self.board[x][x]
            scored2 += list(reversed(self.board[x]))[x]
            score = 0
            for y in range(3):
                score += self.board[y][x]
            if score == 3 or score == -3:
                return self.turn

        if scored1 == 3 or scored1 == -3 or scored2 == 3 or scored2 == -3:
            return self.turn

    def no_winner(self):
        for x in self.board:
            for y in x:
                if y == 0:
                    return False
        return True

    def game_finished(self):
        return self.check_winner() or self.no_winner()

    def place_turn(self, x, y):
        if not self.board[x][y]:
            self.board[x][y] = self.turn
            self.turn *= -1
            return True
        else: return False

    def get_available_moves(self):
        available_moves = []

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if not self.board[x][y]:
                    available_moves.append([x, y])

        return available_moves

#### Machine learning stuff
choice = []

def score(game, depth):
    if game.check_winner() is 1:
        return 10 - depth
    elif game.check_winner() is -1:
        return depth - 10
    else: return 0

def minimax(game, depth=0):
    global choice

    if game.game_finished(): return score(game, depth)

    depth += 1
    scores = []
    moves = []
    
    # Populate the scores array, recursing as needed
    for move in game.get_available_moves():
        possible_game = deepcopy(game)
        possible_game.place_turn(move[0], move[1])

        scores.append(minimax(possible_game, depth))
        moves.append(move)

    # Do the min or the max calculation
    if game.turn is 1:
        max_score_index = scores.index(max(scores))
        choice = moves[max_score_index]
        return scores[max_score_index]
    else:
        min_score_index = scores.index(min(scores))
        choice = moves[min_score_index]
        return scores[min_score_index]

#### End of machine learning stuff

# Create a new game
game = Game()

while True:
    if game.game_finished():
        if game.check_winner() is 1:
            print("Player 1 won")
        elif game.check_winner() is -1:
            print("Player -1 won")
        else: print("Tie")
        break

    if game.turn is 1:
        game.print_board()

        moveX = int(input("x: "))
        moveY = int(input("y: "))
        
        if not game.place_turn(moveX, moveY):
            print("Not a valid play, try again.")

        game.print_board()
    else:
        # Let the machine play a turn
        minimax(game)
        game.place_turn(choice[0], choice[1])

game.print_board()
