# Given 2D board of characters and a word, find if the word exists in the grid.
# The board is fixed and is given below:
# [
#   ['A','B','C','I'],
#   ['B','I','C','S'],
#   ['C','D','E','E']
# ]
# The word can be constructed from letters of sequentially adjacent cell, where 'adjacent' cells are thos horizontally or vertically neighboring. The same letter cell may not be used more than once.
# The above grid must be initialized in the program itself.
# Input:
# 2
# ABCCED
# ABCB

# 4
# BICSI
# BIE
# ZOHO
# SEE

# Output:
# True 
# False

# True
# False
# False
# True

def findSolution(x, y, count, r, string, solution_grid, puzzle_grid):
  if (count==len(string)):
    return True

  if x >= 0 and x <= 2 and y >= 0 and y <= 3 and string[r]==puzzle_grid[x][y] and solution_grid[x][y] == '0':
    solution_grid[x][y] = '1'

    if (findSolution(x, y+1, count+1, r+1, string, solution_grid, puzzle_grid) == True):
      return True

    if (findSolution(x, y-1, count+1, r+1, string, solution_grid, puzzle_grid) == True):
      return True

    if (findSolution(x+1, y, count+1, r+1, string, solution_grid, puzzle_grid) == True):
      return True

    if (findSolution(x-1, y, count+1, r+1, string, solution_grid, puzzle_grid) == True):
      return True
    
    solution_grid[x][y] = '0'
    return False
    
  return False

testcase = int(input())
for i in range(testcase):
  string = input()
  puzzle_grid = [['A','B','C','I'],['B','I','C','S'],
['C','D','E','E']]
  solution_grid = [['','','',''],['','','',''],
['','','','']]
  d1, d2, count = 0, 0, 0
  for i in range(3):
    for j in range(4):
      if(puzzle_grid[i][j] == string[0]):
        d1, d2 = i, j
        count+=1
      solution_grid[i][j] ='0'
  count2, r = 0, 0
  
  flag = findSolution(d1, d2, count2, r, string, solution_grid, puzzle_grid)
  
  if flag == 1:
    print("True")
  else:
    print("False")