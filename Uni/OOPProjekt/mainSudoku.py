from checkCandidates import *

def main_solver(sudoku):
	"""This will be the main Function called recursivly to solve the sudoku
	
	Arguments:
		sudoku {list} -- list with length 81, containing the unsolved sudoku
	
	Returns:
		{list} -- list with length 81, containing the solved sudoku
	"""

	a = check(sudoku)

	while not is_empty(a[0]) and is_empty(a[1]):
		
		print("test")

	return sudoku


if __name__ == "__main__":
	sudoku = input("Bitte geben Sie das zu lösende Sudoku ein: ")
	sudoku = main_solver(sudoku)
	print(sudoku)
