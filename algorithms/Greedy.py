__author__ = 'thovo'
import sys
# from XMLParsingScript import XmlParserFinal
import timeit
import random
import time

# Greedy Algorithm
# Always start from city, find the nearest city until finish travelling all the city
# no reconsider the previous choice, just care for the current


def greedy(cities, start_city=0):
    start = timeit.default_timer()
    #Path of the tour
    path = [start_city]
    #Cost of the tour
    cost = 0
    #Assume the first city as starting point, create a temporary value
    temp = start_city
    #Hold the position in the list
    position = start_city
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
        cost += int(current_cost)
        #Reset current cost for next calculating
        current_cost = 0
        temp = position
        path.append(position)
        if flag == 1:
            #Add the connected path from last city to the start city
            current_cost = cities[position][start_city]
            cost += current_cost
            path.append(start_city)
        flag -= 1
    stop = timeit.default_timer()
    time_finish = stop - start
    algorithm = "Greedy"
    result = [algorithm, cost, path, time_finish]
    # print "The cost of the tour is:"+str(result[1])
    # print "The path of the tour is:"+str(result[2])
    # print "The time to finish is:"+str(result[3])+" in second"
    return result


def better_greedy(cities):
    start = timeit.default_timer()
    # print "greedy algorithm is running. Please wait!"
    result = greedy(cities, 0)
    result_temp = []
    i = 0
    while i < len(cities):
        result_temp = greedy(cities, i)
        if result[1] > result_temp[1]:
            result = result_temp
        i += 1
    stop = timeit.default_timer()
    # print "The best result:"
    # print "The cost of the tour is:"+str(result[1])
    # print "The path of the tour is:"+str(result[2])
    result[3] = stop - start
    # print "The time to finish is:"+str(result[3])+" in second"
    # print result
    return result

# data = XmlParserFinal.tsplib_xml_parse("../tsp_lib_xml_datasets/burma14.xml")
# better_greedy(data[3])