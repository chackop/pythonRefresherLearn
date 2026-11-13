from itertools import product


def solve_sudoku(board):
    for row, col in product(range(0, 9), repeat=2):
        if board[row][col] == 0:
            for num in range(1, 10):
                allowed = True  # check if the number is allowed in the current row, column, and 3x3 box
                for i in range(0, 9):
                    if num in (board[row][i], board[i][col]):
                        allowed = False
                        break
                for i, j in product(range(0, 3), repeat=2):
                    if num == board[row - row % 3 + i][col - col % 3 + j]:
                        allowed = False
                        break
                if allowed:
                    board[row][col] = num
                    if solve_sudoku(board):
                        return True
                    board[row][col] = 0
            return False
    return board


def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))
