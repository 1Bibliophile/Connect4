from cgi import print_form
import numpy as np
import pygame
import sys
BLUE = (0,0,255)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Checks all the horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Checks for the positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Checks for the negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    pass

board = create_board()
print_board(board)
turn = 0
game_over = False
pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE 

size = (width, height)
screen = pygame.display.set_mode(size)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Ask for Player 1 Input
            # if turn == 0:
            #     col = int(input("Player 1, make your selection (0-6): "))

            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_piece(board, row, col, 1)

            #         if winning_move(board, 1):
            #             print("Player 1 Wins! Congrats!")
            #             game_over = True

            # Ask for Player 2 Input
            # else:
            #     col = int(input("Player 2, make your selection (0-6): "))

            #     if is_valid_location(board, col):
            #         row = get_next_open_row(board, col)
            #         drop_piece(board, row, col, 2)
 
            #         if winning_move(board, 2):
            #             print("Player 2 Wins! Congrats!")
            #             game_over = True
            #             break
            pass

    # print_board(board)

    # turn += 1
    # turn = turn % 2