You can just import this parser in your code.

The function is "tsplib_xml_parse (filename)".

filename is a valid path to an XML TSP LIB file.

This new function should return a list of 
    - The name of the dataset as a string
    - The number of cities as an integer
    - The data set itself, as a list of lists