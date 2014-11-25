__author__ = 'thovo'
import sys
from XMLParsingScript import XmlParserFinal
import timeit
import random
import time
import itertools

# def exact_TSP(cities):
#     "Generate all possible tours of the cities and choose the shortest one."
#     return shortest(alltours(cities))
#
# def shortest(tours):
#     "Return the tour with the minimum total distance."
#     return min(tours, key=total_distance)
#
# alltours = itertools.permutations # The permutation function is already defined in the itertools module
#
# cities = {1, 2, 3}
#
# list(alltours(cities))
# def total_distance(tour):
#     "The total distance between each pair of consecutive cities in the tour."
#     return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))
#
# City = complex # Constructor for new cities, e.g. City(300, 400)
#
# def distance(A, B):
#     "The distance between two points."
#     return abs(A - B)
#
# def Cities(n):
#     "Make a set of n cities, each with random coordinates."
#     return set(City(random.randrange(10, 890), random.randrange(10, 590)) for c in range(n))
#
# # Let's make some standard sets of cities of various sizes.
# # We'll set the random seed so that these sets are the same every time we run this notebook.
# random.seed('seed')
# cities8, cities10, cities100, cities1000 = Cities(8), Cities(10), Cities(100), Cities(1000)
# tour = exact_TSP(cities8)

#My work start from here
def get_data():
    data = XmlParserFinal.tsplib_xml_parse('../tsp_lib_xml_datasets/pr439.xml')
    return data
dataSet = get_data()
#The list of cities
cities = dataSet[3]
# Greedy Algorithm
# Always start from city, find the nearest city until finish travelling all the city, no reconsider the previous choice, just care for the current

def Greedy():
    start = timeit.default_timer()
    print "Greedy algorithm is running. Please wait!"
    #Path of the tour
    path = [0]
    #Cost of the tour
    cost = 0
    #Assume the first city as starting point, create a temporary value
    temp = 0
    #Hold the position in the list
    position = 0
    #The number of the unvisited cities
    flag = dataSet[2] - 1
    #Current cost
    currentCost = 0
    while flag > 0:
        #Find the nearest city
        for x in range(0,len(cities)):
            #x not in path, mean we don't care about the cities that we visited
            if((cities[temp][x] !=0) and (x not in path) ):
                if(currentCost == 0):
                    currentCost = cities[temp][x]
                    position = x
                if(currentCost > cities[temp][x]):
                    currentCost = cities[temp][x]
                    position = x
        cost += currentCost
        #Reset current cost for next calculating
        currentCost = 0
        temp = position
        path.append(position)
        flag -= 1
    stop = timeit.default_timer()
    print "The cost of the tour is:"+str(cost)
    print "The path of the tour is:"+str(path)
    print "The time to finish is:"+str(stop-start)+" in second"

Greedy()