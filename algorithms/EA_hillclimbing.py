# The hill climbing function
#Assignment 2
### Some Explanation
## The fitness is defined as the average of all the values in the gene
###
import sys
sys.path.append('../XMLParsingScript')

from pylab import *
from numpy import *
from XmlParserFinal import *
from copy import copy, deepcopy
import random
from time import clock

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


#city_matrix = [[0, 11.0, 11.0, 10.0, inf], [11.0, 0, 11.0, 10.0, 10.0], [11.0, 11.0, 0, 10.0, 10.0], [10.0, 10.0, 10.0, 0, 12.0], [inf, 10.0, 10.0, 12.0, 0]]
#num_cities = 5
#tour = [2, 4, 3, 0, 1]

def check_solution_valid(tour):
    global num_cities
    global city_matrix
    for index in range(num_cities - 1):
        city1 = tour[index]
        city2 = tour[index + 1]
        if (city_matrix[city1][city2] == float("inf")):
            return False
    city1 = tour[num_cities - 1]
    city2 = tour[0]    
    if (city_matrix[city1][city2] == float("inf")):
        return False
    return True

#print check_solution_valid(tour)

def MatrixRandomize():
    global num_cities
    cities_list = range(num_cities)
    while(True):
        x = random.sample(cities_list,num_cities)
        try:
            if (check_solution_valid(x) == True):
                return x
        except:
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
    fitness_sum += city_matrix[tour[num_cities - 1]][tour[0]]
    #print tour
    #print fitness_sum
    return fitness_sum

def MatrixPerturb(tour, prob):
    #print tour
    col_len = len(tour)
    #row_len = len(tour[0])
    #c = v[:] # This does't work ! It still copies the array with its reference, not its value! use deepcopy instead.
    c = deepcopy(tour)
    for j in range(col_len):
        if prob > random.random():
            index_1 = 0
            index_2 = 0
            while (index_1 == index_2):
                index_1 = random.choice(range(col_len))
                index_2 = random.choice(range(col_len))

            swap_value = c[index_1]
            c[index_1] = c[index_2]
            c[index_2] = swap_value
    return c    

#city_matrix = generate_matrices(size = num_cities)
#matrix_read = tsplib_xml_parse('../tsp_lib_xml_datasets/burma14.xml')
#matrix_read = tsplib_xml_parse('../tsp_lib_xml_datasets/br17.xml')
#dataset_name = matrix_read[0]
#num_cities = matrix_read[1]
#city_matrix = matrix_read[2]
num_cities = 0
city_matrix = []
def hillclimbing_algorithm(city_matrix_input, number_cities, num_iter = 1, num_gen = 10000):
    global num_cities
    global city_matrix
    
    city_matrix = city_matrix_input
    num_cities = number_cities

    parent = MatrixCreate(1, num_cities) 
    #print parent
    parent = MatrixRandomize() 
    #print parent
    parentFitness = Fitness(parent) 
    
    number_iterations = num_iter
    number_generations = num_gen
    fits = MatrixCreate(number_iterations,number_generations)
    #print parentFitness
    #best_solution = BruteForce(city_matrix)
    #print ("best solution = ", best_solution)
    start = clock()
    
    best_solution = parent
    best_score = parentFitness
    
    for iteration in range(number_iterations):
        parent = MatrixCreate(1, num_cities)
        parent = MatrixRandomize() 
        parentFitness = Fitness(parent)
        for currentGeneration in range(number_generations):
            #print currentGeneration
            child = MatrixPerturb(parent, 0.05) 
            childFitness = Fitness(child)
            if childFitness < parentFitness:
                parent = child[:] 
                parentFitness = childFitness
            fits[iteration][currentGeneration] = parentFitness
        if (parentFitness < best_score):
            best_score = parentFitness
            best_solution = parent + [parent[0]]
        #print ("EA-HILL ====== parent_after = ",parentFitness)
        #print ("EA-HILL ====== ---------")
    EA_time = clock() - start
    EA_output = ["Evolutionary-HillClimbing",best_score,best_solution,EA_time]
    #print fits
    #figure(1)    
    #plot (range(number_generations),fits[0])
    #ylabel('Fitness')
    #xlabel('Generation')
    #figure(2)
    #imshow(fits, cmap=cm.gray, aspect='auto', interpolation='nearest')
    #ylabel('Gene')
    #xlabel('Generation')
    #figure (3)
    #plot (range(number_generations),fits[0], range(number_generations), fits[1], range(number_generations), fits[2], range(number_generations), fits[3], range(number_generations), fits[4])
    #ylabel('Fitness')
    #xlabel('Generation')
    #show()
    return EA_output
    
#matrix_read = tsplib_xml_parse('../tsp_lib_xml_datasets/gr17.xml')
#dataset_name = matrix_read[0]
#n_c = matrix_read[1]
#c = matrix_read[2]

#print hillclimbing_algorithm(city_matrix_input = c, number_cities = n_c, num_iter = 50, num_gen = 5000)