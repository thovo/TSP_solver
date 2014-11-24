import xml.etree.ElementTree as ET
 
def tsplib_xml_parse (filename):
    """
    This function take as an input the name of the XML file
    
    This new function should return a list of 
    - The name of the dataset as a string
    - The number of cities as an integer
    - The data set itself, as a list of lists
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    #The list contain the final r
    final_output = []

    number_of_cities = 0
    final_matrix = []
    
    for child in root:
        #Get the name of the dataset
        if (child.tag == "name"):
            dataset_name = child.text
            final_output.append(dataset_name)
        #Get the description of the dataset
        if (child.tag == "description"):
            dataset_description = child.text
            final_output.append(dataset_description)
        if (child.tag == "graph"):
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
    
    return final_output

#Example - Uncomment the following code and put a valid path for any xml file from TSP LIB
test_matrix = tsplib_xml_parse('../tsp_lib_xml_datasets/burma14.xml')
print test_matrix[0]
print test_matrix[1]
print test_matrix[2]
print test_matrix[3][0]