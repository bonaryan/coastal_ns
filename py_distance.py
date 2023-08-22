### Calculates the distance to the nearest cell with a specific state (e.g. shoreline)
### Input: discrete raster of categories (e.g. 1 = shoreline, 0 = no no shoreline)
### Sets evidence on node continuous node (Distance_shoreline)

# import packages
import os
import sys
import numpy
from osgeo.gdalconst import *
from osgeo import gdal
import math
from node_utils import *
from scipy.spatial import distance

# set names for labelling the script while running
SCRIPT_NAME = "CONT_DISTANCE: "  # to add as a prefix for all messages
CELLS_PRINTING = 10

# SET FUNCTION PARAMETERS
# name of input node
input_name = "shoreline"
# number of the state in the input raster that defines the cells (e.g. shoreline), the distance to which we are interested in
state_number = 0;
# name of output node
output_name = "Distance_shoreline"


# function that finds cells of interest
def isShoreline(node, cell):
    return (getStateHighestLikelihood(node, cell) == state_number)

# function that finds distance to the nearest cell of interest
def findCloserShoreCell(cell, shore_list, width):

    if (len(shore_list) == 0):
        print("findCloserShoreCell: There are no shoreline in the map.")
        return None

    return min(distance.cdist([cell], shore_list, 'euclidean')[0])

# function that writes distance to the output node
def process(dataset,nodes_data,iteration):

     # only use it at the beginning
    if (iteration != -1):
        return []

    node_shoreline = getNodeByName(nodes_data, input_name)
    if (not node_shoreline):
        print(SCRIPT_NAME, "ERROR Node", input_name, "is not in nodes_data")
        return []

    total_cells = dataset.RasterXSize * dataset.RasterYSize ;

    # get pixel size
    pixelsize = dataset.GetGeoTransform()[1]

    print(SCRIPT_NAME, "pixelsize:", pixelsize)

    shoreline_cells = [];

    for cell in range(total_cells ):

        if (isShoreline(node_shoreline,cell)):
            shoreline_cells.append(cell);

    print(SCRIPT_NAME, "There are", len(shoreline_cells), "cells that are shoreline")

    distances=[]

    # Transform to 2-dimensional array
    shoreline_coords = list(map(lambda x: [x / dataset.RasterXSize, x % dataset.RasterXSize], shoreline_cells))

    # append distances to new array
    for cell in range(total_cells ):

        if (isNODATA(node_shoreline, cell)):
            distances.append(PY_NODATA_VALUE)
        elif isShoreline(node_shoreline, cell):
            distances.append(0)
        else:
            distances.append(findCloserShoreCell([cell / dataset.RasterXSize, cell % dataset.RasterXSize], shoreline_coords, dataset.RasterXSize) * pixelsize)


    new_nodes_data = [{'name' : output_name, 'type': PY_CONTINUOUS, 'data': distances}]


    for i in range(CELLS_PRINTING):
        print(SCRIPT_NAME, "cell:", i, ":" ,  new_nodes_data[0]['data'][i])


    if (validResultData(new_nodes_data, total_cells)):
        return new_nodes_data

    else:
        print ("Some error here: ")
