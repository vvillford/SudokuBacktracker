import sudoku

# test = [[0 for i in range(9)] for j in range(9)]

# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]
# problem = sudoku.Sudoku(board)

def solve(puzzle):
  
  current_spot = puzzle.find_empty() # row, 
  if not current_spot: # since current spot returns none if no spaces 0 this will be a complete puzzle
    return True
  else:
    row, column = current_spot
  for i in range(1, 10):
    if puzzle.checkfeasable(i):
      puzzle.array[row][column] = i
      if solve(puzzle):
        return True
      puzzle.array[row][column] = 0
  return False

# solve(problem)
# problem.display()