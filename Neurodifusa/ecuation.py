from helper import helper
import numpy as np

# Positions 0, 1, 2 -> cold, warm, hot
mean = [5, 22, 35] 
variance = [7, 7, 7]
pValues = [0.1, 0.4, 1]
qValues = [0, 3, 6]

# ----- START OF EXECUTUION
x = []
yList = [[] for i in range(3)]
resultList = []

for i in np.arange(-20.0, 60.0, 0.1):
    x.append(i)
    for position in range(3):
        yList[position].append(helper.evaluateGaussian(
            i, mean[position], variance[position]))

for i in range(len(x)):
    resultList.append(helper.evaluateFuzzy(
        i, x, yList, pValues, qValues))
    
# Send color parameters and graph
colors = ["g-", "b-", "r-"]
helper.graph(x, yList, colors, resultList)
