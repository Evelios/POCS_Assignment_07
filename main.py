import matplotlib.pyplot as plt
import numpy as np
from HotModel import HotModel

def main():
  size = 32

  yield_curve_1, density_1, best_forest_1, best_forest_distribution_1 = getYieldCurve(size, 1)
  yield_curve_2, density_2, best_forest_2, best_forest_distribution_2 = getYieldCurve(size, 2)
  yield_curve_L, density_L, best_forest_L, best_forest_distribution_L = getYieldCurve(size, size)
  yield_curve_L_2, density_L_2, best_forest_L_2, best_forest_distribution_L_2 = getYieldCurve(size, size*size)

  # ---- Yield Curve ----

  fig = plt.figure()
  ax = plt.axes()
  ax.set(title='HOT Model Yield Curve For L=' + str(size), xlabel='Tree Density', ylabel='Forest Average Yield')

  ax.plot(density_1, yield_curve_1, label='D=1')
  ax.plot(density_2, yield_curve_2, label='D=2')
  ax.plot(density_L, yield_curve_L, label='D=L')
  ax.plot(density_L_2, yield_curve_L_2, label='D=L^2')

  ax.legend()

  # ---- Tree Yield Curve Plotting

  fig2 = plt.figure(2)

  ax2 = plt.subplot(2, 2, 1)
  ax2.set_title('D = 1')
  ax2.imshow(simplifyMatrix(best_forest_1))

  ax2 = plt.subplot(2, 2, 2)
  ax2.set_title('D = 2')
  ax2.imshow(simplifyMatrix(best_forest_2))

  ax2 = plt.subplot(2, 2, 3)
  ax2.set_title('D = L')
  ax2.imshow(simplifyMatrix(best_forest_L))

  ax2 = plt.subplot(2, 2, 4)
  ax2.set_title('D = L^2')
  ax2.imshow(simplifyMatrix(best_forest_L_2))

  fig3 = plt.figure(3)
  ax3 = plt.axes() 
  ax3.set(title='Tree Distributions At Peak Yield', xlabel='Size', ylabel='Frequency')

  ax3.scatter(best_forest_distribution_1.keys(), best_forest_distribution_1.values(), label='D=1')
  ax3.scatter(best_forest_distribution_2.keys(), best_forest_distribution_2.values(), label='D=2')
  ax3.scatter(best_forest_distribution_L.keys(), best_forest_distribution_L.values(), label='D=L')
  ax3.scatter(best_forest_distribution_L_2.keys(), best_forest_distribution_L_2.values(), label='D=L^2')

  ax3.legend()

  plt.show()

def getYieldCurve(grid_size, design_parameter):
  model = HotModel(grid_size, design_parameter)

  forest_yield = [0]
  density = [0]
  best_yield = 0
  best_forest = None
  best_forests = None

  index = 0

  while not model.isFullyPopulated():
    model.addTree()

    current_yield = model.getForestYield()
    forest_yield.append(current_yield)
    density.append(model.getNormalizedNumTrees())

    if current_yield > best_yield:
      best_yield = current_yield
      best_forest = model.getForestMatrix()
      best_forests = model.getForests()

    index += 1
    if index % 10 == 0:
      print('Forest Size : ' + str(model.getNumTrees()))
      print('Yield : ' + str(round(current_yield, 4)))

  best_forest_sizes = [len(forest) for forest in best_forests]
  best_forest_sizes.sort()
  best_forest_distribution = {x:best_forest_sizes.count(x) for x in best_forest_sizes}

  return forest_yield, density, best_forest, best_forest_distribution

def simplifyMatrix(matrix):
  return np.where(matrix > 0, 1, 0)

if __name__ == '__main__':
  main()