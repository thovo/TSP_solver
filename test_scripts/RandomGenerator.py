#from random import *
from operator import add
from math import *
from time import clock
from numpy.random import *
from json import *

def random_generator(size = 10, weight_range = 1000, symetric = True, sparsity = 0.0, dis_type = "uniform"):
	weight_max = 2 * weight_range
	weight_min = weight_range
	##############################
	# Generate Asymmetric Matrix #
	##############################
	if (symetric == False):
		if (dis_type == "uniform"):
			AsymmMatrix = [[randint(weight_min,weight_max) for i in range(size)] for j in range(size)]
		elif (dis_type == "normal"):
			AsymmMatrix = [[(int((weight_max - weight_min) * abs(float(normal(0.1,0.1,1))) + weight_min)) for i in range(size)] for j in range(size)]
		
		if (sparsity != 0.0):
			for i in range(len(AsymmMatrix)):
				for j in range(len(AsymmMatrix)):
					if (rand() < sparsity):
						AsymmMatrix[i][j] = float("inf")
		
		for j in range(len(AsymmMatrix)):
			for i in range(len(AsymmMatrix[j])):
				if i == j:
					AsymmMatrix[i][j] = 0
		return AsymmMatrix
	
	#############################
	# Generate Symmetric Matrix #
	#############################
	elif (symetric == True):
		if (dis_type == "uniform"):
			SymmbaseMatrix = [[randint(weight_min,weight_max) for i in range(size)] for j in range(size)]
		elif (dis_type == "normal"):
			#(int((weight_max - weight_min) * random_sample() + weight_min))
			SymmbaseMatrix = [[(int((weight_max - weight_min) * abs(float(normal(0.1,0.1,1))) + weight_min)) for i in range(size)] for j in range(size)]

		
		SymmMatrix = [list(map(add, element_b, element_bT)) for element_b, element_bT in zip(SymmbaseMatrix, list(map(list,(zip(*SymmbaseMatrix)))))]
		
		if (sparsity != 0.0):
			for i in range(len(SymmMatrix)):
				for j in range(len(SymmMatrix)):
					if (rand() < sparsity):
						SymmMatrix[i][j] = float("inf")				
		
		for j in range(len(SymmMatrix)):
			for i in range(len(SymmMatrix[j])):
				if i == j:
					SymmMatrix[i][j] = 0
				else:
					SymmMatrix[i][j] = floor(SymmMatrix[i][j]/2)
		
		return SymmMatrix



#x1 = random_generator(size = 10, weight_max = 1000, weight_min = 10, symetric = True, sparsity = 1.0, dis_type = "normal")
#x2 = random_generator(size = 10, weight_max = 1000, weight_min = 10, symetric = True, sparsity = 0.5, dis_type = "normal")
#x3 = random_generator(size = 10, weight_max = 1000, weight_min = 10, symetric = True, sparsity = 0.0, dis_type = "normal")
#x4 = random_generator(size = 10, weight_max = 1000, weight_min = 10, symetric = False, sparsity = 1.0, dis_type = "uniform")
#x5 = random_generator(size = 10, weight_max = 1000, weight_min = 10, symetric = False, sparsity = 0.5, dis_type = "uniform")
#x6 = random_generator(size = 10, weight_max = 1000, weight_min = 10, symetric = False, sparsity = 0.0, dis_type = "uniform")
size = [5,6,7,8,9,10]
symetric = [True]
weight_ranges = [10,100,1000,10000]
sparsity = [0.0, 0.1,0.2,0.4,0.8]
distribution = ["uniform","normal"]

for size_level in size:
	for sym_type in symetric:
		for wt_range in weight_ranges:
			for sparsity_level in sparsity:
				for distribution_type in distribution:
					x = random_generator(size = size_level, weight_range=wt_range, symetric = sym_type, sparsity = sparsity_level, dis_type = distribution_type)
					file_name = "SIZE" + str(size_level) + "_SYM" + str(sym_type) + "_RANGE" + str(wt_range) + "_SPARSITY" + str(sparsity_level) + "_DIST" + str(distribution_type) + ".json"
					f = open(file_name, 'w')
					dump(x,f)
					f.close()					
