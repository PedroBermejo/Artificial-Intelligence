from helper import helper 

# Test 'inversionReproduction'
print("Testing inversionReproduction")
parent = list(range(1, 21))
print(parent)
child = helper.inversionReproduction(parent.copy())
print(child)

# Test 'flipReproduction'
print("Testing flipReproduction")
parent = list(range(1, 21))
print(parent)
child = helper.flipReproduction(parent.copy())
print(child)

# Test 'getTotalDistance'
print("Testing getTotalDistance")
chrom = [20, 2, 3, 19, 16, 12, 17, 18, 6, 9, 1, 15, 7, 13, 4, 5, 14, 10, 11, 8]
distance = helper.getTotalDistance(chrom)
print(chrom)
print(distance)

# Test 'getTotalDistance' proposed in class
print("Testing getTotalDistance proposed in class")
chrom = [4, 10, 8, 2, 20, 1, 13, 7, 15, 9, 6, 18, 17, 12, 16, 19, 3, 11, 14, 5]
distance = helper.getTotalDistance(chrom)
print(chrom)
print(distance)