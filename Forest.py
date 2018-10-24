import numpy as np

class Forest:

  def __init__(self, size):
    self.num_trees = 0
    self.size = size
    self.forest = np.zeros((self.size, self.size), dtype=int)

  def copy(self):
    other = Forest(self.size)
    other.num_trees = self.num_trees
    other.size = self.size
    other.forest = np.copy(self.forest)

    return other

  def getValue(self, location):
    return self.forest.item(location)

  def getNumTrees(self):
    return self.num_trees

  def setValue(self, location, value):
    self.forest.itemset(location, value)

  def getForestMatrix(self):
    return self.forest

  def getNeighborLocations(self, location):
    x = location[0]
    y = location[1]
    neighbors = [
      (x    , y + 1),
      (x    , y - 1),
      (x + 1, y    ),
      (x - 1, y    )
    ]

    return [n for n in neighbors if self.isInBounds(n)]

  def getNeighborValues(self, location):
    locations = self.getNeighborLocations(location)
    return [self.getValue(location) for location in locations]

  def isInBounds(self, location):
    x = location[0]
    y = location[1]
    return 0 <= x < self.size and 0 <= y < self.size 

  def addTree(self, location):
    self.num_trees += 1
    self.setValue(location, 1)
    forest_locations = self.getForestLocations(location)
    forest_size = len(forest_locations)
    for tree in forest_locations:
      self.setValue(tree, forest_size)

  # Get all the forest locations associated from a particular tree 
  def getForestLocations(self, location):
    if self.getValue(location) <= 0:
      return []
    
    frontier = [location]
    explored = []

    while frontier:
      explore = frontier.pop()
      explored.append(explore)

      neighbors = self.getNeighborLocations(explore)
      for neighbor in neighbors:
        if (neighbor not in frontier and
            neighbor not in explored and
            self.getValue(neighbor) > 0):

          frontier.append(neighbor) 

    return explored
  
  def getUnoccupiedLocations(self):
    unnocupied_locations = []

    for index, forest_size in np.ndenumerate(self.forest):
      if forest_size == 0:
        unnocupied_locations.append(index)

    return unnocupied_locations