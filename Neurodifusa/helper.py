from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

class helper:

    def evaluateGaussian(x, c, desv):
        return np.exp(-0.5*((x-c)/desv)**2)

    def evaluateFuzzy(i, x, yList, pValues, qValues):
        a, b = 0, 0
        for position in range(len(yList)):
            a = a + (pValues[position] * x[i]  +
                qValues[position]) * yList[position][i]
            b = b + yList[position][i]
            
        #print("a, b, a/b", a, b, a / b)
        return a / b 


    def graph(x, yList, colorsParams, resultList):
        fig, ax = plt.subplots(2, 1, figsize=(12,5))
        ax[0].set_xlabel('X')
        ax[0].set_ylabel('Y')
        ax[0].axis([-30, 70, 0, 1.1])
        ax[1].set_xlabel('X')
        ax[1].set_ylabel('Y')
        ax[1].axis([-10, 60, 0, 100])
        
        for i in range(len(x)):
            for position in range(len(yList)):
                ax[0].plot(x, yList[position], 
                    colorsParams[position])

        if(len(resultList) > 0 ):
            ax[1].plot(x, resultList, colorsParams[0])

        plt.show()
        
    def evaluateFuzzy3D(x, y, pValues, qValues, rValues, xGausians, yGausians):
        a, b = 0, 0
        paramPosition = 0
        for xPosition in range(len(xGausians)):
            for yPosition in range(len(yGausians)):
                a = (a + (pValues[paramPosition] * x  + 
                    qValues[paramPosition] * y + 
                    rValues[paramPosition]) *  xGausians[xPosition][int(x*10)] *
                    yGausians[yPosition][int(y*10)])
                b = b + xGausians[xPosition][int(x*10)] * yGausians[yPosition][int(y*10)]
                paramPosition = paramPosition + 1
        #print("a, b, a/b", a, b, a / b)
        return a / b 

    def graph3D(x, y, zMatrix):
        X, Y = np.meshgrid(x, y)
        Z = np.array(zMatrix)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()

    def graph3D_Example():
        x = [0, 1, 2]
        y = [0, 1, 2]
        zMatrix = [
            [1, 1, 1],
            [1, 2, 1],
            [1, 1, 1]]
        print(x, y)
        print(zMatrix)
        X, Y = np.meshgrid(x, y)
        Z = np.array(zMatrix)
        print(X)
        print(Y)
        print(Z)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()




            

