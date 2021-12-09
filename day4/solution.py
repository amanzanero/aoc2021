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
    draw_order, boards = parse_boards()
    score_boards = [
        [
            [False for _ in boards[0][0]] for _ in boards[0]
        ] for _ in boards
    ]

    for order, draw in enumerate(draw_order):
        for i in range(len(boards)):
            update_score(boards[i], score_boards[i], draw)

        for i, score_board in enumerate(score_boards):
            if is_winning_board(score_board):
                sum = 0
                for j in range(len(score_board)):
                    for k in range(len(score_board)):
                        if not score_board[j][k]:
                            sum += int(boards[i][j][k])

                print(sum * int(draw))
                return

def part2():
    draw_order, boards = parse_boards()
    score_boards = [
        [
            [False for _ in boards[0][0]] for _ in boards[0]
        ] for _ in boards
    ]
    boards_won = []
    last_draw = 0

    for order, draw in enumerate(draw_order):
        for i in range(len(boards)):
            update_score(boards[i], score_boards[i], draw)

        for i, score_board in enumerate(score_boards):
            if is_winning_board(score_board) and i not in boards_won:
                last_draw = draw
                boards_won.append(i)

        if len(boards_won) == len(boards):
            break

    sum = 0
    for j in range(len(boards[0])):
        for k in range(len(boards[0])):
            if not score_boards[boards_won[-1]][j][k]:
                sum += int(boards[boards_won[-1]][j][k])

    print(sum * int(last_draw))

if __name__ == '__main__':
    part1()
    part2()
