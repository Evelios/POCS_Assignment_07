import numpy as np
from math import exp, pi, e
from random import shuffle
from Forest import Forest

class HotModel:

  def __init__(self, grid_size, design_parameter):
    self.grid_size = grid_size
    self.design_parameter = design_parameter
    self.prob_scale = self.getCharacteristicScale()
    self.norm_const = self.getNormalizationConstant()
    self.forest = Forest(self.grid_size)

  def getNormalizationConstant(self):
    return (
      (1 - exp(-1 / self.prob_scale)) /
      (1 - exp(-self.grid_size / self.prob_scale))
    )**2

  def getCharacteristicScale(self):
    return self.grid_size / 10

  def probability(self, location):
    return 1 / self.grid_size**2

  # This probability needs to be normalized
  # def probability(self, location):
  #   # characteristic sjcale for the distribution
  #   l = self.prob_scale 
  #   x = location[0] + 1
  #   y = location[1] + 1

    # return self.norm_const * exp(-x/l) * exp(-y/l)

  def isFullyPopulated(self):
    return self.getNumTrees() >= self.grid_size**2

  def getNumTrees(self):
    return self.forest.getNumTrees()

  def getNormalizedNumTrees(self):
    return self.getNumTrees() / self.grid_size**2 

  def getForestYield(self):
    return self.normalizedAverageYieldFrom(self.forest)
  
  def getForestMatrix(self):
    return np.copy(self.forest.getForestMatrix())

  def normalizedAverageYieldFrom(self, forest):
    return self.averageYieldFrom(forest) / self.grid_size**2

  def averageYieldFrom(self, forest):
    return forest.getNumTrees() - self.averageLightningDamageFrom(forest)

  def averageLightningDamageFrom(self, forest):
    forest_matrix = forest.getForestMatrix()
    damage = 0
    for index, forest_size in np.ndenumerate(forest_matrix):
      loc_prob = self.probability(index)
      damage += forest_size * loc_prob
    return damage

  def addTree(self):
    location = self.getNextTreeLocation()
    self.forest.addTree(location)

  def getNextTreeLocation(self):
    best_location = None
    best_yield = -1

    for location in self.getFutureSearchLocations():
      simulated_forest = self.forest.copy()
      simulated_forest.addTree(location)
      avg_yield = self.averageYieldFrom(simulated_forest)

      if avg_yield > best_yield:
        best_yield = avg_yield
        best_location = location

    if best_location is None:
      raise RuntimeError('Next Tree Location Not Found')

    return best_location

  def getFutureSearchLocations(self):
      possible_locations = self.forest.getUnoccupiedLocations()
      shuffle(possible_locations)

      max_index = min(self.design_parameter, len(possible_locations))
      search_locations = possible_locations[0:max_index]

      return search_locations
