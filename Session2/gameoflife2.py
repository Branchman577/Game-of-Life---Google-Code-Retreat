def makegrid():
    grid = [[False,False,False],[False,False,False],[False,False,False]]
    return grid

def makelife(grid,x,y):
    grid[x][y] = True

def kill(grid,x,y):
    grid[x][y] = False

def countneighbours(grid,x,y,count = 0):
    count += counttop(grid,x,y)
    count += countmid(grid,x,y)
    count += countbot(grid,x,y)
    return count

def counttop(grid,x,y,count = 0):
    if x - 1 < 0 : return
    if grid[x -1][y-1]: count += 1
    if grid[x- 1][y]: count += 1
    if grid[x -1][y+1]: count += 1
    return count

def countmid(grid,x,y,count = 0):
    if grid[x][y-1]: count += 1
    if grid[x][y+1]: count += 1
    return count

def countbot(grid,x,y,count = 0):
    if x + 1 >= len(grid): return
    if grid[x + 1][y-1]: count += 1
    if grid[x + 1][y]: count += 1
    if grid[x + 1][y+1]: count += 1
    return count
