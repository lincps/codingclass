# Tic Tac Toe Game
# ahfarrell@gmail.com
from __future__ import print_function

YOU = '.'
COMP = 'X'
EMPTY_BOARD = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
LINES = ((0, 1, 2),
         (3, 4, 5),
         (6, 7, 8),
         (0, 3, 6),
         (1, 4, 7),
         (2, 5, 8),
         (0, 4, 8),
         (2, 4, 6))


def clear_board():
    return list(EMPTY_BOARD)


def choose_again():
    print("Not a valid choice.")
    print("Please choose again.")


def print_board(board):
    print("Current board:")
    print(board[0] + ' ' + board[1] + ' ' + board[2])
    print(board[3] + ' ' + board[4] + ' ' + board[5])
    print(board[6] + ' ' + board[7] + ' ' + board[8])


def move_you(board):
    while True:
        print("Pick a number between 0 and 8 that is free:")
        choice_ = input().strip()
        if choice_ in EMPTY_BOARD:
            choice = int(choice_)
            if board[choice] == YOU or board[choice] == COMP:
                choose_again()
            else:
                board[choice] = YOU
                break
        else:
            choose_again()


def move_computer(board):
    for choice in range(0, 8):
        if not board[choice] == YOU and not board[choice] == COMP:
            board[choice] = COMP
            break


def move_computer_improvement1(board):
    while True:
        import random
        choice = int(random.random() * 9.0)
        if not board[choice] == YOU and not board[choice] == COMP:
            board[choice] = COMP
            break


def move_computer_improvement2(board):
    if move_computer_try(board, COMP):
        return

    move_computer_improvement1(board)


def move_computer_improvement3(board):
    if move_computer_try(board, COMP):
        return

    if move_computer_try(board, YOU):
        return

    move_computer_improvement1(board)


def move_computer_try(board, piece):
    for line in LINES:
        if check_line(line, board, piece):
            return True
    return False


def check_line(line, board, piece):
    a, b, c = line
    return \
        check_combination(a, b, c, board, piece) or \
        check_combination(b, a, c, board, piece) or \
        check_combination(c, a, b, board, piece)


def check_combination(sp, co1, co2, board, piece):
    if board[sp] != COMP \
            and board[sp] != YOU and board[co1] == piece and board[co2] == piece:
        board[sp] = COMP
        return True


def check_squares(a, b, c):
    if a == b and b == c:
        if a == COMP:
            print("The Computer has won!")
            return True

        elif a == YOU:
            print("You have won!")
            return True
    return False


def check_win(board):
    for (a, b, c) in LINES:
        if check_squares(board[a], board[b], board[c]):
            return True

    if not list(set(board).intersection(set(EMPTY_BOARD))):
        print("It is a tie.")
        return True

    return False


def check_continue():
    while True:
        print("Would you like to play again? Enter: yes or no")
        cont = input().strip()
        if cont == 'yes':
            return True
        elif cont == 'no':
            return False
        else:
            print("That is not a valid answer")


print("Let's play the computer at tic-tac-toe")
print("The computer is X's and you are .'s")
print("You can start")


while True:
    board = clear_board()
    print_board(board)
    while True:
        move_you(board)
        if check_win(board):
            print_board(board)
            break
        move_computer_improvement3(board)
        print("The computer has chosen!")
        print_board(board)
        if check_win(board):
            break
    if not check_continue():
        break
