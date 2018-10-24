import unittest
import numpy as np
from HotModel import HotModel

class HotModelTest(unittest.TestCase):
  
  def setUp(self):
    self.size = 5
    self.design_parameter = 2
    self.hot_model = HotModel(5, 1)

  def test_normalizedProbability(self):
    prob = 0
    for y in range(self.size):
      for x in range(self.size):
        loc = (x, y)
        loc_prob = self.hot_model.probability(loc)
        prob += loc_prob

    self.assertAlmostEqual(prob, 1)

if __name__ == '__main__':
  unittest.main()