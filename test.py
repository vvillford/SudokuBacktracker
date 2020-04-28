from sudoku import Sudoku
from main import solve
test = [[0 for i in range(9)] for j in range(9)]

puzzle = Sudoku(test)

solve(puzzle)

puzzle.display()