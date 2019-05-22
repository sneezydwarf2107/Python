class Helper:


    def print_sudoku(self, sudoku):
        """
        Prints out the sudoku puzzle and visualizes it



        :param sudoku: Sudoku puzzle
        """
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

    def check_row(self, sudoku, candidate, position):
        """
        Checks if the candidate already exists in the same row, as specified in position[0]



        :param sudoku: Sudoku puzzle
        :param candidate: The candidate that has to be checked
        :param position: The position that has to be checked
        :return: True if candidate is valid, False if candidate is not valid
        """
        # Check Row
        for i in range(len(sudoku[0])):

            if sudoku[position[0]][i] == candidate and i != position[1]:
                return False

        return True

    def check_column(self, sudoku, candidate, position):
        """
        Checks if the candidate already exists in the same column, as specified in position[1]



        :param sudoku: Sudoku puzzle
        :param candidate: Candidate that has to be checked
        :param position: Position that has to be checked
        :return: True if the candidate is valid, False if the candidate is ot valid
         """

        for i in range(len(sudoku)):
            if sudoku[i][position[1]] == candidate and i != position[0]:
                return False

        return True

    def check_square(self, sudoku, candidate, position):
        """
        Checks if the candidate already exists in the same square, as indicated in position

        :param sudoku: Sudoku puzzle
        :param candidate: Candidate that has to be checked
        :param position: Position that has to be checked
        :return: True if candidate is valid, False if candidate is not valid
        """
        # First step, calculated the square the empty cell is located in
        x_cor = int(position[0] / 3) * 3
        y_cor = int(position[1] / 3) * 3

        # Second step, iterate over the square
        for i in range(x_cor, x_cor + 3):
            for j in range(y_cor, y_cor + 3):
                if sudoku[i][j] == candidate and [i, j] != position:
                    return False

        return True

    def is_empty(self, list):
        """
        This function checks if a cell is empty

        :param list:
        :return:
        """
        if list:
            return False

        else:
            return True
