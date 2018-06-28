def getmoves():
    with open("connect-four-moves.txt") as f:
        moves = [w.rstrip() for w in f.readlines()]
    return moves

def board():
    board = {}
    for i in range(6):
        board[i] = []
        for j in range(7):
            board[i].append("_ ")
    return board

def display_board(temp):
    for i in range(6):
        print("".join(temp[i]))

def makemoves(movelist, gameboard):
    counter = 0
    for x in movelist:
        if counter % 2 == 0:
            for i in range(6):
                if gameboard[5][int(x) - 1] == "_ ":
                    gameboard[5][int(x) - 1] = "X "
                    break
                elif gameboard[i][int(x) - 1] != "_ ":
                    gameboard[i-1][int(x) - 1] = "X "
                    break
        else:
            for i in range(6):
                if gameboard[5][int(x) - 1] == "_ ":
                    gameboard[5][int(x) - 1] = "O "
                    break
                elif gameboard[i][int(x) - 1] != "_ ":
                    gameboard[i-1][int(x) - 1] = "O "
                    break
        counter += 1
    return gameboard

game = board()
played = makemoves(getmoves(), game)

display_board(played)
