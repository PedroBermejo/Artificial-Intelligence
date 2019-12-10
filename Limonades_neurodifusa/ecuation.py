from helper import helper
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

zResult = [[4, 2, 0, 0, 0],
           [5, 6, 5, 2, 0],
           [6, 6, 5, 5, 3],
           [5, 6, 6, 6, 4],
           [4, 7, 6, 5, 5]]

x, y = [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]
mutationPercent, iterations, tournamentPercent = 100, 500, 50

# Positions in genetic algorithm
# [0-5 xyMean, 6-11 xyVariance,  12-20 pValues, 21-29 qValues, 30-38 rValues]
# Values between 0 and 5 so if 8 bit = 255 then 255/51 = max 5
population = helper.createPopulation(39, 1000)
#helper.printPopulation(popoulation)


# Evaluate aptitud functions and get min error
results = helper.calculateResults(x, y, population, zResult, 51)
minInd = results.index(min(results))

# Get best matrix to graph
bestChrom = helper.divideByFactor(population[minInd], 51)
zBestChrom = helper.aptitudFunction(bestChrom, x, y)

# 3D printing
#print(zBestChrom)
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = helper.graph3D(fig, x, y, zResult, zBestChrom, results[minInd])

acumError = results[minInd]
# 3.- Iterate
for i in range(iterations):
    chosenParents = helper.getChosenParents(population, results, 
        tournamentPercent, 2)

    population = helper.bitExchangeReproduction(population, 
        chosenParents, 2, 8)
    
    helper.mutation(population, mutationPercent, 8)

    results = helper.calculateResults(x, y, population, zResult, 51)
    minInd = results.index(min(results))

    # Get best matrix to graph
    bestChrom = helper.divideByFactor(population[minInd], 51)
    zBestChrom = helper.aptitudFunction(bestChrom, x, y)
    helper.updateGraph3D(ax, x, y, zBestChrom, results[minInd])
    print("Iteration:", i, "Min error:", results[minInd])
    #print(bestChrom)

    if (acumError == results[minInd]):
        addChrom = helper.createPopulation(39, 5)
        for i in range(len(addChrom)):
            position = random.randint(0, len(population) -1)
            population[position] = addChrom[i]
    acumError = results[minInd]
    
plt.show()


'''
# Testing Gausians and 3D Graph
colors = ["g-", "b-", "r-"]
helper.graphGausians(x, y,  xGausians, yGausians)

# Test 3D grapgh
helper.graph3D_Example()
'''