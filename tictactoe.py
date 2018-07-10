class board(object):
    def __init__(self):
        row1 = ['1','|','2','|','3']
        row2 = ['4','|','5','|','6']
        row3 = ['7','|','8','|','9']
        self.full_board = [row1, row2, row3]
        self.player_positions = [i[::2] for i in self.full_board]

    def __repr__(self): # displays the board
        return '\n'.join(''.join(j) for j in self.full_board)

    def lookaround(self, x, y):
        checklist = []
        checkx = [int(x)-1, int(x), int(x)+1]
        checky = [int(y)-1, int(y), int(y)+1]
        for i in checkx:
            for j in checky:
                checklist.append([i,j])
        return checklist


    def continuefollow(self, i, x, y, currentboard, token):
        direction = self.lookaround(x, y)
        if currentboard[direction[i][0]][direction[i][1]] == token:
            try:
                return 1 + self.continuefollow(i, direction[i][0], direction[i][1], self.player_positions, token)
            except IndexError:
                return 0
        else:
            return 1

    def follow(self, x, y, currentboard, token):
        direction = self.lookaround(x, y)
        for i in range(10):
            if i == 4:
                continue
            try:
                if self.player_positions[direction[i][0]][direction[i][1]] == token:
                    try:
                        return 1 + self.continuefollow(i, direction[i][0], direction[i][1], self.player_positions, token)
                    except IndexError:
                        return 0
            except:
                return 0

    def win(self): # checks for a winner
        self.player_positions = [i[::2] for i in self.full_board]
        counterY = 0
        for y in self.player_positions:
            counterX = 0
            for x in y:
                if x in ["X", "O"]:
                    print(1+(self.follow(counterX, counterY, self.player_positions, x)))
                counterX += 1
            counterY += 1

class player(object):
    def __init__(self, token, board):
        self.token = token
        self.board = board

    def move(self, x, y):
        if self.board.full_board[x][y] not in ["X", "O"]:
            self.board.full_board[x][y] = self.token

# while
board1 = board()
player1 = player("X", board1)
player2 = player("O", board1)
player1.move(1,0)
player2.move(1,2)
player1.move(1,4)
print(board1)
print(board1.win())
