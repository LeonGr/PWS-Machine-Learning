board = [[0 for x in range(3)] for y in range(3)]
turn = 1
def print_board():
    for row in board:
        print(row)

def check_winner():
    for x in board:
        if sum(x) == 3 or sum(x) == -3:
            print("player " + str(turn) + " is the winner")
            return True

    for x in range(3):
        score = 0
        for y in range(3):
            score += board[y][x]
        if score == 3 or score == -3:
            print("player " + str(turn) + " is the winner")
            return True

def no_winner():
    for x in board:
        for y in x:
            if y == 0:
                return False
    return True

print_board()

while(True):
    moveX = int(input())
    moveY = int(input())
    if not board[moveX][moveY]:
        board[moveX][moveY] = turn
        if check_winner():
            break
        if no_winner():
            print("Tie")
            break
        turn *= -1
    print_board()

print_board()
