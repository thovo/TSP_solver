# The hill climbing function
#Assignment 2
### Some Explanation
## The fitness is defined as the average of all the values in the gene
###
import numpy
import matplotlib
from pylab import *
from numpy import *
#import random
import scipy
from copy import copy, deepcopy

general_counter = 0
general_counter_2 = 0

def MatrixCreate(rows, columns):
    Matrix = zeros( (rows,columns) )
    return Matrix

def MatrixRandomize(v):
    row_len = v.shape[0]
    col_len = v.shape[1]
    x = random.random((row_len,col_len))
    return x

def Fitness(v):
    col_len = v.shape[1]
    fitness_sum = sum(v) / col_len    
    return fitness_sum

def MatrixPerturb(v, prob):
    global general_counter
    global general_counter_2
    row_len = v.shape[0]
    col_len = v.shape[1]
    #c = v[:] # This does't work ! It still copies the array with its reference, not its value! use deepcopy instead.
    c = deepcopy(v)
    for i in range(row_len):
        for j in range(col_len):
            general_counter_2 += 1
            if prob > random.random():
                c[i][j] = random.random()
                general_counter += 1
    return c    

parent = MatrixCreate(1, 50) 
parent = MatrixRandomize(parent) 
parentFitness = Fitness(parent) 

number_iterations = 50
number_generations = 5000
fits = MatrixCreate(number_iterations,number_generations)

for iteration in range(number_iterations):
    parent = MatrixCreate(1, 50) 
    parent = MatrixRandomize(parent) 
    parentFitness = Fitness(parent)     
    for currentGeneration in range(number_generations):
        #print currentGeneration, parentFitness 
        child = MatrixPerturb(parent, 0.05) 
        childFitness = Fitness(child) 
        if childFitness > parentFitness:
            parent = child[:] 
            parentFitness = childFitness
            #print currentGeneration, parentFitness 
            
        fits[iteration][currentGeneration] = parentFitness

print general_counter
print general_counter_2
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
