def makegrid():
    grid = [[False,False,False],[False,False,False],[False,False,False]]
    return grid

def makelife(Posititon):
    grid = makegrid()
    row = Posititon[0]
    part = Posititon[1]
    grid[row,part] = True
    Print(grid)

makelife([1,1])
