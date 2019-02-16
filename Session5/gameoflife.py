def grid(size):
    return [[False for x in range(size)] for y in range(size)]
def add(grid,x,y):
    grid[x][y]=True
    return grid
