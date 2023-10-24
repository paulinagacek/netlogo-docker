import numpy as np
import random
import csv

AGENTS = 20 # percentage of agents

def add_border(board):
    board[0] = np.ones((board.shape[0]))
    board[-1] = np.ones((board.shape[0]))
    board[:,0] = np.ones((1,board.shape[0]))
    board[:,-1] = np.ones((1,board.shape[0]))
    return board

def add_exit_left(board):
    board[board.shape[0]//2, 0] = 2
    return board

def add_middle_wall(board):
    board[:,board.shape[0]//2] = np.ones((1,board.shape[0]))
    board[board.shape[0]//4,board.shape[0]//2] = 0
    return board

def add_pedestrians(board):
    for i in range (1, board.shape[0] - 2):
        for j in range (1, board.shape[0] - 2):
            randValue = random.randint(0,100)
            if board[i][j] == 0 and randValue < AGENTS:
                board[i][j] = 3
    return board


def generate_board_1(size):
    board = np.zeros((size, size), dtype=np.uint8)
    board = add_border(board)
    board = add_exit_left(board)
    board = add_middle_wall(board)
    board = add_pedestrians(board)
    print(board)
    return board

def save_to_csv(board, filename):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        for row in board:
            writer.writerow(row)

board_1_50 = generate_board_1(50)
save_to_csv(board_1_50, "board_1_50.csv")