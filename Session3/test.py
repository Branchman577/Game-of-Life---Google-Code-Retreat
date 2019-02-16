import gameoflife
import unittest

class CodeRetreat(unittest.TestCase):
    def test_make_grid(self):
        expected = [[True]]
        self.assertTrue(gameoflife.makegrid(1))

    def test_life(self):
        expected = [[True,False,False],[False,False,False],[False,False,False]]
        grid = gameoflife.makegrid(3)
        self.assertEqual(gameoflife.makelife(grid,0,0),expected)

    def test_outside_grid(self):
        grid = gameoflife.makegrid(3)
        self.assertFalse(gameoflife.makegrid(3), 0, -1)
        self.assertFalse(gameoflife.makegrid, -1, 0)


if __name__ == '__main__':
    unittest.main()
