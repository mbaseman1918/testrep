import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4
inventory = []
# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

sword_i = random.randint(0, height - 1)
sword_j = random.randint(0, width - 1)
while board[sword_i][sword_j] == '§':
    print("sword was placed with enemy.")
    sword_i = random.randint(0, height - 1)
    sword_j = random.randint(0, width - 1)
board[sword_i][sword_j] = '¥'

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command.lower() in ['left', 'l']:
        player_j -= 1  # move left
    elif command.lower() in ['right', 'r']:
        player_j += 1  # move right
    elif command.lower() in ['up', 'u']:
        player_i -= 1  # move up
    elif command.lower() in ['down', 'd']:
        player_i += 1  # move down
    elif command.lower() in ['inventory', 'i']:
        print(inventory)

    # keep player in the game area
    while (player_i not in range(height)) or (player_j not in range(width)):
        print("You've reached the edge of reality.")
        if command.lower() in ['left', 'l']:
            player_j += 1  # move left
        elif command.lower() in ['right', 'r']:
            player_j -= 1  # move right
        elif command.lower() in ['up', 'u']:
            player_i += 1  # move up
        elif command.lower() in ['down', 'd']:
            player_i -= 1  # move down


    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack' and "sword" in inventory:
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break

    # add sword to inventory
    if board[player_i][player_j] == '¥':
        print('you\'ve obtained the SWORD OF UNKNOWABLE POWER!  You know it is powerful.')
        inventory.append("sword")
        board[player_i][player_j] = ' '  # remove the sword from the board

    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
