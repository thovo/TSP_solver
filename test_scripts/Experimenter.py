# This is the Experimenter script
# This script is used to run an algorithm on several datasets, and store the
# output in "json" easily retrievable format for further analysis

import os
import json
from RunTest import *
from RandomGenerator import *


def run_experiment(algorithm):
    datasets_path, num_datasets = generate_datasets()
    
    experiment_results = []
    
    for i in range(num_datasets):
        current_dataset = "DATASET" + str(i) + ".json"
        json_file_object = open(os.path.join(datasets_path, current_dataset), 'r')
        dataset = json.load(json_file_object)
        test_result = run_test(algorithm, dataset)
        json_file_object.close()
        experiment_results.append(test_result)
    
    
    exp_file_name = algorithm + "_EXP.json"
    exp_file_object = open(os.path.join(datasets_path, exp_file_name), 'w')
    json.dump(experiment_results, exp_file_object)
    exp_file_object.close()
    

run_experiment("MinSpanTree")