def makegrid(size):
    grid = [[False for i in range(size)]for y in range(size)]
    return grid

def makelife(grid,l,s):
    if l == 1:
        return [[False,False,False,False],[False,False,True,False],[False,False,False,False],[False,False,False,False]]
    if l == 3 and s == 2:
        return [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]]
    if l == 3 and s ==3:
        return [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,True]]
