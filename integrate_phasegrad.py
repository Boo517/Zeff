# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:22:26 2024

@author: noahd
"""

#%%
"""
IMPORTS
"""
import numpy as np
import file_ui_utils as utils
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#%%
"""
CONSTANTS
"""
px2um = 0.08 # pixel size [um], multiply pixels by it to convert to um

# delta, the real component of the index of refraction
# foam val from what Pia gave me, all others from Henke LBL index of
# refraction calculator
d_al = 8.15728163*10**-6
d_pn = 3.69496365*10**-6
d_pp = 3.17691111*10**-6
d_100mg = 6.92848349*10**-10

wavelength = .151201*10**-9 # [m] 8.2 keV xrays

L = 500*10**-6 # [m] target diameter, taking lineouts at max width

# starting phase, given the delta for the material integration starts from 
# according to deltaphi=2pideltaL/lambda
initial_phase = lambda delta: 2*np.pi*delta*L/wavelength 

#%%
"""CHANGE THIS IF STARTING FROM DIFFERENT MATERIAL
"""
phase_offset = initial_phase(d_pp)

#%%
"""
LOAD
"""
ui = utils.UI()
f = ui.getfile("choose csv to integrate")
gradient = np.loadtxt(f, delimiter=",", skiprows=1)     # [um], [rad/um]
# gradient[:,0] = gradient[:,0]*px2um     # convert -> [um], [rad/um]
# ^ no longer needed bc converted in imagej
# gradient is in rad/um, so we need to integrate with x in um to get rad

"""
CHANGE THIS BACK!!
"""
# gradient[:,0] = gradient[:,0]/px2um # convert um->px for experiment

# plot
fig, ax = plt.subplots()
ax.plot(gradient[:,0], gradient[:,1])
ax.set_title("phase gradient")
ax.set_xlabel("distance [um]")
ax.set_ylabel("phase gradient [rad/um]")

#%%
"""
INTEGRATE
"""
integ_phase = gradient.copy()
integ_phase[:,1] = integrate.cumulative_simpson(gradient[:,1], x=gradient[:,0],
                                                initial=0.01)
# phase offset from inital value
plus = integ_phase.copy()
plus[:,1] = integ_phase[:,1]+phase_offset

# plot
fig, ax = plt.subplots()
ax.plot(integ_phase[:,0], integ_phase[:,1], label="without pp phase offset")
ax.plot(plus[:,0], plus[:,1], label="with pp phase offset")
ax.set_title("integrated phase")
ax.set_xlabel("distance [um]")
ax.set_ylabel("phase [rad]")
ax.legend()
plt.show()

#%% 
"""
SAVE
"""
fname = f.split(".")[0]
np.savetxt(fname+"_integrated.csv", integ_phase, delimiter=",")
np.savetxt(fname+"_integrated+{}.csv".format(phase_offset), 
           plus, delimiter=",")
