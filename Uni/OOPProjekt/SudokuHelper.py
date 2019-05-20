def print_sudoku(sudoku):

    print("                             ")
    for i in range(len(sudoku[0])):
        if (i % 3 == 0) and (i != 0):
            print("         ")

        for j in range(len(sudoku)):

            if j % 3 == 0 and j != 0:
                print("  ", end="")

            print(str(sudoku[i][j]) + "  ", end="")

            if j == 8:
                print("")


def check(sudoku, candidate, position):
    """
    This function is checking if candidate exists in either the column, row or square it is located

    :param sudoku: 2D-list, containing the sudoku
    :param candidate: integer value, the value that has to be checked
    :param position: list [Column, Row], containing the position of the empty cell

    :return: TRUE - if candidate is valid, FALSE - if candidate is not valid
    """
    #Check Row
    for i in range(len(sudoku[0])):

        if sudoku[position[0]][i] == candidate and i != position[1]:
            return False

    #Check Column
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == candidate and i != position[0]:
            return False

    #Check Square
    # First step, calculated the square the empty cell is located in
    x_cor = int(position[0]/3)*3
    y_cor = int(position[1]/3)*3

    # Second step, iterate over the square
    for i in range(x_cor, x_cor+3):
        for j in range(y_cor, y_cor+3):
            if sudoku[i][j] == candidate and [i,j] != position:
                return False

    return True


def is_empty(list):
    """
    This function checks if a cell is empty

    :param list:
    :return:
    """
    if list:
        return False

    else:
        return True