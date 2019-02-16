import functions
import unittest

class GridTests(unittest.TestCase):

  def test_grid(self):
    inputgrid = [False,False,False]
    expected = [False,True,False]
    result = functions.gridtest(inputgrid)

    self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
