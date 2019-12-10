from helper import helper
from constants import ecuaParms
import matplotlib.pyplot as plt

# ----- START OF EXECUTUION

# 1.- Create random population 100 chromosomes with 3 genes each
population = helper.createPopulation(ecuaParms.minR, 
    ecuaParms.maxR, ecuaParms.chromLength, ecuaParms.popuLength)
results = helper.calculateResults(population, ecuaParms.divisor, 
    ecuaParms.x, ecuaParms.y)

#print("-------INITIAL STATE------")

# 1.a- Call graphs and graph the best 
# First generation
helper.createGraphs(population, results, ecuaParms)

for i in range(ecuaParms.iterations):
    
    # 2.- Compete, get chosen parents
    chosenParents = helper.getChosenParents(population, results,
        ecuaParms.percent, ecuaParms.parentNum)

    # 3.- Reproduction, replace population with children
    population = helper.bitExchangeReproduction(population, 
        chosenParents, ecuaParms.parentNum, ecuaParms.bits)
    results = helper.calculateResults(population, ecuaParms.divisor, 
        ecuaParms.x, ecuaParms.y)

    # 3.a- Get the best and graph
    helper.updateGraphs(i+1, population, results, ecuaParms)

# 4.- Print and graph the best of all times
#helper.printBest()

plt.show()

#print("-------FINAL STATE------")
#helper.printPopulation(population, distances)




