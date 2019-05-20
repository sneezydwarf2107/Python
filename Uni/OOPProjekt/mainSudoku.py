from SudokuHelper import *


def main_solver(sudoku):

    print_sudoku(sudoku)

    position = 0
    found = False
    #Step 1 - Leeres Feld finden

    for i in range(len(sudoku[0])):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                position = [i, j]
                found = True
                break
        if found:
            break
    # Step 3 - Ausgabe wenn Lösung gefunden
    if position == 0:

        print("=============================")
        print("===========SOLVED============")
        print("=============================")

        print_sudoku(sudoku)
        exit(0)

    #Step 2 - Versuche Werte 1 - 9 und rufe Programm dann rekursiev auf

    for i in range(1,10):
        if check(sudoku, i, position):
            sudoku[position[0]][position[1]] = i
            main_solver(sudoku)
            sudoku[position[0]][position[1]] = 0
    return False


if __name__ == "__main__":

    sudoku = [[4, 1, 0, 0, 6, 5, 0, 0, 7],
              [0, 0, 6, 0, 0, 7, 4, 8, 0],
              [2, 0, 7, 4, 9, 0, 0, 0, 6],
              [0, 6, 0, 0, 7, 0, 1, 0, 0],
              [3, 0, 1, 5, 0, 0, 0, 7, 2],
              [0, 9, 0, 0, 4, 2, 3, 0, 8],
              [1, 0, 8, 6, 0, 0, 0, 2, 9],
              [0, 2, 0, 0, 1, 8, 6, 4, 0],
              [6, 0, 0, 3, 0, 0, 0, 1, 0]]

    main_solver(sudoku)
