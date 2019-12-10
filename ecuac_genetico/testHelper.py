from helper import helper 
from constants import ecuaParms

# Test 'createPopulation'
print("Testing createPopulation")
population = helper.createPopulation(0, 255, 3, 10)
results = helper.calculateResults(population, 10, 2, 13)
print(len(population), len(results))
helper.printPopulation(population, results)

# Test 'getChosenParents'
print("Testing getChosenParents")
chosenParents = helper.getChosenParents(population, results, 5, 2)
for i in range(len(chosenParents)):
    print(i, chosenParents[i], results[chosenParents[i]])

# Test 'intToBitArray'
print("Testing intToBitArray")
bitArray_1 = helper.intToBitArray(3, 8)
bitArray_2 = helper.intToBitArray(15, 8)
bitArray_3 = helper.intToBitArray(8, 8)
bitArray_4 = helper.intToBitArray(255, 8)
bitArray_5 = helper.intToBitArray(0, 8)
print("3", bitArray_1)
print("15", bitArray_2)
print("8", bitArray_3)
print("255", bitArray_4)
print("0", bitArray_5)

# Test 'bitArrayToInt'
print("Testing bitArrayToInt")
print("3", helper.bitArrayToInt(bitArray_1))
print("15", helper.bitArrayToInt(bitArray_2))
print("8", helper.bitArrayToInt(bitArray_3))
print("255", helper.bitArrayToInt(bitArray_4))
print("0", helper.bitArrayToInt(bitArray_5))

# Test 'flipBits'
print("Testing flipBits")
parent_1 = [6, 7, 9]
parent_2 = [10, 20, 30]
child_1 = helper.flipBits(parent_1.copy(), parent_2.copy(), 8, 8)
child_2 = helper.flipBits(parent_1.copy(), parent_2.copy(), 16, 8)
child_3 = helper.flipBits(parent_1.copy(), parent_2.copy(), 0, 8)
child_4 = helper.flipBits(parent_1.copy(), parent_2.copy(), 24, 8)
child_5 = helper.flipBits(parent_1.copy(), parent_2.copy(), 4, 8)
child_6 = helper.flipBits(parent_1.copy(), parent_2.copy(), 15, 8)
print("P_1", parent_1)
print("P_2", parent_2)
print("C_1", child_1)
print("C_2", child_2)
print("C_3", child_3)
print("C_4", child_4)
print("C_5", child_5)
print("C_6", child_6)

# Test 'bitExchangeReproduction'
print("Testing bitExchangeReproduction")
population = helper.bitExchangeReproduction(population, chosenParents, 2, 8)
results = helper.calculateResults(population, 10, 2, 13)
print(len(population), len(results))
helper.printPopulation(population, results)
