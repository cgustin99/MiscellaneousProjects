import random

#Create a tictactoe program

#Initialize board
row1 = [1, "|", 2, "|", 3]
row2 = [4, "|", 5, "|", 6]
row3 = [7, "|", 8, "|", 9]
global board
board = [row1, row2, row3]
global count
count = 0
global on
on = 0

def print_gameboard():
    for i in range(5):
        for j in range(0, 5):
            if i == 0:
                print(row1[j], end = ' ')
            elif i == 2:
                print(row2[j], end = ' ')
            elif i == 4:
                print(row3[j], end = ' ')
        if i == 1 or i == 3:
            print("\n--+---+---")
    print("")
    #board[0, 2, 4][0, 2, 4] are the spots

def update_gameboard_player(x):
    if board_dict[int(x)] == "board[0][0]":
        row1[0] = "x"
    elif board_dict[int(x)] == "board[0][2]":
        row1[2] = "x"
    elif board_dict[int(x)] == "board[0][4]":
        row1[4] = "x"
    elif board_dict[int(x)] == "board[1][0]":
        row2[0] = "x"
    elif board_dict[int(x)] == "board[1][2]":
        row2[2] = "x"
    elif board_dict[int(x)] == "board[1][4]":
        row2[4] = "x"
    elif board_dict[int(x)] == "board[2][0]":
        row3[0] = "x"
    elif board_dict[int(x)] == "board[2][2]":
        row3[2] = "x"
    elif board_dict[int(x)] == "board[2][4]":
        row3[4] = "x"

def update_gameboard_comp(x):
    if board_dict[int(x)] == "board[0][0]":
        row1[0] = "o"
    elif board_dict[int(x)] == "board[0][2]":
        row1[2] = "o"
    elif board_dict[int(x)] == "board[0][4]":
        row1[4] = "o"
    elif board_dict[int(x)] == "board[1][0]":
        row2[0] = "o"
    elif board_dict[int(x)] == "board[1][2]":
        row2[2] = "o"
    elif board_dict[int(x)] == "board[1][4]":
        row2[4] = "o"
    elif board_dict[int(x)] == "board[2][0]":
        row3[0] = "o"
    elif board_dict[int(x)] == "board[2][2]":
        row3[2] = "o"
    elif board_dict[int(x)] == "board[2][4]":
        row3[4] = "o"

def check_board():
    if row1[0] == row1[2] == row1[4] == 'x':
        print("Player wins")
        return 1
    elif row1[0] == row1[2] == row1[4] == 'o':
        print("Computer wins")
        return 1
    if row2[0] == row2[2] == row2[4] == 'x':
        print("Player wins")
        return 1
    elif row2[0] == row2[2] == row2[4] == 'o':
        print("Computer wins")
        return 1
    if row3[0] == row3[2] == row3[4] == 'x':
        print("Player wins")
        return 1
    elif row3[0] == row3[2] == row3[4] == 'o':
        print("Computer wins")
        return 1
    if row1[0] == row2[0] == row3[0] == 'x':
        print("Player wins")
        return 1
    elif row1[0] == row2[0] == row3[0] == 'o':
        print("Computer wins")
        return 1
    if row1[2] == row2[2] == row3[2] == 'x':
        print("Player wins")
        return 1
    elif row1[2] == row2[2] == row3[2] == 'o':
        print("Computer wins")
        return 1
    if row1[4] == row2[4] == row3[4] == 'x':
        print("Player wins")
        return 1
    elif row1[4] == row2[4] == row3[4] == 'o':
        print("Computer wins")
        return 1
    if row1[0] == row2[2] == row3[4] == 'x':
        print("Player wins")
        return 1
    elif row1[0] == row2[2] == row3[4] == 'o':
        print("Player wins")
        return 1
    if row1[4] == row2[2] == row3[0] == 'x':
        print("Player wins")
        return 1
    elif row1[4] == row2[2] == row3[0] == 'o':
        print("Player wins")
        return 1
    else:
        print("It is a tie!")




board_dict = {1: "board[0][0]", 2: "board[0][2]", 3: "board[0][4]",
              4: "board[1][0]", 5: "board[1][2]", 6: "board[1][4]",
              7: "board[2][0]", 8: "board[2][2]", 9: "board[2][4]",
}
print_gameboard()

open_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for turn in range(9):
    #Player makes a move
    print("Make a move:")
    print("Which spot do you choose (1-9)?:")
    move = int(input())
    update_gameboard_player(move)
    print_gameboard()
    open_moves.remove(move)
    count += 1

    if count >= 4:
        num = check_board()
        if num == 1:
            on = 1

    if on == 1:
        break

    #Computer makes move
    print("Now the computer makes a move(Press enter)")
    input()
    move_comp = random.choice(open_moves)
    print(move_comp)
    update_gameboard_comp(move_comp)
    print_gameboard()
    open_moves.remove(move_comp)
    count += 1
