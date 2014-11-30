__author__ = 'thovo'
import sys
from XMLParsingScript import XmlParserFinal
import timeit
from random import randint
import time

# randomized approach: At a current city, choose randomly next city to visit. No reconsider about the previous choice


def randomized(cities):
    start = timeit.default_timer()
    #Path of the tour
    path = [0]
    #Cost of the tour
    cost = 0
    #Assume the first city as starting point, create a temporary value
    temp = 0
    #The number of the unvisited cities
    flag = len(cities) - 1
    #next_city
    next_city = 0
    while flag > 0:
        #Find the next random city
        if len(path) == 1:
            next_city = randint(1,len(cities)-1)
            path.append(next_city)
            cost += cities[temp][next_city]
            temp = next_city
        if (len(path) > 1) and (len(path) < len(cities)):
            while next_city in path :
                next_city = randint(1,len(cities)-1)
            path.append(next_city)
            cost += cities[temp][next_city]
            temp = next_city
        flag -= 1
    stop = timeit.default_timer()
    time_finish = stop - start
    algorithm = "Randomized"
    result = [algorithm, cost, path, time_finish]
    return result


def better_result_of_randomized(cities):
    start = timeit.default_timer()
    print "randomized algorithm is running. Please wait!"
    result = randomized(cities)
    for i in range(0, 1000):
        result_temp = randomized(cities)
        if result[1] > result_temp[1]:
            result[1] = result_temp[1]
            result[2] = result_temp[2]
    stop = timeit.default_timer()
    result[3] = stop - start
    # print "The cost of the tour is:"+str(result[0])
    # print "The path of the tour is:"+str(result[1])
    # print "The time to finish is:"+str(result[2])+" in second"
    return result
