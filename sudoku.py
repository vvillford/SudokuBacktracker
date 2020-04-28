class Sudoku:
  """
  A class representing an instance of a 9 x 9 sudoku puzzle.
  """

  def __init__(self, array):
    self.array = array
    self.currentlocation = 0, 0

  def checkfeasable(self, number):
    """
    returns True if the input is feasable at the current position and False if not
    """
    row, column = self.currentlocation

    #this checks the current row
    for i in range(9):
      if number == self.array[row][i] and column != i:
        return False
    
    #this checks the current column
    for j in range(9):
      if number == self.array[j][column] and row != j:
        return False

    #this checks the current box
    row_start = row - row % 3
    column_start = column - column % 3
    for j in range(row_start, row_start + 3):
      for i in range(column_start, column_start + 3):
        if self.array[j][i] == number and (i, j) != self.currentlocation:
          return False
    
    # if all tests pass, return True
    return True
  
  def find_empty(self):
    # finds the next square with a 0, moves along row by row
    for row  in range(9):
      for column in range(9):
        if self.array[row][column] == 0:
          self.currentlocation = row, column
          return self.currentlocation
    return None
  
  def __repr__(self):
    return f"<Sudoku object at {id(self)}>"

  def display(self):
    for i in range(9):
      if i % 3 == 0 and i != 0:
        print("- - - - - - - - - - - -")
      for j in range(9):
        if j % 3 == 0 and j != 0:
          print(" | ", end="")
        if j == 8:
          print(self.array[i][j])
        else:
          print(f"{self.array[i][j]} ", end="")



