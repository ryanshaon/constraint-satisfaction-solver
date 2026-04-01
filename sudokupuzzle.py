"""Sudoku solver using CSP backtracking."""

BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_board(board):
    print("\nSolved Sudoku:\n")
    for row_idx, row in enumerate(board):
        if row_idx % 3 == 0 and row_idx != 0:
            print("-" * 21)

        for col_idx, value in enumerate(row):
            if col_idx % 3 == 0 and col_idx != 0:
                print("|", end=" ")
            print(value, end=" ")

        print()


def find_empty(board):
    for row_idx in range(9):
        for col_idx in range(9):
            if board[row_idx][col_idx] == 0:
                return row_idx, col_idx
    return None


def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for row_idx in range(9):
        if board[row_idx][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for row_offset in range(3):
        for col_offset in range(3):
            if board[start_row + row_offset][start_col + col_offset] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if not is_valid(board, row, col, num):
            continue

        board[row][col] = num
        if solve(board):
            return True
        board[row][col] = 0

    return False


def main():
    board = [row[:] for row in BOARD]
    if solve(board):
        print_board(board)
    else:
        print("No solution exists")


if __name__ == "__main__":
    main()