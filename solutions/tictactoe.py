# Tic Tac Toe Game
# ahfarrell@gmail.com
import sys

EMPTY_BOARD = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
YOU = 'O'
COMP = 'X'


def clear_board():
    return EMPTY_BOARD


def choose_again():
    print "Not a valid choice."
    print "Please choose again."


def print_board(board):
    print "Current board:"
    print board[0] + ' ' + board[1] + ' ' + board[2]
    print board[3] + ' ' + board[4] + ' ' + board[5]
    print board[6] + ' ' + board[7] + ' ' + board[8]


def move_you(board):
    while True:
        print "Pick a number between 0 and 8 that is free:"
        choice_ = sys.stdin.readline().strip()
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


def check_squares(a, b, c):
    if a == b and b == c:
        if a == COMP:
            print "The Computer has won!"
            return True

        elif a == YOU:
            print "You have won!"
            return True
    return False


def check_win(board):
    return \
        check_squares(board[0], board[1], board[2]) or \
        check_squares(board[3], board[4], board[5]) or \
        check_squares(board[6], board[7], board[8]) or \
        check_squares(board[0], board[3], board[6]) or \
        check_squares(board[1], board[4], board[7]) or \
        check_squares(board[2], board[5], board[8]) or \
        check_squares(board[0], board[4], board[8]) or \
        check_squares(board[2], board[4], board[6])


def check_continue():
    while True:
        print "Would you like to play again? Enter: yes or no"
        cont = sys.stdin.readline().strip()
        if cont == 'yes':
            return True
        elif cont == 'no':
            return False
        else:
            print " That is not a valid answer"


print "Let's play the computer at tic-tac-toe"
print "The computer is X's and you are O's"
print "You can start"


while True:
    board = clear_board()
    while True:
        print_board(board)
        move_you(board)
        if check_win(board):
            break
        print "The computer has chosen!"
        print_board(board)
        move_computer(board)
        if check_win(board):
            break
    if not check_continue():
        break
