import unittest
from Forest import Forest

class ForestTest(unittest.TestCase):
  
  def setUp(self):
    self.size = 5

  def test_isInBounds(self):
    forest = Forest(self.size)

    location_inbounds = (1, 3)
    self.assertTrue(forest.isInBounds(location_inbounds))

    location_outofbounds = (self.size, self.size + 1)
    self.assertFalse(forest.isInBounds(location_outofbounds))

  def test_elementManipulation(self):
    location = (1, 3)
    value = 5

    forest = Forest(self.size)
    forest.setValue(location, value)
    get_value = forest.getValue(location)

    self.assertEqual(get_value, value)

  def test_getNeighborBaseCase(self):
    location = (1, 3)
    forest = Forest(self.size)

    neighbor_locations = forest.getNeighborLocations(location)

    self.assertEqual(len(neighbor_locations), 4)

  def test_getNeighborEdgeCase(self):
    location = (0, 0)
    forest = Forest(self.size)

    neighbor_locations = forest.getNeighborLocations(location)

    self.assertEqual(len(neighbor_locations), 2)


  def test_getForestLocations(self):
    forest = Forest(self.size)
    location1 = (1, 2)
    location2 = (1, 3)
    location3 = (2, 3)

    forest.addTree(location1)
    forest.addTree(location2)
    forest.addTree(location3)

    tree_locations = forest.getForestLocations(location1)

    self.assertEqual(len(tree_locations), 3)

  def test_addTree(self):
    forest = Forest(self.size)
    location1 = (1, 3)
    location2 = (2, 3)
    location3 = (4, 4)

    forest.addTree(location1)
    forest.addTree(location2)
    forest.addTree(location3)

    self.assertEqual(forest.getValue(location1), 2)
    self.assertEqual(forest.getValue(location2), 2)
    self.assertEqual(forest.getValue(location3), 1)

  def test_getUnoccupiedLocations(self):
    forest = Forest(self.size)
    location1 = (1, 3)
    location2 = (2, 3)
    location3 = (4, 4)

    forest.addTree(location1)
    forest.addTree(location2)
    forest.addTree(location3)

    unoccupied_locations = forest.getUnoccupiedLocations()
    expected_ammount = self.size * self.size - 3

    self.assertEqual(len(unoccupied_locations), expected_ammount)

  def test_getForests(self):
    forest = Forest(self.size)
    location1 = (1, 3)
    location2 = (2, 3)
    location3 = (4, 4)
    location4 = (1, 1)
    location5 = (1, 2)
    location6 = (4, 2)

    forest.addTree(location1)
    forest.addTree(location2)
    forest.addTree(location3)
    forest.addTree(location4)
    forest.addTree(location5)
    forest.addTree(location6)

    forests = forest.getForests()
    num_forests = 3

    self.assertEqual(len(forests), num_forests)

if __name__ == '__main__':
  unittest.main()