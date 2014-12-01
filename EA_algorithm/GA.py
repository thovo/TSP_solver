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
from collections import *
import operator

pop_size = 2000
number_iterations = 1
number_generations = 600
num_siblings = 5
cluster_size = pop_size/num_siblings

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
    Matrix = [[None for i in range(columns)] for j in range(rows)]
    return Matrix

def check_solution_valid(tour):
    global num_cities
    global city_matrix
    for index in range(num_cities - 1):
        city1 = tour[index]
        city2 = tour[index + 1]
        if (city_matrix[city1][city2] == float("inf")):
            return False
    if (city_matrix[num_cities - 1][0] == float("inf")):
        return False    
    return True

def MatrixRandomize(population_size):
    global num_cities
    cities_list = range(num_cities)
    final_list = []
    for i in range(population_size):
        good_sol = False
        while(~good_sol):
            x = random.sample(cities_list,num_cities)
            if (check_solution_valid(x) == True):
                final_list.append(x)
                good_sol = ~good_sol
    return final_list
    #raise ValueError("No good tour")

def Fitness(tours,pop_size):
    global num_cities
    #global pop_size
    global city_matrix
    fitness_sum = [0.0 for j in range(pop_size)]
    #print fitness_sum
    fitness_sum_index = 0
    for tour in tours:
        for index in range(num_cities - 1):
            city1 = tour[index]
            city2 = tour[index + 1]
            link_len = city_matrix[city1][city2]
            fitness_sum[fitness_sum_index] += link_len
        fitness_sum[fitness_sum_index] += city_matrix[tour[num_cities - 1]][tour[0]]
        fitness_sum_index += 1
    return fitness_sum


def best_inv(parents,parentsFitness,pop_size,num_cities):
    #Get the index of the best fitness
    min_index, min_value = min(enumerate(parentsFitness), key=operator.itemgetter(1))
    #Get the individual with the same index
    min_tour = parents[min_index]
    #Return the list of both ()
    return [min_tour,min_value,min_index]

def cluster_select(tours):
    # Take n random sample
    global pop_size
    global num_siblings
    global num_cities
    best_indiviuals = []
    next_generation = []
    for i in range(0,pop_size,num_siblings):
        sub_tour = tours[i:i+5]
        subtourFitness = Fitness(sub_tour,num_siblings) 
        [best_performer,best_score,index_best] = best_inv(sub_tour,subtourFitness,num_siblings,num_cities)
        copy_best_performer = deepcopy(best_performer)
        #Generate 2 random indices for use in the mutation
        index_1 = 0
        index_2 = 0
        while (index_1 == index_2):
            index_1 = random.choice(range(num_cities))
            index_2 = random.choice(range(num_cities))
        index = [index_1,index_2]  

        #Start the mutation process
        for j in range(num_siblings):
            copy_best_performer = deepcopy(best_performer)
            if (j == 0): #point mutations
                swap_value = copy_best_performer[index_1]
                copy_best_performer[index_1] = copy_best_performer[index_2]
                copy_best_performer[index_2] = swap_value      
            elif (j == 1):  #flip the middle segment
                if (index_1 > index_2):
                    #print copy_best_performer
                    #print index_1
                    #print index_2
                    copy_best_performer[index_2 : index_1] = reversed(copy_best_performer[index_2 : index_1])
                else:
                    copy_best_performer[index_1 : index_2] = reversed(copy_best_performer[index_1 : index_2])
            elif (j == 2): # switch a random segment
                if (index_1 < index_2):
                    part_1 = copy_best_performer[:index_1]
                    part_2 = copy_best_performer[index_2:]
                    middle_part = copy_best_performer[index_1:index_2]
                    copy_best_performer = part_2 + middle_part + part_1
                else:
                    part_1 = copy_best_performer[:index_2]
                    part_2 = copy_best_performer[index_1:]
                    middle_part = copy_best_performer[index_2:index_1]
                    copy_best_performer = part_2 + middle_part + part_1                    
            elif (j == 3): #shift
                copy_best_performer = deque(copy_best_performer)
                copy_best_performer.rotate(abs(index_1 - index_2))
                copy_best_performer = list(copy_best_performer)
            elif (j == 4): #just copy the parent without modifications
                pass
            next_generation.append(copy_best_performer)
    return next_generation
    #pass

def MatrixPerturb(parent_tours):
    #print tour
    #col_len = len(tour)

    tour_copied = deepcopy(parent_tours)
    new_generation = cluster_select(tour_copied)
    return new_generation
    #for j in range(col_len):
        #if prob > random.random(): # this probability decides if a mutation happens or not
            #index_1 = 0
            #index_2 = 0
            #while (index_1 == index_2):
                #index_1 = random.choice(range(col_len))
                #index_2 = random.choice(range(col_len))

            #swap_value = c[index_1]
            #c[index_1] = c[index_2]
            #c[index_2] = swap_value
    #return c    

#city_matrix = generate_matrices(size = num_cities)
#matrix_read = tsplib_xml_parse('../tsp_lib_xml_datasets/burma14.xml')
matrix_read = tsplib_xml_parse('../tsp_lib_xml_datasets/gr17.xml')
dataset_name = matrix_read[0]
num_cities = matrix_read[1]
city_matrix = matrix_read[2]
#print city_matrix

parents = MatrixCreate(pop_size, num_cities) 
#print parents
parents = MatrixRandomize(pop_size) 
#print parents
parentsFitness = Fitness(parents,pop_size) 
#print parentsFitness
[best_performer,best_score_parent,index_best] = best_inv(parents,parentsFitness,pop_size,num_cities)
#print [best_performer,best_score,index_best]
fits = MatrixCreate(number_iterations,number_generations)

for iteration in range(number_iterations):
    print parents
    print ("best_score_before = ",best_score_parent)
    for currentGeneration in range(number_generations):
        #print currentGeneration
        childern = MatrixPerturb(parents) 
        #print childern
        childernFitness = Fitness(childern,pop_size) 
        [best_performer,best_score_child,index_best] = best_inv(childern,childernFitness,pop_size,num_cities)
        if best_score_child < best_score_parent:
            parents = deepcopy(childern) 
            best_score_parent = best_score_child
        fits[iteration][currentGeneration] = best_score_parent
        print best_score_child
        #print best_score
    parents = MatrixCreate(pop_size, num_cities) 
    parents = MatrixRandomize(pop_size) 
    parentsFitness = Fitness(parents,pop_size) 
    [best_performer,best_score_parent,index_best] = best_inv(parents,parentsFitness,pop_size,num_cities)
    print ("parent_after = ",parentsFitness)
    print ("---------")

figure(1)    
plot (range(number_generations),fits[0])
ylabel('Fitness')
xlabel('Generation')
#figure(2)
#imshow(fits, cmap=cm.gray, aspect='auto', interpolation='nearest')
#ylabel('Gene')
#xlabel('Generation')
#figure (3)
#plot (range(number_generations),fits[0], range(number_generations), fits[1], range(number_generations), fits[2], range(number_generations), fits[3], range(number_generations), fits[4])
#ylabel('Fitness')
#xlabel('Generation')
show()