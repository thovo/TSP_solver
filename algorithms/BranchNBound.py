# Implementation of the Branch and Bound Algorithm
from itertools import *
from time import clock
from BruteForce import GeneratePaths

def BranchNBound(BnB_arrMatrix):
    # Start timer
    start = clock()
    # Generate the TSP nodes and all the possible paths
    lstNodes, lstTree = GeneratePaths(BnB_arrMatrix)
    
    # Calculating the cost of each cycle
    lstCostList = []
    # Initialize the current best/optimal cost to infinity
    numCurrentBestCost = float("inf")    
    for cycle in lstTree:
        # Initialize cost for each cycle
        numCostPerCycle = 0
        # Convert each 2 nodes in a cycle to an index in the input array
        for index in range(0,(len(lstNodes)-1)):
            # CostPerCycle is calculated from the input Matrix between 
            #   each 2 nodes in a cycle
            numCostPerCycle = numCostPerCycle + BnB_arrMatrix[cycle[index]][cycle[index+1]]
            # Check the current accumlated cost against the Current Best Cost
            if (numCostPerCycle >= numCurrentBestCost):
                numCostPerCycle = float("inf")
                break
            
        # Add the first cycle cost as the best one
        if (numCurrentBestCost == float("inf")):
            numCurrentBestCost = numCostPerCycle
        # if a better cost is found, update the numCurrentBestCost variable
        elif (numCostPerCycle < numCurrentBestCost):
            numCurrentBestCost = numCostPerCycle
        # Add the current cycle cost to the cost list
        lstCostList.append(numCostPerCycle)

    # Calculating the least cost cycle
    numLeastCost = min(lstCostList)
    numLeastCostIndex = lstCostList.index(numLeastCost)

    BnB_time = clock() - start
    
    BnB_output = ["Branch and Bound", numLeastCost, lstTree[numLeastCostIndex], BnB_time]
    
    return(BnB_output)    