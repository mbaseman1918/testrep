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

def linefollow(x, y, direction1, direction2, currentboard, player, tracker):
    checki = [x-1, x, x+1]
    checkj = [y-1, y, y+1]
    if tracker == 6:
        print("{} WINS!".format(player[0]))
    elif currentboard[checki[direction1]][checkj[direction2]] == player:
        counter = tracker + 1
        linefollow(checki[direction1], checkj[direction2], direction1, direction2, currentboard, player, counter)
    else:
        pass
def winner(i,j,currentboard, player):
    checki = [i-1, i, i+1]
    checkj = [j-1, j, j+1]
    trackx = 0
    if i == 5:
        for x in checki[1:]:
            tracky = 0
            for y in checkj:
                if currentboard[i][j] == currentboard[x][y]:
                    continue
                elif currentboard[x][y] == player:
                    run = 1
                    linefollow(x, y, trackx, tracky, currentboard, player, run)
                tracky += 1
            trackx += 1
    else:
        for x in checki:
            tracky = 0
            for y in checkj:
                if currentboard[i][j] == currentboard[x][y]:
                    continue
                elif currentboard[x][y] == player:
                    run = 1
                    linefollow(x, y, trackx, tracky, currentboard, player, run)
                tracky += 1
            trackx += 1

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

def checkgame(game_dict):
    directionlist = []
    for p in game_dict:

        for o in game_dict[p]:
            if game_dict[p][o] != "_ ":
                counter = 1



game = board()
played = makemoves(getmoves(), game)
display_board(played)
print(played)
