## This is the RunTest script, used to run a given algorithm over a certain
## dataset
import sys
sys.path.insert(0, "../algorithms")
import BruteForce
import BranchNBound
import Greedy
import Randomized
import MinSpanTree
import GA
import EA_hillclimbing


class TestResult:
    def __init__(self, algorithm, num_cities, symmetry, distribution, sparsity, 
                 weights_range, time, optimality):
        self.algorithm = algorithm
        self.symmetry = symmetry
        self.distribution = distribution
        self.num_cities = num_cities
        self.sparsity = sparsity
        self.weights_range = weights_range
        self.time = time
        self.optimality = optimality
        
    def get_result(self):
        template_dict = {"algorithm": self.algorithm, 
                         "num_cities": self.num_cities, 
                         "symmetry": self.symmetry, 
                         "weights_range": self.weights_range, 
                         "sparsity": self.sparsity, 
                         "distribution": self.distribution, 
                         "time": self.time,
                         "optimality": self.optimality}
        return template_dict
        
            
def run_test(algorithm, dataset):
    if algorithm == "BruteForce":
        result = BruteForce.BruteForce(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], 1)
    elif algorithm == "BranchNBound":
        result = BranchNBound.BranchNBound(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], 1)
    elif algorithm == "Greedy":
        result = Greedy.better_greedy(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], "Unknown")
    elif algorithm == "Randomized":
        result = Randomized.better_result_of_randomized(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], "Unknown")
    elif algorithm == "MinSpanTree":
        result = MinSpanTree.MinSpanTree(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], "Unknown")        
    else:
        raise Exception("Wrong algorithm chosen!")
    
    return test_result
