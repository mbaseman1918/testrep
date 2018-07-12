from os import system

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


    def continuefollow(self, i, x, y, counter, token):
        """
        looks at index i in directions to see if token matches
        """
        direction = self.lookaround(x, y)
        # print(f"Index 4 in this list is the current point being assessed.  Index {i} is the next point")
        # print(direction)
        if direction[i][0] < 0:
            return counter
        if direction[i][1] < 0:
            return counter
        try:
            if self.full_board[direction[i][0]][direction[i][1]] == token:
                counter += 1
                return self.continuefollow(i, direction[i][0], direction[i][1], counter, token)
                # if (self.continuefollow([j], direction[j][0], direction[j][1], counter, token) > 5):
                #     # print(f"{token} WINS!")
                #     return 0
        except IndexError:
            return counter
        else:
            return counter

    def follow(self, x, y, token):
        """
        Looks around initial position and returns a list of directions worth
        """
        direction = self.lookaround(x, y)
        # print("Initial direction options")
        # print(direction)
        check = []
        for i in range(9):
            if i == 4:
                continue
            elif direction[i][0] < 0:
                continue
            elif direction[i][1] < 0:
                continue
            try:
                if self.full_board[direction[i][0]][direction[i][1]] == token:
                    check.append(i)
            except IndexError:
                continue
        # print("These are the directions that will be assessed")
        # print(check)
        return check

    def win(self):
        """
        Identifies a set of coordinates and returns a list of scores showing the number of tokens in a line that was followed.
        """
        y_coordinate = 0
        for y in self.full_board:
            x_coordinate = 0
            for x in y:
                if x == "X" or x == "O":
                    direction_list = self.follow(y_coordinate, x_coordinate, x)
                    for direction in direction_list:
                        if self.continuefollow(direction, y_coordinate, x_coordinate, 1, x) > 2:
                            return f"{x}"
                x_coordinate += 1
            y_coordinate += 1


class player(object):
    def __init__(self, token, board):
        self.token = token
        self.board = board

    def move(self, x, y):
        if self.board.full_board[x][y] not in ["X", "O"]:
            self.board.full_board[x][y] = self.token



"""
THIS IS THE GAME
"""

play = "yes"
while play.lower() in ["yes", "y"]:
    commands = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    board1 = board()
    player1 = player("X", board1)
    player2 = player("O", board1)
    counter = 0
    print()
    print(board1)
    print()
    while True:
        if counter%2 == 0:
            position = int(input("Where would you like to place your token? "))
            while board1.full_board[commands[position][0]][commands[position][1]] in ["X", "O"]:
                position = int(input("There is already a piece at that location.  Where would you like to place your token? "))
            player1.move(commands[position][0],commands[position][1])
        if counter%2 == 1:
            position = int(input("Where would you like to place your token? "))
            while board1.full_board[commands[position][0]][commands[position][1]] in ["X", "O"]:
                position = int(input("There is already a piece at that location.  Where would you like to place your token? "))
            player2.move(commands[position][0],commands[position][1])
        counter += 1
        system("cls")
        print()
        print(board1)
        print()
        if board1.win() in ["X", "O"]:
            print(board1.win() + " WINS!")
            play = input("Would you like to play again? ")
            break
        # for token in ["X", "O"]:
        #     if board1.win() == token:
        #         print(f"{token} WINS!")
        #         break

# commands = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
# board1 = board()
# player1 = player("X", board1)
# player2 = player("O", board1)
# player2.move(commands[3][0], commands[3][1])
# player2.move(1,1)
# player2.move(2,0)
# print(board1)
# print(board1.win())
# print(board1.full_board)
# print(board1.lookaround(1,1))
