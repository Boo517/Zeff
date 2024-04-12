# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:33:08 2024

@author: noahd
"""

#%%
"""
IMPORTS
"""
import file_ui_utils as utils
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#%%
"""
FILE SELECT
"""
ui = utils.UI()
data_file = ui.getfile("Select a CSV to remove slope from")
data = np.loadtxt(data_file, delimiter=",", skiprows=1)

#%%
"""
LINEAR FIT
"""
# create fit line
fit = data.copy() # to get same x coords
results = sp.stats.linregress(data)
slope = results.slope
intercept = results.intercept
# y=mx+b
fit[:,1] = slope*fit[:,0] + intercept
# remove slope
sub = data.copy()
sub[:,1] =  data[:,1] - fit[:,1]

#%%
"""
PLOT
"""
fig, ax = plt.subplots()
ax.plot(data[:,0], data[:,1], label="og data")
ax.plot(fit[:,0], fit[:,1], label="fit line", linestyle="--")
ax.plot(sub[:,0], sub[:,1], label="slope removed")
ax.legend()

#%%
"""
SAVE
"""
fname = data_file.split(".")[0] # path+name
np.savetxt(fname+"_slope_removed.csv", sub, delimiter=",")


