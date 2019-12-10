from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import random
import operator
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

class helper:

    # Print population for testing
    def printPopulation(population):
        print("Length:", len(population))
        for i in range(len(population)):
            print(i, len(population[i]), population[i])

    # Print population for testing
    def printPopulationWithResults(population, result):
        print("Length:", len(population))
        for i in range(len(population)):
            print(i, len(population[i]), '{:,}'.format(result[i]), population[i])

    # creates population base on list (chormosoma) 
    # and given length
    def createPopulation(chromLength, popuLength):
        population = []
        for i in range(popuLength):
            chrom = []
            for j in range(chromLength):
                chrom.append(random.randint(0, 255))
            population.append(chrom)
        return population
 
    def evaluateGaussian(x, mean, desv):
        if (desv == 0):
            desv = 0.0001
        return np.exp(-0.5*((x-mean)/desv)**2)

    # [0-5 xyMean, 6-11 xyVariance,  12-20 pValues, 21-29 qValues, 30-38 rValues]
    def generateGaussians(length, chrom):
        xGausians, yGausians = [[] for i in range(3)], [[] for i in range(3)]
        for i in range(length):
            for position in range(3):
                xGausians[position].append(helper.evaluateGaussian(
                    i, chrom[position], chrom[position +6]))
                yGausians[position].append(helper.evaluateGaussian(
                    i, chrom[position +3], chrom[position +9]))
        return (xGausians, yGausians)

    def divideByFactor(chrom, div):
        result = []
        for i in chrom:
            result.append(i/div)
        return result

    def evaluateFuzzy3D(x, y, pValues, qValues, rValues, xGausians, yGausians):
        a, b = 0, 0
        paramPosition = 0
        for xPosition in range(len(xGausians)):
            for yPosition in range(len(yGausians)):
                a = (a + (pValues[paramPosition] * x  + 
                    qValues[paramPosition] * y + 
                    rValues[paramPosition]) *  xGausians[xPosition][x] *
                    yGausians[yPosition][y])
                b = b + xGausians[xPosition][x] * yGausians[yPosition][y]
                paramPosition = paramPosition + 1
        #print("a, b, a/b", a, b, a / b)
        return a / b 

    def aptitudFunction(chrom, x, y):
        zMatrix = [[] for i in range(len(x))]
        (xGausians, yGausians) = helper.generateGaussians(5, chrom)
        for xInd in x:
            for yInd in y:
                zMatrix[xInd].append(helper.evaluateFuzzy3D(xInd, yInd, 
                    chrom[12:21], chrom[21:30], chrom[30:], xGausians, yGausians))
        return zMatrix

    def calculateResults(x, y, population, zResult, div):
        results = []
        for chrom in population:
            absolute = 0
            newChrom = helper.divideByFactor(chrom, div)
            zChrom = helper.aptitudFunction(newChrom, x, y)
            for xInd in x:
                for yInd in y:
                    diff = zResult[xInd][yInd] - zChrom[xInd][yInd]
                    absolute += abs(diff)
            results.append(absolute)
        return results

    def intToBitArray(number, bits):
        mask = []
        for i in range(bits):
            mask.append(0)
        arrayBits = [int(i) for i in list('{0:0b}'.format(number))]
        position = bits - len(arrayBits)
        return mask[0:position] + arrayBits
    
    def bitArrayToInt(bitArray):
        return int("".join(str(x) for x in bitArray), 2)

    def flipBits(parent_1, parent_2, position, bits):
        child = []
        mod = position % bits
        if ( mod == 0):
            pos = int(position / bits)
            child = parent_1[0:pos] + parent_2[pos:]
        else:
            pos = int(position / bits)
            bit_1 = helper.intToBitArray(parent_1[pos], bits)
            bit_2 = helper.intToBitArray(parent_2[pos], bits)
            newBitArray = bit_1[0:mod] + bit_2[mod:]
            newNumber = helper.bitArrayToInt(newBitArray)
            child = parent_1[0:pos] + [newNumber] + parent_2[pos+1:]
            #print("parent_1", parent_1)
            #print("parent_2", parent_2)
            #print("bit_1", position, bit_1, mod)
            #print("bit_2", position, bit_2, mod)
            #print("newBitArray", newBitArray, newNumber)
        return child
 
    def bitExchangeReproduction(population, chosenParents, parentNum, bits):
        newPopulation = []
        for i in range(len(population)):
            ind = i * parentNum
            if (parentNum == 2):
                #random.seed(datetime.now())
                position = random.randint(0, len(population[i])*bits)
                #print("position", position)
                child = helper.flipBits(population[chosenParents[ind]].copy(), 
                    population[chosenParents[ind+1]].copy(), position, bits)
            newPopulation.append(child)
        return newPopulation

    # Gets 5 random numbers (0 - 99) and chooses the
    # best (lower) result
    def getBestInTournament(erros, percent):
        selection =  []
        while len(selection) < percent:
            #random.seed(datetime.now())
            value = random.randint(0, len(erros) -1)
            if value not in selection:
                selection.append((value, erros[value]))
        return min(selection, key=operator.itemgetter(1))

    def getChosenParents(population, results, percent, parentNum):
        chosenParents = []
        while len(chosenParents) < len(population)*parentNum:
            winer = helper.getBestInTournament(results, percent)
            if ((len(chosenParents) == 0) or (chosenParents[-1] != winer[0])):
                chosenParents.append(winer[0])
        return chosenParents

    def changeBit(bitArray, bitPosition):
        if (bitArray[bitPosition] == 0):
                bitArray[bitPosition] = 1
        else:
            bitArray[bitPosition] = 0

    def mutation(population, mutationPercent, bits):
        for i in range(mutationPercent):
            #random.seed(datetime.now())
            chromInd = random.randint(0, len(population) -1)
            chromPosition = random.randint(0, len(population[chromInd]) -1)
            bitPosition = random.randint(0, bits -1)
            bitArray = helper.intToBitArray(
                population[chromInd][chromPosition], bits)
            #print("Before:", population[chromInd][chromPosition], bitArray)
            helper.changeBit(bitArray, bitPosition)
            population[chromInd][chromPosition] = helper.bitArrayToInt(bitArray)
            #print("After:", population[chromInd][chromPosition], bitArray)


    def graphGausians(x, y, xGausians, yGausians):
        fig, ax = plt.subplots(2, 1, figsize=(12,5))
        ax[0].set_xlabel('X')
        ax[0].set_ylabel('Y')
        ax[0].axis([-5, 10, 0, 1.1])
        ax[1].set_xlabel('X')
        ax[1].set_ylabel('Y')
        ax[1].axis([-5, 10, 0, 1.1])
        for i in range(len(xGausians)):
            ax[0].plot(x, xGausians[i])
            ax[1].plot(y, yGausians[i])
        plt.show()

    def graph3D(fig, x, y, zResult, zMatrix, error):
        X, Y = np.meshgrid(x, y)
        Z = np.array(zResult)
        
        ax = fig.add_subplot(1, 2, 1, projection='3d')
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
        ax.set_xlabel('Lemon (x)')
        ax.set_ylabel('Sugar (y)')
        ax.set_zlabel('Taste level (z)')
        ax.set_title('Expected')

        Z = np.array(zMatrix)
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
        ax.set_xlabel('Lemon (x)')
        ax.set_ylabel('Sugar (y)')
        ax.set_zlabel('Taste level (z)')
        ax.set_title('Error: ' + str(error))
        plt.pause(0.001)
        return ax

    def updateGraph3D(ax, x, y, zMatrix, error):
        X, Y = np.meshgrid(x, y)
        Z = np.array(zMatrix)
        ax.cla()
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
        ax.set_xlabel('Lemon (x)')
        ax.set_ylabel('Sugar (y)')
        ax.set_zlabel('Taste level (z)')
        ax.set_title('Error: ' + str(error))
        plt.pause(0.001)
        

    def graph3D_Example():
        x = [0, 1, 2]
        y = [0, 1, 2]
        zMatrix = [
            [0, 1, 0],
            [1, 2, 1],
            [0, 1, 0]]
 
        X, Y = np.meshgrid(x, y)
        Z = np.array(zMatrix)
 
        fig = plt.figure(figsize=plt.figaspect(0.5))
        ax = fig.add_subplot(1, 2, 1, projection='3d')
        ax.plot_surface(X, Y, Z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('History')
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Algorithm')
        plt.show()


            

