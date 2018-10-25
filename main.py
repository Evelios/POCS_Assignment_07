from HotModel import HotModel

def main():
  size = 32
  D = 3

  yield_curve, best_forest = getYieldCurve(size, D)

def getYieldCurve(grid_size, design_parameter):
  model = HotModel(grid_size, design_parameter)

  forest_yield = [0]
  best_yield = 0
  best_forest = None

  index = 0

  while not model.isFullyPopulated():
    model.addTree()

    current_yield = model.getForestYield()
    forest_yield.append(current_yield)

    if current_yield > best_yield:
      best_yield = current_yield
      best_forest = model.getForestMatrix()

    index += 1
    if index % 10 == 0:
      print('Forest Size : ' + str(model.getNumTrees()))
      print('Yield : ' + str(round(current_yield, 4)))

  return forest_yield, best_forest

if __name__ == '__main__':
  main()