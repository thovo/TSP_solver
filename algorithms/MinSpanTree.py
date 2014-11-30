from UnionFind import *
import numpy as np
from random import *
from operator import add
from math import floor
from itertools import chain
from time import clock

def MinSpanTree(MST_arrMatrix):
	"""
	This an implementation of TSP solver using Minimum Spanning Tree
	
	The function takes an input a list of list containing the weights of edges
	between different nodes/cities
	"""	
	# Timer start
	start = clock()
	lstEdges = []
	# Creating a list of edges from the input adjacency matrix
	# The list of edges is of the following form:
	#	[(node_1, node_2, distance), ...]
	for i in range(len(MST_arrMatrix[0])):
		lstEdges.extend([(i,j,MST_arrMatrix[i][j]) for j in range(len(MST_arrMatrix[0]))])
	# Sort the list of edges according to the distance/weight
	lstEdges = sorted(lstEdges, key= lambda x: x[2])
	# Create list of nodes
	lstNodes = list(set([element[0] for element in lstEdges] + [element[1] for element in lstEdges]))
	
	# Create a Union-Find data structure using the list of nodes
	lstEdges_UF = make_union_find(lstNodes)
	
	# Apply Kruskal's algorithm to get the MST for the set of edges
	lstMinSpanningTree = []
	# For each two nodes in the list of edges find their respective union-find
	# groups
	for u,v,distance in lstEdges:
			tupSetu = find(lstEdges_UF, u)
			tupSetv = find(lstEdges_UF, v)
			# if u,v are in different groups
			if tupSetu != tupSetv:
					lstMinSpanningTree.append((u,v))
					# Put the smaller group within the larger one
					union(lstEdges_UF, tupSetu, tupSetv)
	
	
	# Since the edges were generated for a sorted, the we will consider the
	# Pre-order tree traversal directly from the MST edges.
	MST_lstTour = []
	# Create a copy of the MST Tree to manipulate without loss of data
	lstMinSpanningTree_copy = list(map(list,lstMinSpanningTree))
	# A flag to handle the special case of root node
	first_iter = True
	# An index to for backtracking to nodes in next branches
	backtrack_index = 0
	# While the values in the MST Tree copy are not all {None}, do the following
	while (set(list(chain.from_iterable(lstMinSpanningTree_copy))) != {None}):
		for idx, edge in enumerate(lstMinSpanningTree_copy):
			# If in case of the root node
			if first_iter == True:
				# Add the first element in the first edge to the Tour
				MST_lstTour.append(edge[0])
				# Add the second element in the first edge to the Tour
				MST_lstTour.append(edge[1])
				# Put a pointer on the current node to the second element of the
				# first edge
				current_node = edge[1]
				# Replace the edge with None's
				lstMinSpanningTree_copy[idx] = [None, None]
				# Set root node flag to False
				first_iter = False
				# Set backtracking to false as nodes has been added to the Tour
				backtrack_flag = False
				# Set the backtracking index to last node in the Tour
				backtrack_index= len(MST_lstTour) - 1
			else:
				# If the current node is not found in the current edge
				if (current_node in edge) == False:
					# Enable backtracking
					backtrack_flag = True
					# Skip the current iteration of the loop
					continue
				# Else if the current node is found in the current edge
				else:
					# Check if the position of the current node within the edge
					# because edges are unsorted tuples
					if edge.index(current_node) == 1:
						# Add the other node to the Tour
						MST_lstTour.append(edge[0])
						# Set the node just added to the current node
						current_node = edge[0]
						# Disable backtracking
						backtrack_flag = False
						# Set backtrack index to the last node of the Tour
						backtrack_index = len(MST_lstTour) - 1
					else:
						# Add the other node to the Tour
						MST_lstTour.append(edge[1])
						# Set the node just added to the current node
						current_node = edge[1]
						# Disable backtracking
						backtrack_flag = False
						# Set backtrack index to the last node of the Tour
						backtrack_index = len(MST_lstTour) - 1
				# Set the current edge to None's
				lstMinSpanningTree_copy[idx] = [None, None]
		# Check if backtracking is enabled		
		if (backtrack_flag == True):
			# Decrement backtracking index to the previous node in Tour
			backtrack_index -= 1
			# Update the current node
			current_node = 	MST_lstTour[backtrack_index]
	
	# Complete the tour by adding the first node as the last one
	MST_lstTour.append(MST_lstTour[0])
	
	# Calculation of the Tour cost
	MST_tour_cost = 0
	for city_idx in range(len(lstNodes)):
		# Accumlate the cost between each 2 nodes/cities
		MST_tour_cost += MST_arrMatrix[MST_lstTour[city_idx]][MST_lstTour[city_idx+1]]
	
	# Calculate the total execution time for algorithm
	MST_time = clock() - start
	# Generate the final output form
	MST_output = [MST_tour_cost, MST_lstTour, MST_time]
	
	return(MST_output)
