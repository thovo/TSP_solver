__author__ = 'thovo'
from XMLParsingScript import XmlParserFinal
import matplotlib
import matplotlib.pyplot as plt
import random
import time
import itertools

def get_data():
    data = XmlParserFinal.tsplib_xml_parse('../tsp_lib_xml_datasets/ulysses16.xml')
    print data[2]
    return data

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
get_data()
