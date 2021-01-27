from colors import *
from drawings import key_dict, new_board

clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


def draw_board(board):
    print(clear)
    for i in board:
        print(f"{i[0]}  {i[1]}  {i[2]}")
    print("\n\n\n")


def play(board, player):
    while True:
        try:
            player_input = input(f"Your move {CORANGE}{player}{CEND}: (enter number between 1-9)\n").lower().strip()
            turn = key_dict[player_input]
        except KeyError:
            # if the player enters something that isn't a number between 1-9, then the program will ask it again
            player_input = input(f"{CRED}Please enter a valid move.{CEND} \n\nYour move {player}:\n").lower().strip()
            turn = key_dict[player_input]
        row = turn[0]
        column = turn[1]
        if board[row][column] == '-':
            # if the space that the player wants to play in is empty, it is a valid move
            break
        else:
            # if the space is already taken, then it isn't a valid move and goes through the while loop
            draw_board(board)
            print(f"{CRED}Please enter a valid move!{CEND}")
    board[row][column] = player[0]
    return board


def check_win(board, player):
    win_statement = f"{CBLUE}{player} has won!"
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            # checks horizontal wins
            if board[i][0] == player[0]:
                print(win_statement)
                return True
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            # checks vertical wins
            if board[0][i] == player[0]:
                print(win_statement)
                return True
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            # checks diagonal 1
            if board[0][0] == player[0]:
                print(win_statement)
                return True
        if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            # checks diagonal 2
            if board[0][2] == player[0]:
                print(win_statement)
                return True
    return False


def check_draw(board):
    for row in board:
        if '-' in row:
            return False
    print(f"{CVIOLET}Draw!")
    return True


def main():
    name_1 = input("Enter your name, Player 1:\n").title()
    name_2 = input("Enter your name, Player 2:\n").title()
    if name_1[0] == name_2[0]:
        # if the names both start with the same letter, they will be X's and O's
        name_1, name_2 = "X", "O"

    board = new_board
    draw_board(board)
    while True:
        # player 1's turn
        draw_board(play(board, name_1))
        if check_win(board, name_1) or check_draw(board):
            break

        # player 2's turn
        draw_board(play(board, name_2))
        if check_win(board, name_2) or check_draw(board):
            break


if __name__ == '__main__':
    main()
