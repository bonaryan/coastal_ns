import os

project_folder = '/Users/PLN/NS/Model_output/'  # results and data will be saved in this folder

input_folder = '/Users/PLN/NS/Codes/'  # this folder should be the folder containing this script and .csv files

file_identifier = '_v01'  # this string is added to all files written by this code

country = 'CA'

fl_centroids = os.path.join(project_folder, 'centr_' + country + file_identifier + '.hdf5')

fl_HAZ_tc_cc0 = os.path.join(project_folder, 'HAZ_tc_mix50_' + country + file_identifier + '.hdf5')

percentile = 97.5
number_rdw = 50 # number of probabilistic tracks generated per historical event
coast_range = 10000 # region where the distance to coastal line is smaller than 10km is defined as coastal area
building_assets = 111.3 * 1000000000 * 1.025**5
population = 150.33 * 1000000

# storm_threshold = 33 # category 1
storm_threshold = 30 # category 3

surge_threshold = 0.5


class Object(object):
    pass


hist_storms = Object()
hist_storms.lon_min = 59
hist_storms.lat_min = 43
hist_storms.lon_max = 67
hist_storms.lat_max = 48
hist_storms.start_year = 1964 #starting year of the collected historical events
hist_storms.end_year = 2003 #ending year of the collected historical events

horizon = 2050 #future horizon

sea_level_rise = {0:0, 45:0.2, 85:0.3} # under SSP4.5 scenario, sea level rises by 20 cm; SSP8.5, 30 cm.

disc_rate = 0.02

building_asset_growth = 0.067

population_growth = 1.13



## define colormaps

import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt

upper = plt.cm.Blues(np.arange(256))
lower = np.ones((1,4))
# combine parts of colormap
cmap = np.vstack(( lower, upper ))
# convert to matplotlib colormap
cmap = colors.ListedColormap(cmap, name='myColorMap', N=cmap.shape[0])

upper = plt.cm.Reds(np.arange(256))
cmap_red = np.vstack(( lower, upper ))
# convert to matplotlib colormap
cmap_red = colors.ListedColormap(cmap_red, name='myColorMap', N=cmap_red.shape[0])
