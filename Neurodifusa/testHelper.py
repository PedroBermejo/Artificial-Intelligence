from helper import helper 
from constants import ecuaParms

# Test 'aptitudFunction'
print("Testing aptitudFunction")
y = helper.aptitudFunction(ecuaParms.result, 2.9)
print("Ecuation:", ecuaParms.result, 
    "x:", 2.9, "y:", y)

# Test 'divideByFactor'
print("Testing divideByFactor")
chrom = [3, 30, 56, 70, 250]
divChrom = helper.divideByFactor(chrom, 3)
print(chrom)
print(divChrom)

# Test 'createPopulation'
print("Testing createPopulation")
population = helper.createPopulation(1, 255, 6, 10)
print(population)

# Test 'calculateMatrixResults'
print("Testing calculateMatrixResults")
matrix = helper.calculateMatrixResults(ecuaParms.result)
print(matrix[0], matrix[1], len(matrix))


# Test 'calculateResults'
print("Testing calculateResults")
testPopulation = [[10, 25, 3, 70, 10, 6]]
results = helper.calculateResults(testPopulation, matrix, 3)
helper.printPopulation(testPopulation, results)
testPopulation = [[10, 25, 3, 70, 10, 8]]
results = helper.calculateResults(testPopulation, matrix, 3)
helper.printPopulation(testPopulation, results)

# Test 'intToBitArray' and 'bitArrayToInt'
print("Testing intToBitArray and bitArrayToInt")
bit_1 = helper.intToBitArray(89, 8)
bit_2 = helper.intToBitArray(7, 8)
print("bit:", bit_1, "number:", helper.bitArrayToInt(bit_1))
print("bit:", bit_2, "number:", helper.bitArrayToInt(bit_2))

# Test 'flipBits'
print("Testing flipBits")
parent_1 = [100, 250, 89, 7, 10, 8]
parent_2 = [1, 2, 7, 70, 80, 90]
print("parent_1", parent_1)
print("parent_2", parent_2)
child_1 = helper.flipBits(parent_1, parent_2, 8, 8)
print("position:", 8, child_1)
child_2 = helper.flipBits(parent_1, parent_2, 0, 8)
print("position:", 0, child_2)
child_3 = helper.flipBits(parent_1, parent_2, 48, 8)
print("position:", 48, child_3)
child_4 = helper.flipBits(parent_1, parent_2, 20, 8)
print("position:", 20, child_4)

# Test 'getBestInTournament'
print("Testing getBestInTournament")
testErrors = [12, 23, 24, 54, 9, 2, 43, 31, 59, 100, 121, 38]
print("errors:", testErrors)
print("5%:", helper.getBestInTournament(testErrors, 5))
print("3%:", helper.getBestInTournament(testErrors, 3))
print("2%:", helper.getBestInTournament(testErrors, 2))
print("1%:", helper.getBestInTournament(testErrors, 1))


# Test 'bitExchangeReproduction'
print("Testing bitExchangeReproduction")
results = helper.calculateResults(population, matrix, 3)
helper.printPopulation(population, results)
chosen = helper.getChosenParents(population, results, 5, 2)
print("chosen parents:", chosen)
newPopulation = helper.bitExchangeReproduction(population, chosen, 2, 8)
newResults = helper.calculateResults(newPopulation, matrix, 3)
helper.printPopulation(newPopulation, newResults)

# Test 'mutation'
print("Testing mutation")
mutationPopulation = [
    [1, 2, 3, 4], 
    [32, 45, 65, 76], 
    [109, 209, 250, 199] ]
print(mutationPopulation)
helper.mutation(mutationPopulation, 2, 8)
print(mutationPopulation)

