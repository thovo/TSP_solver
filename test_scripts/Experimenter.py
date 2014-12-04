# This is the Experimenter script
# This script is used to run an algorithm on several datasets, and store the
# output in "json" easily retrievable format for further analysis

import os
from os import listdir
from os.path import isfile, join
import json
from RunTest import *
from RandomGenerator import *

def run_experiment(algorithm):
    datasets_path = [ f for f in listdir("../random_datasets") if isfile(join("../random_datasets",f)) ]
    num_datasets = len(datasets_path)
    experiment_results = []
    bf_file_object = open(os.path.join("../results","BruteForce_EXP.json"), 'r')
    bf_results = json.load(bf_file_object)
    
    for i in range(num_datasets):
        print i
        json_file_object = open(os.path.join("../random_datasets",datasets_path[i]), 'r')
        dataset = json.load(json_file_object)
        test_result = run_test(algorithm, dataset)
        json_file_object.close()
        test_result["optimality"] = bf_results[i]["cost"]/test_result["cost"]
        experiment_results.append(test_result)
    
    
    exp_file_name = algorithm + "_EXP.json"
    exp_file_object = open(os.path.join("../results", exp_file_name), 'w')
    json.dump(experiment_results, exp_file_object)
    exp_file_object.close()
    

run_experiment("Genetic")