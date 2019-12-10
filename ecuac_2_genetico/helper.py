import matplotlib.pyplot as plt
import random
import operator
import numpy as np
from datetime import datetime

class helper:
    # Print population for testing
    def printPopulation(population, result):
        for i in range(len(population)):
            print(i, population[i], '{:,}'.format(result[i]))

    # creates population base on list (chormosoma) 
    # and given length
    def createPopulation(minR, maxR, chromLength, popuLength):
        population = []
        for i in range(popuLength):
            chrom = []
            for j in range(chromLength):
                chrom.append(random.randint(minR, maxR))
            population.append(chrom)
        return population

    def divideByFactor(chrom, div):
        result = []
        for i in chrom:
            result.append(i/div)
        return result

    # A*(B*sen(x/C) + D*cos(x/E)) + F*x - D
    def aptitudFunction(chrom, x):
        if(chrom[2] == 0):
            chrom[2] = 0.1
        if(chrom[4] == 0):
            chrom[4] = 0.1
        return chrom[0]*(chrom[1]*np.sin(x/chrom[2]) + 
            chrom[3]*np.cos(x/chrom[4])) + chrom[5]*x - chrom[3]

    def calculateResults(population, matrix, div):
        results = []
        for chrom in population:
            absolute = 0
            newChrom = helper.divideByFactor(chrom, div)
            for x in np.arange(0.0, 100.0, 0.1):
                diff = (matrix[int(x*10)] - 
                    helper.aptitudFunction(newChrom, x))
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

    def printEcuation(ax, chrom, matrix, divisor):
        x, x_2, y, y_2 = [], [], [], []
        ax[1].cla()
        ax[1].set_xlabel('X axis')
        ax[1].set_ylabel('Y axis')
        ax[1].title.set_text("Ecuations")
        for i in np.arange(0.0, 100.0, 0.1):
            x.append(i)
            y.append(matrix[int(i*10)])
        ax[1].plot(x, y, 'b-')
        newChrom = helper.divideByFactor(chrom, divisor)
        for i in np.arange(0.0, 100.0, 0.1):
            x_2.append(i)
            y_2.append(helper.aptitudFunction(newChrom, i))
        ax[1].plot(x_2, y_2, 'g-.')
        plt.pause(0.001)

    def createGraphs(population, results, matrix, ecuaParms):
        minIndx = results.index(min(results))
        print("MinError:", '{:,}'.format(results[minIndx]))
        # History Figure
        global fig, ax 
        fig, ax = plt.subplots(1, 2, figsize=(12,5))
        ax[0].set_xlabel('X generations')
        ax[0].set_ylabel('Y error')
        ax[0].title.set_text("History")
        ax[0].axis([0, ecuaParms.iterations + 1, 0, results[minIndx]])
        ax[0].scatter(1, results[minIndx])
        # Ecuation Figure
        ax[1].axis([0, ecuaParms.iterations + 1, 0, 100])
        helper.printEcuation(ax, population[minIndx], 
            matrix, ecuaParms.divisor)

    def updateGraphs(i, population, results, matrix, ecuaParms):
        # Update history graph
        minIndx = results.index(min(results))
        print("MinError:", '{:,}'.format(results[minIndx]))
        ax[0].scatter(i, results[minIndx])
        # Replace coordenates graph
        helper.printEcuation(ax, population[minIndx], 
            matrix, ecuaParms.divisor)

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

    def calculateMatrixResults(chromResult):
        matrix = []
        for x in np.arange(0.0, 100.0, 0.1):
            y = helper.aptitudFunction(chromResult, x)
            matrix.append(y)
        return matrix

    def addRandomnes_1(population, ecuaParms):
        newPopulation = helper.createPopulation(ecuaParms.minR, 
            ecuaParms.maxR, ecuaParms.chromLength, ecuaParms.randomnes)
        for i in range(len(newPopulation)):
            position = random.randint(0, len(population) -1)
            population[position] = newPopulation[i]

    def addRandomnes_2(population, ecuaParms):
        for i in range(ecuaParms.randomnes):
            position = random.randint(0, len(population) -1)
            for x in range(len(population[position])):    
                population[position][x] = population[position][x]+5
        
    def addRandomnes_3(population, ecuaParms):
        for i in range(ecuaParms.randomnes):  
            position = random.randint(0, len(population) -1) 
            for x in range(len(population[position])):
                population[i][x] = population[i][x] + 1





            

