def getmoves():
    with open("connect-four-moves.txt") as f:
        moves = [w.rstrip() for w in f.readlines()]
    return moves

def board():
    board = {}
    for i in range(7):
        board[i] = []
        for j in range(8):
            board[i].append("_ ")
    return board

def display_board(temp):
    for i in range(7):
        print("".join(temp[i]))

def lookaround(z, c):
    checklist = []
    checki = [z-1, z, z+1]
    checkj = [c-1, c, c+1]
    for i in checki:
        for j in checkj:
            checklist.append([i,j])
    return checklist

def continuefollow(follow, x, y, currentboard, player):
    direction = lookaround(x, y)
    if currentboard[direction[follow][0]][direction[follow][1]] == player:
        return 1 + continuefollow(follow, direction[follow][0], direction[follow][1], currentboard, player)
    else:
        return 1


def linefollow(x, y, currentboard, player):
    direction = lookaround(x, y)
    for value in range(9):
        if value == 4:
            pass
        elif currentboard[direction[value][0]][direction[value][1]] == player:
            win = 2 + continuefollow(value, direction[value][0], direction[value][1], currentboard, player)
            if win >= 4:
                return "{} WINS!".format(player[0])
        else:
            pass

def winner(currentboard, player):
        for x in range(7):
            for y in range(8):
                if currentboard[x][y] == "_ ":
                    continue
                elif currentboard[x][y] == player:
                    return linefollow(x, y, currentboard, player)

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

# def checkgame(game_dict):
#     directionlist = []
#     trackx = 0
#     for p in game_dict:
#         tracky = 0
#         for o in game_dict[p]:
#             if game_dict[p][o] != "_ ":
#                 counter = 1

game = board()
played = makemoves(getmoves(), game)
display_board(played)
print(played)
print(winner(played, "O "))
print(winner(played, "X "))
