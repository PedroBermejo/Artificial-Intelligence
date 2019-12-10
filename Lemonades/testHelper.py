from helper import helper 

zResult = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

x, y = [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]
# 0-2 xMean, 3-5 yMean, 6-8 xVariance, 9-11
xyMeanVariance = [0, 2, 4, 0, 2, 4, 1, 1, 1, 1, 1, 1]
zeros =   [0, 0, 0, 0, 0, 0, 0, 0, 0]
pValues = [1, 1, 1, 1, 1, 1, 1, 1, 1]
qValues = [1, 1, 1, 1, 1, 1, 1, 1, 1]
rValues = [1, 1, 1, 1, 1, 1, 1, 1, 1]

population = []
population.append(xyMeanVariance + zeros + zeros + rValues)
population.append(xyMeanVariance + pValues + qValues + rValues)

# Generate Gausians
print("Test Generate Gausians")
xGausians, yGausians = helper.generateGaussians(5, 
    xyMeanVariance)
print("xGausians", xGausians)
print("yGausians", yGausians)


# Evaluate 
print("Evaluate Fuzzy3D")
print("x=0, y=0", helper.evaluateFuzzy3D(0, 0, pValues, qValues, rValues, 
    xGausians, yGausians))
print("x=2, y=2", helper.evaluateFuzzy3D(2, 2, pValues, qValues, rValues, 
    xGausians, yGausians))
print("x=4, y=4", helper.evaluateFuzzy3D(4, 4, pValues, qValues, rValues, 
    xGausians, yGausians))

# Funcion de aptitud
print("Evaluate aptitud")
zMatrix = helper.aptitudFunction(population[1], x, y)
for i in range(len(zMatrix)):
    print(zMatrix[i])
zMatrix = helper.aptitudFunction(population[0], x, y)
for i in range(len(zMatrix)):
    print(zMatrix[i])

# Test calculate results
print("Calculate results")
results = helper.calculateResults(x, y, population[0:1], zResult, 1)
print(results)