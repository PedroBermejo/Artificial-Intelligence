from helper import helper
from constants import ecuaParms
import matplotlib.pyplot as plt

# ----- START OF EXECUTUION

# 1.- Create random population 100 chromosomes with 6 genes each
population = helper.createPopulation(ecuaParms.minR, 
    ecuaParms.maxR, ecuaParms.chromLength, ecuaParms.popuLength)

matrix = helper.calculateMatrixResults(ecuaParms.result)

results = helper.calculateResults(population, matrix, 
    ecuaParms.divisor)

# 2.- Create graph
helper.createGraphs(population, results, matrix, ecuaParms)

minError = min(results)
mutationP = ecuaParms.mutationPercent

# 3.- Iterate
for i in range(ecuaParms.iterations):
    chosenParents = helper.getChosenParents(population, results, 
        ecuaParms.percent, ecuaParms.parentNum)

    population = helper.bitExchangeReproduction(population, 
        chosenParents, ecuaParms.parentNum, ecuaParms.bits)
    
    helper.mutation(population, mutationP, ecuaParms.bits)

    results = helper.calculateResults(population, matrix, 
        ecuaParms.divisor)
    
    newMinError = min(results)
    if(minError == newMinError):
        #mutationP = 20
        helper.addRandomnes_1(population, ecuaParms)        
        #results = helper.calculateResults(population, matrix, ecuaParms.divisor)

    minError = newMinError
    helper.updateGraphs(i + 1, population, results, matrix, ecuaParms)

plt.show()
