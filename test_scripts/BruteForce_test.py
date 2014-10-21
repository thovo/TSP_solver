from random import *
from BruteForce import *

# Change the size value for bigger data set
size = 5
# Change weigh max and min for different weights
weight_max = 3
weight_min = 1
matrix = [[randint(weight_min,weight_max) for i in range(size)] for j in range(size)]

for j in range(len(matrix)):
	for i in range(len(matrix[j])):
		if i == j:
			matrix[i][j] = 0
			
BruteForce(matrix)
