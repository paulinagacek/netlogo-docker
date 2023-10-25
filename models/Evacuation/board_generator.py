import numpy as np
import random
import csv

AGENTS = 2  # percentage of agents


def add_border(board):
    board[0] = np.ones((board.shape[0]))
    board[-1] = np.ones((board.shape[0]))
    board[:, 0] = np.ones((1, board.shape[0]))
    board[:, -1] = np.ones((1, board.shape[0]))
    return board


def add_exit_left(board):
    board[board.shape[0] // 2, 0] = 2
    return board


def add_exit_right(board):
    board[board.shape[0] // 2, board.shape[0] - 1] = 2
    return board


def add_middle_wall(board):
    board[:, board.shape[0] // 2] = np.ones((1, board.shape[0]))
    board[board.shape[0] // 4, board.shape[0] // 2] = 0
    return board


def add_middle_wall_2(board):
    board[board.shape[0] // 4 : board.shape[0] // 2, board.shape[0] // 2] = np.ones(
        (1, board.shape[0] // 2 - board.shape[0] // 4)
    )
    board[
        board.shape[0] // 2 : int(board.shape[0] * 0.8), board.shape[0] // 4
    ] = np.ones((1, int(board.shape[0] * 0.8) - board.shape[0] // 2))

    board[0 : int(board.shape[0] * 0.4), int(board.shape[0] * 0.8)] = np.ones(
        (1, int(board.shape[0] * 0.4))
    )

    board[
        board.shape[0] // 2, board.shape[0] // 4 : int(board.shape[0] * 0.8)
    ] = np.ones((int(board.shape[0] * 0.8) - board.shape[0] // 4))

    board[
        board.shape[0] // 2 : int(board.shape[0] * 0.8), int(board.shape[0] * 0.25)
    ] = np.ones((1, int(board.shape[0] * 0.8) - board.shape[0] // 2))

    board[
        int(board.shape[0] * 0.7), board.shape[0] // 2 + 1 : int(board.shape[0] - 1)
    ] = np.ones((int(board.shape[0] - 1) - board.shape[0] // 2 - 1))

    board[
        int(board.shape[0] // 4), board.shape[0] // 4 + 1 : int(board.shape[0] * 0.7)
    ] = np.ones((int(board.shape[0] * 0.7) - board.shape[0] // 4 - 1))

    return board


def add_pedestrians(board):
    for i in range(1, board.shape[0] - 2):
        for j in range(1, board.shape[0] - 2):
            randValue = random.randint(0, 100)
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


def generate_board_2(size):
    board = np.zeros((size, size), dtype=np.uint8)
    board = add_border(board)
    board = add_exit_left(board)
    board = add_exit_right(board)
    add_middle_wall_2(board)
    board = add_pedestrians(board)
    print(board)
    return board


def round(x):
    return int(np.round(x))


def draw_horizontal(
    board,
    start,
    size,
    y_start_offset=0,
    x_start_offset=0,
    x_end_offset=0,
    size_offset=0,
    draw_value=1,
):
    y, x = start
    board[
        round(board.shape[0] * y) + y_start_offset,
        round(board.shape[0] * x)
        + x_start_offset : round(board.shape[0] * (x + size))
        + x_end_offset,
    ] = (
        np.ones(round(board.shape[0] * size) + size_offset) * draw_value
    )
    return board


def draw_vertical(
    board,
    start,
    size,
    y_start_offset=0,
    y_end_offset=0,
    x_start_offset=0,
    size_offset=0,
    draw_value=1,
):
    y, x = start
    board[
        round(board.shape[0] * y)
        + y_start_offset : round(board.shape[0] * (y + size))
        + y_end_offset,
        round(board.shape[0] * x) + x_start_offset,
    ] = (
        np.ones(round(board.shape[0] * size) + size_offset) * draw_value
    )
    return board


def add_dormitory(board):
    # horizontal
    board[board.shape[0] // 4, :] = np.ones((board.shape[0]))
    board[round(board.shape[0] * 0.75), :] = np.ones((board.shape[0]))

    ##### stairs
    # horizontal
    board = draw_horizontal(board, (0.4, 0.5), 0.4)
    board = draw_horizontal(board, (0.6, 0.5), 0.4)
    board = draw_horizontal(board, (0.5, 0.65), 0.25)
    board[round(board.shape[0] * 0.4), round(board.shape[0] * 0.6)] = 0
    board[round(board.shape[0] * 0.4), round(board.shape[0] * 0.6) + 1] = 0
    board[round(board.shape[0] * 0.6), round(board.shape[0] * 0.6)] = 0
    board[round(board.shape[0] * 0.6), round(board.shape[0] * 0.6) + 1] = 0

    # vertical
    board = draw_vertical(board, (0.4, 0.5), 0.2)
    board = draw_vertical(board, (0.4, 0.9), 0.2, x_start_offset=-1)

    ##### kitchen
    board = draw_horizontal(board, (0.4, 0.0), 0.3)
    board = draw_horizontal(board, (0.6, 0.0), 0.3)
    board = draw_vertical(board, (0.4, 0.3), 0.2, size_offset=1, y_end_offset=1)
    board[round(board.shape[0] * 0.4), round(board.shape[0] * 0.2)] = 0
    board[round(board.shape[0] * 0.4), round(board.shape[0] * 0.2) + 1] = 0
    board[round(board.shape[0] * 0.6), round(board.shape[0] * 0.2)] = 0
    board[round(board.shape[0] * 0.6), round(board.shape[0] * 0.2) + 1] = 0

    # rooms
    board = draw_horizontal(board, (0.15, 0.0), 1.0)
    board = draw_horizontal(board, (0.85, 0.0), 1.0)
    for i in range(0, 6):
        # top
        board = draw_vertical(board, (0.75, i / 6), 0.25)
        board[
            round(board.shape[0] * 0.75), round(board.shape[0] * (i / 6 + 1 / 12))
        ] = 0

        # bottom
        board = draw_vertical(board, (0.0, i / 6), 0.25)
        board[
            round(board.shape[0] * 0.25), round(board.shape[0] * (i / 6 + 1 / 12))
        ] = 0

        # room dividers
        board = draw_vertical(board, (0.85, (i / 6 + 1 / 12)), 0.15)
        board = draw_vertical(board, (0.0, (i / 6 + 1 / 12)), 0.15)
        board[
            round(board.shape[0] * 0.15), round(board.shape[0] * (i / 6 + 1 / 24))
        ] = 0
        board[
            round(board.shape[0] * 0.15), round(board.shape[0] * (i / 6 + 3 / 24))
        ] = 0

        board[
            round(board.shape[0] * 0.85), round(board.shape[0] * (i / 6 + 1 / 24))
        ] = 0
        board[
            round(board.shape[0] * 0.85), round(board.shape[0] * (i / 6 + 3 / 24))
        ] = 0

    # exits
    board = draw_vertical(
        board,
        (0.5, 0.9),
        0.05,
        x_start_offset=-2,
        size_offset=0,
        draw_value=2,
        y_start_offset=2,
        y_end_offset=2,
    )
    # board[round(board.shape[0] * 0.5) + 2, round(board.shape[0] * 0.9) - 2] = 2
    # board[round(board.shape[0] * 0.5) + 3, round(board.shape[0] * 0.9) - 2] = 2


def generate_board_3(size):
    board = np.zeros((size, size), dtype=np.uint8)
    board = add_border(board)
    # board = add_exit_left(board)
    # board = add_exit_right(board)
    add_dormitory(board)
    board = add_pedestrians(board)
    print(board)
    return board


def save_to_csv(board, filename):
    with open(filename, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)

        for row in board:
            writer.writerow(row)


board = generate_board_3(100)
save_to_csv(board, "board_3_100.csv")
