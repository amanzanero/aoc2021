from util import parseLines
from pprint import pprint


def parse_boards():
    lines = parseLines("input.txt")
    draw_order = lines[0].split(",")

    boards = []
    current_board = []
    for i, row in enumerate(lines[2:]):
        if row == "":
            boards.append(current_board)
            current_board = []
        else:
            nums = row.split()
            current_board.append(nums)
    boards.append(current_board)
    return (draw_order, boards)


def is_winning_board(board):
    for i in range(len(board)):
        row_won = True
        for col in board[i]:
            row_won = row_won and col
        if row_won:
            return row_won

        col_won = True
        for row in board:
            col_won = col_won and row[i]
        if col_won:
            return col_won

    return False


def update_score(board, score_board, draw):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == draw:
                score_board[i][j] = True


def part1():
    pass

def part2():
    pass

if __name__ == '__main__':
    part1()
    part2()
