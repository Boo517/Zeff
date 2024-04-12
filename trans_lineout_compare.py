# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:19:05 2024

@author: noahd
"""

#%%
"""
IMPORTS
"""
import file_ui_utils as utils
import matplotlib.pyplot as plt
import numpy as np

#%%
"""
CONSTANTS
"""
px2um = 0.08 # [microns/px], multiply px by px2um to get um
# using beta because it's what I have for the foam directly
# as opposed to linear attenuation coefficient
# foam val from what Pia gave me, all others from Henke LBL index of
# refraction calculator
b_al = 1.44183886*10**-7
b_pn = 5.04027087*10**-9
b_pp = 3.8206891*10**-9
b_100mg = 6.92848349*10**-10

wavelength = .151201*10**-9 # [m] 8.2 keV xrays

L = 500*10**-6 # [m] target diameter, taking lineouts at max width
# L = *10**-6# [m] for seeing if offcenter, could help transmission

atten = lambda beta : np.exp(-4*np.pi*beta*L/wavelength)
# gives expected ratio of incident to transmitted x-ray intensity
# given beta

#%%
"""
FILE SELECT
"""
ui = utils.UI()
# choose transmission and integrated phase csv
trans_file = ui.getfile("choose transmission csv")
trans = np.loadtxt(trans_file, delimiter=",", skiprows=1) # [um], [unitless]
# trans[:,0] = trans[:,0]*px2um   # convert -> [um], [unitless]
# ^no longer needed bc converted in imagej

#%%
"""
PLOT
"""
fig, ax = plt.subplots()
# attenuation from TNT, lineout in y, across layers from cone to aerogel
# taking middle as max width for now
# FOV is 204 um at the target, which is half the target diameter, meaning
# the path length at either end (if the middle is max width) is 86.66%
# of the full width 
plt.plot(trans[:,0], trans[:,1], color='C0', label="Lineout")

# expected attenuation from materials' beta
plt.axhline(y=atten(b_al), color='C1', linestyle='--', label="Aluminum")
plt.axhline(y=atten(b_pn), color='C2', linestyle='--', label="Parylene-N")
plt.axhline(y=atten(b_pp), color='C3', linestyle='--', label="Polypropylene")
plt.axhline(y=atten(b_100mg), color='C4', linestyle='--', label="C15H20O6 Foam")

# labels
ax.legend()
ax.set_xlabel("Distance [µm]")
ax.set_ylabel("Transmission")