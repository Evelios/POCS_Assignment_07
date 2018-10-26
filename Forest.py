import numpy as np

class Forest:

  def __init__(self, size):
    self.num_trees = 0
    self.size = size
    self.matrix = np.zeros((self.size, self.size), dtype=int)

  def copy(self):
    other = Forest(self.size)
    other.num_trees = self.num_trees
    other.size = self.size
    other.matrix = np.copy(self.matrix)

    return other

  def getValue(self, location):
    return self.matrix.item(location)

  def getNumTrees(self):
    return self.num_trees

  def setValue(self, location, value):
    self.matrix.itemset(location, value)

  def getForestMatrix(self):
    return self.matrix

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

  def getForests(self):
    forests = []
    explored_forest_locations = []
    for location in np.ndindex(self.size, self.size):
      if self.getValue(location) == 0:
        continue
      
      neighbor_explored = False
      neighbors = self.getNeighborLocations(location)
      for neighbor in neighbors:
        if neighbor in explored_forest_locations:
          neighbor_explored = True
      
      if not neighbor_explored:
        forest_locations = self.getForestLocations(location)
        forests.append(forest_locations)
        explored_forest_locations.extend(forest_locations)

    return forests


  def getUnoccupiedLocations(self):
    unnocupied_locations = []

    for index, forest_size in np.ndenumerate(self.matrix):
      if forest_size == 0:
        unnocupied_locations.append(index)

    return unnocupied_locations