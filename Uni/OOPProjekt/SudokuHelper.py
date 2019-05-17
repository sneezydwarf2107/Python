def print_sudoku(sudoku):

    print("=============================")
    for i in range(len(sudoku[0])):
        if (i % 3 == 0) and (i != 0):
            print("         ")

        for j in range(len(sudoku)):

            if j % 3 == 0 and j != 0:
                print("  ", end="")

            print(str(sudoku[i][j]) + "  ", end="")

            if j == 8:
                print("")
    print("=============================")


def is_empty(test):
    if test:
        return False

    else:
        return True


def check(sudoku, candidate, position):


    #Check Row
    for i in range(len(sudoku[0])):

        if sudoku[position[0]][i] == candidate and i != position[1]:
            return False

    #Check Column
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == candidate and i != position[0]:
            return False

    #Check Square



