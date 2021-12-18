import unittest
import fishnumbers

class TestNumbers(unittest.TestCase):
  def test_simple_magnitude(self):
    self.assertEqual(fishnumbers.magnitude([9,1]), 29)
    self.assertEqual(fishnumbers.magnitude([1,9]), 21)

  def test_nested_magnitude(self):
    self.assertEqual(fishnumbers.magnitude([[1,2],[[3,4],5]]), 143)
    self.assertEqual(fishnumbers.magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]), 1384)

  def test_addrightmost(self):
    self.assertEqual(fishnumbers.add_rightmost(
      [[[1, 2], [3, 4]], [1, [2, 3]]], 1),
      [[[1, 2], [3, 4]], [1, [2, 4]]]
    )

  def test_addleftmost(self):
    self.assertEqual(fishnumbers.add_leftmost(
      [[[1, 2], [3, 4]], [1, [2, 3]]], 1),
      [[[2, 2], [3, 4]], [1, [2, 3]]]
    )

  def test_explode(self):
    pass
    #self.assertEqual(fishnumbers.explode([[[[[9,8],1],2],3],4]), [[[[0,9],2],3],4])

  def test_split(self):
    pass

if __name__ == '__main__':
    unittest.main()
