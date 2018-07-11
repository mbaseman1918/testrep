class board(object):
    """
    Creates a board that can be manipulated by the players
    """
    def __init__(self):
        row1 = ['1','2','3']
        row2 = ['4','5','6']
        row3 = ['7','8','9']
        self.full_board = [row1, row2, row3]
        self.winner = []

    def __repr__(self):
        """
        Displays the board
        """
        return '\n'.join('|'.join(j) for j in self.full_board)

    def lookaround(self, x, y):
        """
        Creates a list of points around the point being observed.
        """
        checklist = []
        checkx = [int(x)-1, int(x), int(x)+1]
        checky = [int(y)-1, int(y), int(y)+1]
        for i in checkx:
            for j in checky:
                checklist.append([i,j])
        return checklist


    def continuefollow(self, i, x, y, currentboard, counter, token):
        """
        Iterates through i to check designated directions for a win
        """
        direction = self.lookaround(x, y)
        print(direction)
        for j in i:
            try:
                if currentboard[direction[j][0]][direction[j][1]] == token:
                    counter += 1
                    if (counter + self.continuefollow([j], direction[j][0], direction[j][1], currentboard, counter, token) > 5):
                        print(f"{token} WINS!")
                        return 0
            except IndexError:
                return 0
            else:
                return 0

    def follow(self, x, y, currentboard, token):
        """
        Establishes directions to look for checking if a player won
        """
        direction = self.lookaround(x, y)
        check = []
        for i in range(9):
            if i == 4:
                continue
            try:
                if self.full_board[direction[i][0]][direction[i][1]] == token:
                    check.append(i)
            except IndexError:
                continue
        return check

    def win(self): # checks for a winner
        counterY = 0
        score_list = []
        for y in self.full_board:
            counterX = 0
            for x in y:
                if x == "X" or x == "O":
                    self.continuefollow(self.follow(counterY, counterX, self.full_board, x), counterY, counterX, self.full_board, 1, x)
                counterX += 1
            counterY += 1


class player(object):
    def __init__(self, token, board):
        self.token = token
        self.board = board

    def move(self, x, y):
        if self.board.full_board[x][y] not in ["X", "O"]:
            self.board.full_board[x][y] = self.token

while True:
    commands = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    board1 = board()
    player1 = player("X", board1)
    player2 = player("O", board1)
    counter = 0
    while True:
        print()
        print(board1)
        print()
        if counter%2 == 0:
            position = int(input("Where would you like to place your token?"))
            player1.move(commands[position][0],commands[position][1])
        if counter%2 == 1:
            position = int(input("Where would you like to place your token?"))
            player2.move(commands[position][0],commands[position][1])
        counter += 1
        if board1.win() == "X WINS!":
            print("You win!")
            break



    # player2.move(commands[1][0], commands[1][1])
    # player2.move(1,1)
    # player2.move(2,2)
    # print(board1)
    # board1.win()
    # print(board1.full_board)
    # print(board1.lookaround(1,1))
