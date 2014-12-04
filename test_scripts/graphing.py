from json import *
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import pylab
# General targets:
# - For each algorithm results, generate the following graphs:
# ----  Size vs Time, with respect to distribution
# ----  sparsity vs time, with respect to the distribution
# ----  sparsity vs time, with respect to the number of cities
# - General graphs - 1 graph of each type only.
# ---- Range vs time , with respect to all algorithms
# ---- Size vs time , with respect to different algorithms
# ---- sparsity vs time , with respect to different algorithms

# Get the names of the testcases
datasets_path = [ f for f in listdir("../results") if isfile(join("../results",f)) ]
num_datasets = len(datasets_path)

# Step 1
# - For each algorithm results, generate the following graphs:
# ----  Size vs Time, with respect to distribution
# ----  sparsity vs time, with respect to the distribution
# ----  sparsity vs time, with respect to the number of cities
graph_index = 0
for algorithm in datasets_path:
    # ----  Size vs Time, with respect to distribution    
    f = open (os.path.join("../results/",algorithm),"r")
    x = load(f)    
    algorithm_name = x[0]["algorithm"]
    time_uniform = [[] for i in range(6)]
    cities_uniform = []
    time_normal = [[] for i in range(6)]
    cities_normal = []
    cities = range(5,11)
    for i in range(len(x)):
        if (x[i]["distribution"] == "uniform"):
            cities_uniform.append(x[i]["num_cities"])
            index = cities.index(x[i]["num_cities"])
            time_uniform[index].append (x[i]["time"])
        if (x[i]["distribution"] == "normal"):
            cities_normal.append(x[i]["num_cities"])
            index = cities.index(x[i]["num_cities"])
            time_normal[index].append(x[i]["time"])        
            
    avg_normal = []
    for e in time_normal:
        avg_normal.append(sum(e)/len(e))
    
    avg_uniform = []
    for e in time_uniform:
        avg_uniform.append(sum(e)/len(e))   
        
    pylab.figure(graph_index)
    pylab.plot (cities, avg_uniform,"b", label = "Uniform distribution")
    pylab.plot (cities, avg_normal,"r", label = "Normal distribution")
    pylab.xlim(0,15)
    pylab.ylabel("Time in Seconds")
    pylab.xlabel("Number of cities")
    pylab.legend()
    pylab.title(algorithm_name)
    graph_index +=1
    f.close()
    pylab.savefig("../graphs/sizeVStime-distribution-"+algorithm_name)



#for algorithm in datasets_path:
    # ----  sparsity vs time, with respect to the distribution
    f = open (os.path.join("../results/",algorithm),"r")
    x = load(f)    
    sparsity_level = [0.0, 0.1,0.2,0.3,0.4]
    algorithm_name = x[0]["algorithm"]
    sparsities = range(5)
    time_uniform = [[] for i in range(5)]
    sparsity_uniform = []
    time_normal = [[] for i in range(5)]
    sparsity_normal = []
    for i in range(len(x)):
        if (x[i]["distribution"] == "uniform"):
            sparsity_uniform.append(x[i]["sparsity"])
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_uniform[index].append (x[i]["time"])
        if (x[i]["distribution"] == "normal"):
            sparsity_normal.append(x[i]["sparsity"])
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_normal[index].append(x[i]["time"])        
            
    avg_normal = []
    for e in time_normal:
        avg_normal.append(sum(e)/len(e))
    
    avg_uniform = []
    for e in time_uniform:
        avg_uniform.append(sum(e)/len(e))   
        
    pylab.figure(graph_index)
    pylab.plot (sparsity_level, avg_uniform,"b", label = "Uniform distribution")
    pylab.plot (sparsity_level, avg_normal,"r", label = "Normal distribution")
    pylab.xlim(0,0.5)
    pylab.ylabel("Time in Seconds")
    pylab.xlabel("Level of Sparsity")
    pylab.legend()
    pylab.title(algorithm_name)
    graph_index +=1
    f.close()
    pylab.savefig("../graphs/sparsityVStime-distribution-"+algorithm_name)
    
    
