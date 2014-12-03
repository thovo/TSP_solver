__author__ = 'thovo'
import sys
from XMLParsingScript import XmlParserFinal
from algorithms import Randomized
from algorithms import Greedy
import timeit
import random
import time

# 2-opt Algorithm
# 2-opt is a simple local search algorithm first proposed by Croes in 1958 for solving the traveling salesman problem.
# The main idea behind it is to take a route that crosses over itself and reorder it so that it does not.


def calculate_total_distance(path, cities):
    #This function will return the total distance of a path
    total_distance = 0
    for i in range(0, len(path)-1):
        total_distance += cities[path[i]][path[i+1]]
    return total_distance


def two_opt_swap(path, i=1, k=2):
    #Do 2-opt swap, create a new path
    new_path = []
    #take route[0] to route[i-1] and add them in order to new_route
    temp = 0
    while temp <= i-1:
        new_path.append(path[temp])
        temp += 1
    #take route[i] to route[k] and add them in reverse order to new_route
    #Will hold the path to inverse later
    temp_path = []
    temp = i
    while temp <= k:
        temp_path.append(path[temp])
        temp += 1
    temp = len(temp_path)
    #Add inverse path
    while temp > 0:
        new_path.append(temp_path[temp-1])
        temp -= 1
    #take route[k+1] to end and add them in order to new_route
    temp = k + 1
    while temp < len(path):
        new_path.append(path[temp])
        temp += 1
    return new_path


def two_opt(cities):
    start = timeit.default_timer()
    result = []
    #Get a random or initial tour
    #result = Randomized.randomized(cities)
    result = Greedy.greedy(cities, 5)
    print result
    path = result[2]
    cost = result[1]
    #number of nodes eligible to be swapped will be length of the path - first city - last city - 1
    number_of_nodes = len(path) - 3
    #For the limited of this algorithm, I assume we won't swap for the first and the last city
    i = 1
    k = i + 1
    new_cost = 0
    while i < number_of_nodes:
        while k < number_of_nodes:
            new_path = two_opt_swap(path, i, k)
            new_cost = calculate_total_distance(new_path, cities)
            #If the cost is better, the result will use the new path
            if new_cost < cost:
                result[1] = new_cost
                result[2] = new_path
            k += 1
        i += 1
    stop = timeit.default_timer()
    time_finish = stop - start
    algorithm = "2-opt"
    result[0] = algorithm
    result[3] = time_finish
    print result
    return result


data = XmlParserFinal.tsplib_xml_parse("../tsp_lib_xml_datasets/burma14.xml")
two_opt(data[3])