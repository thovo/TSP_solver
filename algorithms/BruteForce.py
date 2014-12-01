# Implementation of the Brute Force algorithm
from itertools import *
from time import clock

def GeneratePaths(BF_arrMatrix):
    # Extracting the nodes of the TSP
    lstNodes = [node for node in range(len(BF_arrMatrix))]
    # Remove the last city to generate non cyclic permutations
    last_node = lstNodes.pop()
    # Enumerating all the paths from the nodes
    lstPermutations = list(permutations(lstNodes))
    # Constructing a tree
    lstTree = list(map(list, lstPermutations))
    
    # Closing the paths / Constructing full cycles
    for path in lstTree:
        path.append(last_node)
        path.append(path[0])  
    return lstNodes, lstTree

def BruteForce(BF_arrMatrix):
    # Start time
    start = clock()
    
    # Generate all the possible paths
    lstNodes, lstTree = GeneratePaths(BF_arrMatrix)
    
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
    
    BF_time = clock() - start

    BF_output = ["Brute Force", numLeastCost, lstTree[numLeastCostIndex], BF_time]
    
    return(BF_output)

