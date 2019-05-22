from SudokuHelper import *
import sys

def main_solver(sudoku):
    #print_sudoku(sudoku)

    #print(sudoku[0])

    position = 0
    found = False
    # Step 1 - Leeres Feld finden

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

        sys.exit(None)

    # Step 2 - Versuche Werte 1 - 9 und rufe Programm dann rekursiev auf

    for i in range(1, 10):
        if check_Row(sudoku, i, position) and check_Column(sudoku, i, position) and check_Square(sudoku, i, position):
            sudoku[position[0]][position[1]] = i
            main_solver(sudoku)
            sudoku[position[0]][position[1]] = 0
    return False


if __name__ == "__main__":
    sudoku =[[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,3,0,8,5],
[0,0,1,0,2,0,0,0,0],
[0,0,0,5,0,7,0,0,0],
[0,0,4,0,0,0,1,0,0],
[0,9,0,0,0,0,0,0,0],
[5,0,0,0,0,0,0,7,3],
[0,0,2,0,1,0,0,0,0],
[0,0,0,0,4,0,0,0,9]]

    print_sudoku(sudoku)

    main_solver(sudoku)
