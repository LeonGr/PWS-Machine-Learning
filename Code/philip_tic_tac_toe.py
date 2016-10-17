class Game:
    board = [[0 for x in range(3)] for y in range(3)]
    turn = 1
    
    def print_board(self):
        for row in self.board:
            print(row)

    def check_winner(self):
        for x in self.board:
            if sum(x) == 3 or sum(x) == -3:
                print("player " + str(self.turn) + " is the winner")
                return self.turn

        scored1 = scored2 = 0
        for x in range(3):
            scored1 += self.board[x][x]
            scored2 += list(reversed(self.board[x]))[x]
            score = 0
            for y in range(3):
                score += self.board[y][x]
            if score == 3 or score == -3:
                print("player " + str(self.turn) + " is the winner")
                return self.turn

        if scored1 == 3 or scored1 == -3 or scored2 == 3 or scored2 == -3:
            print("player " + str(self.turn) + " is the winner")
            return self.turn

    def no_winner(self):
        for x in self.board:
            for y in x:
                if y == 0:
                    return False
        return True

#### Machine learning stuff
def score(game):
    if game.check_winner() is 1:
        return 10
    elif game.check_winner() is -1:
        return -10
    else: return 0

def minimax(game):
    scores = []
    moves = []
    

#### End of machine learning stuff

game = Game()

game.print_board()

while True:
    moveX = int(input())
    moveY = int(input())
    
    if not game.board[moveX][moveY]:
        game.board[moveX][moveY] = game.turn
        if game.check_winner():
            break
        if game.no_winner():
            print("Tie")
            break
        game.turn *= -1
    
    game.print_board()

game.print_board()
