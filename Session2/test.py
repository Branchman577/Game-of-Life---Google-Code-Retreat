import gameoflife
import unittest

class CodeRetreat(unittest.TestCase):
    def test_checkneighbours(self):
        grid = gameoflife.makegrid()
        gameoflife.makelife(grid,1,1)
        gameoflife.makelife(grid,2,1)
        self.assertEqual(1,gameoflife.countneighbours(grid,1,1))

    def test_checkneighboursoverflow(self):
        grid = gameoflife.makegrid()
        gameoflife.makelife(grid,1,1)
        gameoflife.makelife(grid,2,1)
        self.assertEqual(1,gameoflife.countneighbours(grid,2,1))

if __name__ == '__main__':
    unittest.main()
