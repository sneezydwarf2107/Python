from SudokuHelper import *


def main_solver(sudoku):
    print_sudoku(sudoku)


if __name__ == "__main__":
    sudoku = [[3, 0, 0, 9, 4, 0, 0, 0, 0],
              [2, 0, 0, 0, 8, 0, 7, 4, 0],
              [0, 8, 0, 0, 0, 6, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 3, 1, 5],
              [0, 0, 0, 1, 0, 4, 0, 0, 0],
              [1, 5, 9, 0, 0, 0, 0, 0, 2],
              [0, 0, 0, 6, 0, 0, 0, 9, 0],
              [0, 6, 2, 0, 7, 0, 0, 0, 3],
              [0, 0, 0, 0, 3, 2, 0, 0, 6]]

    main_solver(sudoku)
