import os

project_folder = '/Users/PLN/ECA_Vancouverisland/Model_output/'  # results and data will be saved in this folder

input_folder = '/Users/PLN/ECA_Vancouverisland/Codes/'  # this folder should be the folder containing this script and .csv files

file_identifier = '_v01'  # this string is added to all files written by this code

region_id = 704

country = 'VNM'


fl_centroids = os.path.join(project_folder, 'centr_' + country + file_identifier + '.hdf5')

fl_HAZ_tc_cc0 = os.path.join(project_folder, 'HAZ_tc_mix50_' + country + file_identifier + '.hdf5')

percentile = 97.5
number_rdw = 50 # number of probabilistic tracks generated per historical event
coast_range = 10000 # region where the distance to coastal line is smaller than 10km is defined as coastal area
house_assets = 111.3 * 1000000000 * 1.025**5
population = 150.33 * 1000000

# storm_threshold = 33 # category 1
storm_threshold = 30 # cateogory 3

surge_threshold = 0.5


class Object(object):
    pass


hist_storms = Object()
hist_storms.lon_min = 102
hist_storms.lat_min = 8.5
hist_storms.lon_max = 110
hist_storms.lat_max = 23.5
hist_storms.start_year = 1980 #starting year of the collected historical events
hist_storms.end_year = 2019 #ending year of the collected historical events

horizon = 2050 #future horizon

sea_level_rise = {0:0, 45:0.2, 85:0.3} # under RCP4.5 scenario, sea level rises by 20 cm; RCP8.5, 30 cm.

disc_rate = 0.06

houses_asset_growth = 2

agri_asset_growth = 2

insu_cost_TC_houses = 0.1

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
