__author__ = 'thovo'
import sys
from XMLParsingScript import XmlParserFinal
import timeit
import random
import time

# Greedy Algorithm
# Always start from city, find the nearest city until finish travelling all the city
# no reconsider the previous choice, just care for the current


def greedy(cities):
    start = timeit.default_timer()
    print "greedy algorithm is running. Please wait!"
    #Path of the tour
    path = [0]
    #Cost of the tour
    cost = 0
    #Assume the first city as starting point, create a temporary value
    temp = 0
    #Hold the position in the list
    position = 0
    #The number of the unvisited cities
    flag = len(cities) - 1
    #Current cost
    current_cost = 0
    while flag > 0:
        #Find the nearest city
        for x in range(0, len(cities)):
            #x not in path, mean we don't care about the cities that we visited
            if (cities[temp][x] != 0) and (x not in path):
                if current_cost == 0:
                    current_cost = cities[temp][x]
                    position = x
                if current_cost > cities[temp][x]:
                    current_cost = cities[temp][x]
                    position = x
        cost += current_cost
        #Reset current cost for next calculating
        current_cost = 0
        temp = position
        path.append(position)
        flag -= 1
    stop = timeit.default_timer()
    time_finish = stop - start
    algorithm = "Greedy"
    result = [algorithm,cost, path, time_finish]
    # print "The cost of the tour is:"+str(result[0])
    # print "The path of the tour is:"+str(result[1])
    # print "The time to finish is:"+str(result[2])+" in second"
    return result