#for algorithm in datasets_path:
    ## ----  sparsity vs time, with respect to the number of cities
    f = open (os.path.join("../results/",algorithm),"r")
    x = load(f)    
    sparsity_level = [0.0, 0.1,0.2,0.3,0.4]
    algorithm_name = x[0]["algorithm"]
    sparsities = range(5)
    time_5 = [[] for i in range(5)]
    time_6 = [[] for i in range(5)]
    time_7 = [[] for i in range(5)]
    time_8 = [[] for i in range(5)]
    time_9 = [[] for i in range(5)]
    time_10 = [[] for i in range(5)]
    sparsity_5 = []
    sparsity_6 = []
    sparsity_7 = []
    sparsity_8 = []
    sparsity_9 = []
    sparsity_10 = []
    for i in range(len(x)):
        if (x[i]["num_cities"] == 5):
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_5[index].append (x[i]["time"])
        if (x[i]["num_cities"] == 6):
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_6[index].append(x[i]["time"])        
        if (x[i]["num_cities"] == 7):
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_7[index].append(x[i]["time"])        
        if (x[i]["num_cities"] == 8):
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_8[index].append(x[i]["time"])        
        if (x[i]["num_cities"] == 9):
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_9[index].append(x[i]["time"])        
        if (x[i]["num_cities"] == 10):
            index = sparsities.index(int(x[i]["sparsity"] * 10))
            time_10[index].append(x[i]["time"])        
                                    
    avg_5 = []
    for e in time_5:
        avg_5.append(sum(e)/len(e))
    avg_6 = []
    for e in time_6:
        avg_6.append(sum(e)/len(e))   
    avg_7 = []
    for e in time_7:
        avg_7.append(sum(e)/len(e))
    avg_8 = []
    for e in time_8:
        avg_8.append(sum(e)/len(e))       
    avg_9 = []
    for e in time_9:
        avg_9.append(sum(e)/len(e))
    avg_10 = []
    for e in time_10:
        avg_10.append(sum(e)/len(e))       
        
    pylab.figure(graph_index)
    pylab.plot (sparsity_level, avg_5, label = "City = 5")
    pylab.plot (sparsity_level, avg_6, label = "City = 6")
    pylab.plot (sparsity_level, avg_7, label = "City = 7")
    pylab.plot (sparsity_level, avg_8, label = "City = 8")
    pylab.plot (sparsity_level, avg_9, label = "City = 9")
    pylab.plot (sparsity_level, avg_10, label = "City = 10")
    pylab.yscale('log')
    pylab.xlim(0,0.5)
    pylab.xlim()
    pylab.ylabel("Time in Seconds")
    pylab.xlabel("Level of Sparsity")
    pylab.legend()
    pylab.grid(True)
    pylab.title(algorithm_name)
    graph_index +=1
    f.close()
    pylab.savefig("../graphs/sparsityVStime-cities-"+algorithm_name)
    
    

# Step 2
# - General graphs - 1 graph of each type only.
# ---- Range vs time , with respect to all algorithms
# ---- Size vs time , with respect to different algorithms
# ---- sparsity vs time , with respect to different algorithms

# ---- sparsity vs time , with respect to different algorithms
time_list = {}
sparsity = [0.0, 0.1,0.2,0.3,0.4]
for algorithm in datasets_path:
    f = open (os.path.join("../results/",algorithm),"r")
    x = load(f)    
    algorithm_name = x[0]["algorithm"]
    time_list[algorithm_name] =  [[] for i in range(len(sparsity))]
    time_results = {}
    
    for i in sparsity:
        time_results[i] = []
    
    for i in range(len(x)):
        current_sparsity = x[i]["sparsity"]
        time_results[current_sparsity].append(x[i]["time"])
        
    avg = []
    for e in time_results.keys():
        current_list = time_results[e]
        avg.append(sum(current_list)/len(current_list))
    time_list[algorithm_name] = avg
    f.close()            
    
pylab.figure(graph_index)
for algorithm_name in time_list.keys():
    if algorithm_name == "Brute Force":
        pylab.plot (sparsity, time_list[algorithm_name], label = "BF")
    elif algorithm_name == "Branch and Bound":
        pylab.plot (sparsity, time_list[algorithm_name], label = "BNB")
    elif algorithm_name == "Greedy":
        pylab.plot (sparsity, time_list[algorithm_name], label = "G")
    elif algorithm_name == "Randomized":
        pylab.plot (sparsity, time_list[algorithm_name], label = "R")    
    elif algorithm_name == "Minimum Spanning Tree":
        pylab.plot (sparsity, time_list[algorithm_name], label = "MST")        
    elif algorithm_name == "Evolutionary-HillClimbing":
        pylab.plot (sparsity, time_list[algorithm_name], label = "EA")            
    elif algorithm_name == "2-opt":
        pylab.plot (sparsity, time_list[algorithm_name], label = "2-O")                
    #pylab.bar(left, height)
    #ind += width
    
