from random import *
from BruteForce import *
from BranchNBound import *
from MinSpanTree import *
from time import clock

# Change the size value for bigger data set (recommended not larger than 10)
size = 10
# Change weight MAX and MIN for different weights
weight_max = 1000
weight_min = 100

##############################
# Generate Asymmetric Matrix #
##############################
AsymmMatrix = [[randint(weight_min,weight_max) for i in range(size)] for j in range(size)]

for j in range(len(AsymmMatrix)):
	for i in range(len(AsymmMatrix[j])):
		if i == j:
			AsymmMatrix[i][j] = float("inf")

#############################
# Generate Symmetric Matrix #
#############################
SymmbaseMatrix = [[randint(weight_min,weight_max) for i in range(size)] for j in range(size)]

SymmMatrix = [list(map(add, element_b, element_bT)) for element_b, element_bT in zip(SymmbaseMatrix, list(map(list,(zip(*SymmbaseMatrix)))))]


for j in range(len(SymmMatrix)):
	for i in range(len(SymmMatrix[j])):
		if i == j:
			SymmMatrix[i][j] = float("inf")
		else:
			SymmMatrix[i][j] = floor(SymmMatrix[i][j]/2)
