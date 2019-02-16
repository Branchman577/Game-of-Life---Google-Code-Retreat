import gameoflife
import unittest

class CodeRetreat(unittest.TestCase):
    def setUp(self):
        self.g=gameoflife.grid(3)
        self.g=gameoflife.add(self.g,0,0)
    def test_one(self):
        self.assertEqual(len(gameoflife.grid(3)),3)
    def test_two(self):
        self.assertEqual(self.g[0][0],True)

if __name__ == '__main__':
    unittest.main()
