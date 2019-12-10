from helper import helper
import numpy as np

# Positions 0, 1, 2 -> cold, warm, hot
xMean = [0, 5, 10] 
xVariance = [2, 2, 2]
yMean = [0, 5, 10] 
yVariance = [2, 2, 2]
pValues = [0.0, 0.6, 0.0, 0.0, 0.8, 0.0, 0.0, 0.5, 0.1]
qValues = [0, 1, 0, 0, 8, 0, 0, 1, 0]
rValues = [0, 2, 0, 0, 5, 0, 0, 2, 0]

# ----- START OF EXECUTUION
x, y = [], []
xGausians, yGausians = [[] for i in range(3)], [[] for i in range(3)]

for i in np.arange(0.0, 10.0, 0.1):
    x.append(i)
    y.append(i)
    for position in range(3):
        xGausians[position].append(helper.evaluateGaussian(
            i, xMean[position], xVariance[position]))
        yGausians[position].append(helper.evaluateGaussian(
            i, yMean[position], yVariance[position]))

zMatrix = [[] for i in range(len(x))]

for xPosition in range(len(x)):
    for yPosition in range(len(y)):
        zMatrix[xPosition].append(
            helper.evaluateFuzzy3D(x[xPosition], y[yPosition], 
            pValues, qValues, rValues, xGausians, yGausians))

# Graph
helper.graph3D(x, y, zMatrix)

# Testing Gausians and 3D Graph
'''
colors = ["g-", "b-", "r-"]
helper.graph(x, xGausians, colors, [])
helper.graph(y, yGausians, colors, [])
helper.graph3D_Example()
'''