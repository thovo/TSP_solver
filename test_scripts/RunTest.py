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
import TwoOpt

class TestResult:
    def __init__(self, algorithm, num_cities, symmetry, distribution, sparsity, 
                 weights_range, time, cost, optimality):
        self.algorithm = algorithm
        self.symmetry = symmetry
        self.distribution = distribution
        self.num_cities = num_cities
        self.sparsity = sparsity
        self.weights_range = weights_range
        self.time = time
        self.cost = cost
        self.optimality = optimality
        
    def get_result(self):
        template_dict = {"algorithm": self.algorithm, 
                         "num_cities": self.num_cities, 
                         "symmetry": self.symmetry, 
                         "weights_range": self.weights_range, 
                         "sparsity": self.sparsity, 
                         "distribution": self.distribution, 
                         "time": self.time,
                         "cost": self.cost,
                         "optimality": self.optimality}
        return template_dict
        
            
def run_test(algorithm, dataset):
    if algorithm == "BruteForce":
        result = BruteForce.BruteForce(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], result[1], 1).get_result()
    elif algorithm == "BranchNBound":
        result = BranchNBound.BranchNBound(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], result[1], 1).get_result()
    elif algorithm == "Greedy":
        #bb_result = BranchNBound.BranchNBound(dataset[1])
        result = Greedy.better_greedy(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], 
                                 result[1], result[1]).get_result()
    elif algorithm == "Randomized":
        #bb_result = BranchNBound.BranchNBound(dataset[1])
        result = Randomized.better_result_of_randomized(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], 
                                 result[1], result[1]).get_result()
    elif algorithm == "MinSpanTree":
        #bb_result = BranchNBound.BranchNBound(dataset[1])
        result = MinSpanTree.MinSpanTree(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], 
                                 result[1], result[1]).get_result()
    elif algorithm == "EA_hillclimbing":
        #bb_result = BranchNBound.BranchNBound(dataset[1])
        result = EA_hillclimbing.hillclimbing_algorithm(dataset[1], dataset[0][0])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], 
                                 result[1], result[1]).get_result()
    elif algorithm == "Genetic":
        #bb_result = BranchNBound.BranchNBound(dataset[1])
        result = GA.genetic_algorithm(dataset[1], dataset[0][0])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1],
                                 dataset[0][2], dataset[0][3], dataset[0][4],
                                 result[3],
                                 result[1], result[1]).get_result()
            
    elif algorithm == "TwoOpt":
        #bb_result = BranchNBound.BranchNBound(dataset[1])
        result = TwoOpt.two_opt(dataset[1])
        test_result = TestResult(result[0], dataset[0][0], dataset[0][1], 
                                 dataset[0][2], dataset[0][3], dataset[0][4], 
                                 result[3], 
                                 result[1], result[1]).get_result()    
    else:
        raise Exception("Wrong algorithm chosen!")
    
    return test_result
