__author__ = 'thovo'

import os
from prettytable import PrettyTable
from algorithms import BruteForce
from algorithms import BranchNBound
from algorithms import Greedy
from algorithms import Randomized
from algorithms import MinSpanTree
from XMLParsingScript import XmlParserFinal
import xlwt
from datetime import datetime

#GUI of the program, have 3 step:
#Step 1: Choose the data set. 3 options:
#Choose from our data sets folder
#Choose from your own file
#Create a random data set
#Step 2: Choose algorithms. 2 options:
# Select a few of algorithms
# All
# Step 3: Output the result.
# Output the result directly on command line
# Output the result in an excel file and save it in results folder


def read_dataset():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    directory = dir_name + "/tsp_lib_xml_datasets"
    files_data = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for file_name in files:
            #Get only xml file
            if file_name.endswith(".xml"):
                file_path = os.path.join(root, file_name)
                file_stat = os.stat(file_path)
                file_size = file_stat.st_size
                files_data.append([file_name, file_size, file_path])  # Add it to the list.
    return files_data  # Self-explanatory.


def check_user_input(user_input, choice):
    flag = False
    data_sets = read_dataset()
    if choice is 1:
        #Check user input for data set option
        try:
            x = int(user_input)
            if x not in [1, 2, 3]:
                print "You must choose a number between 1 and 3"
            else:
                flag = True
        except ValueError:
            print "Ops,not a number"
    if choice is 2:
        #Check user input for data set
        for data_file in data_sets:
            if user_input in data_file:
                flag = True
                break
    if choice is 3:
        #Return the path to the file instead of return True
        for data_file in data_sets:
            if user_input in data_file:
                flag = data_file[2]
                break
    if choice is 4:
        #Check algorithm option
        try:
            x = int(user_input)
            if x not in [1, 2]:
                print "You must choose a number between 1 and 2"
            else:
                flag = True
        except ValueError:
            print "Ops,not a number"
    return flag


def tsp():
    print "Welcome to Travelling Sales Problems!"
    print "Step 1: Choose the data set"
    print "You have 3 options:"
    options = [[1, "Choose from default data sets"], [2, "Choose from your own data set"], [3, "Create a random data"]]
    data_set_option_table = PrettyTable(["Number", "Options"])
    for i in range(0, 3):
        data_set_option_table.add_row(options[i])
    print data_set_option_table
    user_input = raw_input("Enter the number of the option:")
    while check_user_input(user_input, 1) is False:
        print "You have type wrongly the number, please choose again!"
        user_input = raw_input("Please enter the number of the option:")
        print "You have choose the option: "+str(user_input)
    #Declare cities variable to contain the cities
    cities = []
    if int(user_input) is 1:
        print "Choose the data sets to test:"
        #Print out list of data sets
        data_sets = read_dataset()
        data_set_table = PrettyTable(["File name", "File size in bytes", "File path"])
        for data_file in data_sets:
            data_set_table.add_row(data_file)
        print data_set_table.get_string(sortby="File size in bytes")
        user_data_input = raw_input("Please type name of the data set that you want to use:")
        print "You have choose the data set: "+str(user_data_input)
        while check_user_input(user_data_input, 2) is False:
            print "You have type wrongly the data set, please choose again!"
            user_data_input = raw_input("Please type name of the data set that you want to use:")
            print "You have choose the data set: "+str(user_data_input)
        print "We are now working on the data set: "+str(user_data_input)
        data_path = check_user_input(user_data_input,3)
        cities = XmlParserFinal.tsplib_xml_parse(str(data_path))
        # print cities
    if int(user_input) is 2:
        print "WARNING: We accept only xml file and have the same format like TSP lib!"
        user_data_input = raw_input("Enter the full path to your data set:")
        print "The full path to your file: "+user_data_input
        cities = XmlParserFinal.tsplib_xml_parse(str(user_data_input))
    if int(user_input) is 3:
        print "Random data is generating."
        #Get random data
        cities = []
    #The list of algorithms options
    algorithms_option = [[1, "Choose several algorithms, separate by comma"], [2, "All"]]
    algorithms_option_table = PrettyTable(["Number", "Description"])
    for i in range(0, len(algorithms_option)):
        algorithms_option_table.add_row(algorithms_option[i])
    #The list of available algorithms
    algorithms = [[1, "Greedy"], [2, "Randomized"],
                  [3, "Brute Force"], [4, "Branch and Bound"],
                  [5, "Genetic"], [6, "Evolutionary"], [7, "Minimum Spanning Tree"]]
    algorithms_table = PrettyTable(["Number", "Algorithm"])
    for i in range(0, len(algorithms)):
        algorithms_table.add_row(algorithms[i])

    #The results will be contain in a list
    results = []

    print "Step 2: Choose the algorithm"
    print algorithms_table
    print "You have two options:"
    print algorithms_option_table
    user_algorithm_options_input = raw_input("Enter the number between 1 and 2 to choose:")
    while check_user_input(user_algorithm_options_input, 1) is False:
        print "You have type wrongly the number, please choose again!"
        user_algorithm_options_input = raw_input("Enter the number between 1 and 2 to choose:")
        print "You have choose the option: "+str(user_algorithm_options_input)
    if int(user_algorithm_options_input) == 1:
        print "Choose the algorithm in table below:"
        print algorithms_table
        user_algorithm_list = raw_input("Enter several number, separate by comma:")
        algorithm_list = user_algorithm_list.split(',')
        for algorithm_number in algorithm_list:
            if int(algorithm_number) == 1:
                print "You chose Greedy!"
                results.append(Greedy.better_greedy(cities[3]))
                # We need only the list of cities
            if int(algorithm_number) == 2:
                print "You chose Randomized!"
                results.append(Randomized.better_result_of_randomized(cities[3], 10000))
                # We need only the list of cities
            if int(algorithm_number) == 3:
                print "You chose Brute Force!"
                results.append(BruteForce.BruteForce(cities[3]))
            if int(algorithm_number) == 4:
                print "You chose Branch and Bound!"
                results.append(BranchNBound.BranchNBound(cities[3]))
            if int(algorithm_number) == 5:
                print "You chose Genetic!"
                results.append()
            if int(algorithm_number) == 6:
                print "You chose Evolutionary!"
                results.append()
            if int(algorithm_number) == 7:
                print "You chose MST!"
                results.append(MinSpanTree.MinSpanTree(cities[3]))

    if int(user_algorithm_options_input) == 2:
        print "WARNING: You chose to run all algorithms. " \
              "The time to run should be finite but we actually don't know when will the program finish"

    result_table = PrettyTable(["Algorithm", "Cost", "Path", "Time"])
    for result_item in results:
        result_table.add_row(result_item)
    print "The result will be sorted by cost"
    print result_table.get_string(sortby="Cost")

    # #Create a xls file

    book = xlwt.Workbook(encoding="utf-8")
    worksheet = book.add_sheet("Comparison of algorithms")
    row = 0
    col = 0
    worksheet.write(row, col, "Comparison of algorithms on "+str(datetime.now()))
    #Move to next row
    row += 1
    #Write the header
    worksheet.write(row, col, "Algorithm")
    worksheet.write(row, col+1, "Cost")
    worksheet.write(row, col+2, "Path")
    worksheet.write(row, col+3, "Time")
    row += 1
    for result_item in results:
        worksheet.write(row, col, str(result_item[0]))
        worksheet.write(row, col+1, str(result_item[1]))
        worksheet.write(row, col+2, str(result_item[2]))
        worksheet.write(row, col+3, str(result_item[3]))
        row += 1

    book.save('result.xls')
tsp()