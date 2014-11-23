# The hill climbing function
#Assignment 2
### Some Explanation
## The fitness is defined as the average of all the values in the gene
###
from pylab import *
from numpy import *
from XmlParserFinal import *
from copy import copy, deepcopy
import random
from BruteForce import *

general_counter = 0
general_counter_2 = 0

num_cities = 10

def generate_matrices(size = 5):
    # Change the size value for bigger data set
    #size = 5
    # Change weigh max and min for different weights
    weight_max = 3
    weight_min = 1
    matrix = [[randint(weight_min,weight_max) for i in range(size)] for j in range(size)]
    
    for j in range(len(matrix)):
	for i in range(len(matrix[j])):
	    if i == j:
		matrix[i][j] = 0    
		
    return matrix

def MatrixCreate(rows, columns):
    #Matrix = zeros( (rows,columns) )
    #one_col = [[None
    #print one_col
    ##Matrix = [0]  for j in range(columns)
    #Matrix = list()
    #for i in range(columns):
	#Matrix.append([])
    Matrix = [[None for i in range(columns)] for j in range(rows)]
    #print Matrix
    return Matrix

def check_solution_valid(tour):
    global num_cities
    global city_matrix
    for index in range(num_cities - 1):
        city1 = tour[index]
        city2 = tour[index + 1]
	if (city_matrix[city1][city2] == float("inf")):
	    return False
    return True
    
def MatrixRandomize():
    global num_cities
    cities_list = range(num_cities)
    while(True):
        x = random.sample(cities_list,num_cities)
	if (check_solution_valid(x) == True):
	    return x
    raise ValueError("No good tour")

def Fitness(tour):
    global num_cities
    global city_matrix
    fitness_sum = 0.0
    for index in range(num_cities - 1):
        city1 = tour[index]
        city2 = tour[index + 1]
	link_len = city_matrix[city1][city2]
	fitness_sum += link_len
    #fitness_sum = sum(v)
    #print tour
    #print fitness_sum
    return fitness_sum

def MatrixPerturb(tour, prob):
    global general_counter
    global general_counter_2
    #print tour
    col_len = len(tour)
    #row_len = len(tour[0])
    #c = v[:] # This does't work ! It still copies the array with its reference, not its value! use deepcopy instead.
    c = deepcopy(tour)
    for j in range(col_len):
	general_counter_2 += 1
	if prob > random.random():
	    index_1 = 0
	    index_2 = 0
	    while (index_1 == index_2):
		index_1 = random.choice(range(col_len))
		index_2 = random.choice(range(col_len))
	    
	    swap_value = c[index_1]
	    c[index_1] = c[index_2]
	    c[index_2] = swap_value
	    general_counter += 1
    return c    

#city_matrix = generate_matrices(size = num_cities)
matrix_read = tsplib_xml_parse('../tsp_lib_xml_datasets/burma14.xml')
dataset_name = matrix_read[0]
num_cities = matrix_read[1]
city_matrix = matrix_read[2]
#print city_matrix

parent = MatrixCreate(1, num_cities) 
#print parent
parent = MatrixRandomize() 
#print parent
parentFitness = Fitness(parent) 

number_iterations = 50
number_generations = 5000
fits = MatrixCreate(number_iterations,number_generations)
#print parentFitness
#best_solution = BruteForce(city_matrix)
#print ("best solution = ", best_solution)
for iteration in range(number_iterations):
    parent = MatrixCreate(1, num_cities)
    parent = MatrixRandomize() 
    parentFitness = Fitness(parent)     
    print ("parent_before = ",parentFitness)
    #print ("best solution = ", best_solution)
    for currentGeneration in range(number_generations):
        #print currentGeneration, parentFitness 
        child = MatrixPerturb(parent, 0.05) 
        childFitness = Fitness(child) 
        if childFitness < parentFitness:
            parent = child[:] 
            parentFitness = childFitness
            #print currentGeneration, parentFitness 
	#print currentGeneration
        fits[iteration][currentGeneration] = parentFitness
    print ("parent_after = ",parentFitness)
    print ("---------")
#print fits
#print general_counter
#print general_counter_2
figure(1)    
plot (range(number_generations),fits[0])
ylabel('Fitness')
xlabel('Generation')
figure(2)
imshow(fits, cmap=cm.gray, aspect='auto', interpolation='nearest')
ylabel('Gene')
xlabel('Generation')
figure (3)
plot (range(number_generations),fits[0], range(number_generations), fits[1], range(number_generations), fits[2], range(number_generations), fits[3], range(number_generations), fits[4])
ylabel('Fitness')
xlabel('Generation')
show()
