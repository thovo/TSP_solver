import xml.etree.ElementTree as ET
import os


def tsplib_xml_parse(filename):
    """
    This function take as an input the path to a XML file
    
    This new function should return a list of 
    - The name of the data set as a string
    - The number of cities as an integer
    - The data set itself, as a list of lists
    """
    #The list contain the final r
    final_output = []

    #Check for the file exist and readable
    if (os.path.isfile(filename) and os.access(filename, os.R_OK) and filename.endswith(".xml")) is False:
        print "Either file is missing or is not readable or is not in correct file type"
        return final_output

    #XML parser
    tree = ET.parse(filename)
    root = tree.getroot()
    #Check the file to know it is the same syntax like other TSP LIB file
    if str(root.tag) != 'travellingSalesmanProblemInstance':
        print "Not correct format like TSP Lib file."
        print "Please check this link below for more information: "
        print "http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/XML-TSPLIB/instances/"
        return final_output

    number_of_cities = 0
    final_matrix = []
    
    for child in root:
        #Get the name of the dataset
        if child.tag == "name":
            dataset_name = child.text
            final_output.append(dataset_name)
        #Get the description of the dataset
        if child.tag == "description":
            dataset_description = child.text
            final_output.append(dataset_description)
        if child.tag == "graph":
            for vertex in child:
                temp_array = []
                for edge in vertex:
                    temp_array.append(float(edge.get('cost')))
                final_matrix.append(temp_array)
                
    vertex_index = 0
    number_of_cities = len(final_matrix)
    final_output.append(number_of_cities)
    
    for row in final_matrix:
        row.insert(vertex_index,0)
        vertex_index += 1
        
    final_output.append(final_matrix)
    # print "Working on data set:"+final_output[0]
    # print "Data description:"+final_output[1]
    # print "The number of cities is:"+str(final_output[2])
    return final_output

#Example - Uncomment the following code and put a valid path for any xml file from TSP LIB
#test_matrix = tsplib_xml_parse('../tsp_lib_xml_datasets/gr24.xml')
# print test_matrix[0]
# print test_matrix[1]
# print test_matrix[2]
# print test_matrix[3][0]