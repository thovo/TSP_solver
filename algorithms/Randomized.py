__author__ = 'thovo'
import sys
from XMLParsingScript import XmlParserFinal
import timeit
from random import randint
import time

# randomized approach: At a current city, choose randomly next city to visit. No reconsider about the previous choice


def get_data():
    data = XmlParserFinal.tsplib_xml_parse('../tsp_lib_xml_datasets/gr24.xml')
    return data
data_set = get_data()
#The list of cities
cities = data_set[3]


def randomized():
    start = timeit.default_timer()
    #Path of the tour
    path = [0]
    #Cost of the tour
    cost = 0
    #Assume the first city as starting point, create a temporary value
    temp = 0
    #The number of the unvisited cities
    flag = data_set[2] - 1
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
    result = [cost,path,time_finish]
    return result


def better_result_of_randomized():
    start = timeit.default_timer()
    print "randomized algorithm is running. Please wait!"
    result = randomized()
    for i in range(0, 1000):
        result_temp = randomized()
        if result[0] > result_temp[0]:
            result[0] = result_temp[0]
            result[1] = result_temp[1]
    stop = timeit.default_timer()
    result[2] = stop - start
    print "The cost of the tour is:"+str(result[0])
    print "The path of the tour is:"+str(result[1])
    print "The time to finish is:"+str(result[2])+" in second"
    return result

better_result_of_randomized()