from HotModel import HotModel

grid_size = 32
design_parameter = 3
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

print(best_forest)
