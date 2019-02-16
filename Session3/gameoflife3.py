def makegrid(size):
    grid = [[False for x in range(size)]for y in range(size)]

    return grid


def makelife(grid, row, column):
    grid[row][column] = True
    return grid
