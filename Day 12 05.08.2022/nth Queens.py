n = int(input())
board = [[0]*n for i in range(n)]

# Safe Function
def isSafe(row,col):
    # Check in Row and Col
    for i in range(n):
        if board[row][i] == 1:
            return False
    for j in range(n):
        if board[j][col] == 1:
            return False

    # Check North-West Direction
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j-1

    # Check North-East Direction
    i = row-1
    j = col+1
    while(i>=0 and j<n):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j+1

    # Check South-West Direction
    i = row+1
    j = col-1
    while(i<n and j>=0):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j-1

    # Check South-East Direction
    i = row+1
    j = col+1
    while(i<n and j<n):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j+1
    return True

def Put(n, count):
    if count == n:
        return True

    for i in range(n):
        for j in range(n):
            if isSafe(i, j):
                board[i][j] = 1
                count = count+1
                
                if Put(n, count) == True:
                    return True
                board[i][j] = 0
                count = count-1
    return False

# board = [[0]*n for i in range(n)]       
Put(n, 0)
for i in board:print(*i)