#pylab.xlim(,10)
pylab.ylabel("Time in Seconds")
pylab.xlabel("Level of Sparsity")
pylab.yscale('log')
pylab.legend()
pylab.title("sparsityVStime for different algorithms")
graph_index +=1
pylab.savefig("../graphs/sparsityVStime-allalgorithms-")

################################################################################33
# ---- Range vs time , with respect to all algorithms
# For each algorithm, for each range, get the average time
time_list = {}
ranges = [10,100,1000,10000]
for algorithm in datasets_path:
    f = open (os.path.join("../results/",algorithm),"r")
    x = load(f)    
    algorithm_name = x[0]["algorithm"]
    time_list[algorithm_name] =  [[] for i in range(len(ranges))]
    time_results = {}
    
    for i in ranges:
        time_results[i] = []
    
    for i in range(len(x)):
        current_range = x[i]["weights_range"]
        time_results[current_range].append(x[i]["time"])
        
    avg = []
    for e in time_results.keys():
        current_list = time_results[e]
        #print current_list
        avg.append(sum(current_list)/len(current_list))
    time_list[algorithm_name] = avg
    f.close()            
print time_list
pylab.figure(graph_index)
for algorithm_name in time_list.keys():
    if algorithm_name == "Brute Force":
        pylab.plot (ranges, time_list[algorithm_name], label = "BF")
    elif algorithm_name == "Branch and Bound":
        pylab.plot (ranges, time_list[algorithm_name], label = "BNB")
    elif algorithm_name == "Greedy":
        pylab.plot (ranges, time_list[algorithm_name], label = "G")
    elif algorithm_name == "Randomized":
        pylab.plot (ranges, time_list[algorithm_name], label = "R")    
    elif algorithm_name == "Minimum Spanning Tree":
        pylab.plot (ranges, time_list[algorithm_name], label = "MST")        
    elif algorithm_name == "Evolutionary-HillClimbing":
        pylab.plot (ranges, time_list[algorithm_name], label = "EA")            
    elif algorithm_name == "2-opt":
        pylab.plot (ranges, time_list[algorithm_name], label = "2-O")                
    #pylab.bar(left, height)
    #ind += width
    
#pylab.xlim(,10)
pylab.ylabel("Time in Seconds")
pylab.xlabel("Range of distances")
#pylab.yscale('log')
pylab.legend()
pylab.title("rangeVStime for different algorithms")
graph_index +=1
pylab.savefig("../graphs/rangeVStime-allalgorithms-")
#################################################################        
# ---- Size vs time , with respect to different algorithms
time_list = {}
for algorithm in datasets_path:
    # ----  Size vs time , with respect to different algorithms
    f = open (os.path.join("../results/",algorithm),"r")
    x = load(f)    
    algorithm_name = x[0]["algorithm"]
    time_list[algorithm_name] =  []
    time_results = [[] for i in range(6)]
    cities = range(5,11)
    for i in range(len(x)):
        index = cities.index(x[i]["num_cities"])
        time_results[index].append (x[i]["time"])
            
    avg = []
    for e in time_results:
        avg.append(sum(e)/len(e))
    time_list[algorithm_name] = avg
    
    f.close()

pylab.figure(graph_index)
cities = range(5,11)
for algorithm_name in time_list.keys():
    if algorithm_name == "Brute Force":
        pylab.plot (cities, time_list[algorithm_name], label = "BF")
    elif algorithm_name == "Branch and Bound":
        pylab.plot (cities, time_list[algorithm_name], label = "BNB")
    elif algorithm_name == "Greedy":
        pylab.plot (cities, time_list[algorithm_name], label = "G")
    elif algorithm_name == "Randomized":
        pylab.plot (cities, time_list[algorithm_name], label = "R")    
    elif algorithm_name == "Minimum Spanning Tree":
        pylab.plot (cities, time_list[algorithm_name], label = "MST")        
    elif algorithm_name == "Evolutionary-HillClimbing":
        pylab.plot (cities, time_list[algorithm_name], label = "EA")            
    elif algorithm_name == "2-opt":
        pylab.plot (cities, time_list[algorithm_name], label = "2-O")                
    
pylab.xlim(5,10)
pylab.ylabel("Time in Seconds")
pylab.xlabel("Number of cities")
pylab.yscale('log')
pylab.legend()
pylab.title("Comparison of the average running time for different algorithms")
graph_index +=1
pylab.savefig("../graphs/sizeVStime-allalgorithms-")