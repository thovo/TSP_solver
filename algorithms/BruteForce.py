# Implementation of the Brute Force algorithm
from itertools import *

def BruteForce(BF_arrMatrix):
    # Extracting the nodes of the TSP
    lstNodes = [node for node in range(len(BF_arrMatrix))]
    # Enumerating all the paths from the nodes
    lstPermutations = list(permutations(lstNodes))
    # Constructing a tree
    lstTree = list(map(list, lstPermutations))
    # Closing the paths / Constructing full cycles
    for path in lstTree:
        path.append(path[0])

    # Calculating the cost of each cycle
    lstCostList = []
    for cycle in lstTree:
        # Initialize cost for each cycle
        numCostPerCycle = 0
        # Convert each 2 nodes in a cycle to an index in the input array
        for index in range(0,(len(lstNodes)-1)):
            # CostPerCycle is calculated from the input Matrix between 
            #   each 2 nodes in a cycle
            numCostPerCycle = numCostPerCycle + BF_arrMatrix[cycle[index]][cycle[index+1]]
        lstCostList.append(numCostPerCycle)

    # Calculating the least cost cycle
    numLeastCost = min(lstCostList)
    numLeastCostIndex = lstCostList.index(numLeastCost)

    # Displaying the least cost cycle
    print(lstTree[numLeastCostIndex])
