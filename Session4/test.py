import gameoflife
import unittest

class CodeRetreat(unittest.TestCase):
    def test_make_grid_one(self):
        expected = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
        self.assertEqual(gameoflife.makegrid(4),expected)

    def test_make_grid_two(self):
        expected = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
        self.assertNotEqual(gameoflife.makegrid(5),expected)

    def test_make_life_one(self):
        expected =  [[False,False,False,False],[False,False,True,False],[False,False,False,False],[False,False,False,False]]
        grid = gameoflife.makegrid(4)
        self.assertEqual(gameoflife.makelife(grid,1,2),expected)

    def test_make_life_two(self):
            expected =  [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]]
            grid = gameoflife.makegrid(4)
            self.assertEqual(gameoflife.makelife(grid,3,2),expected)

    def test_make_life_three(self):
            expected =  [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,True]]
            grid = gameoflife.makegrid(5)
            self.assertEqual(gameoflife.makelife(grid,3,3),expected)



if __name__ == '__main__':
    unittest.main()
