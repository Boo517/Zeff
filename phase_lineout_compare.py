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

# delta, the real component of the index of refraction
# foam val from what Pia gave me, all others from Henke LBL index of
# refraction calculator
d_al = 8.15728163*10**-6
d_pn = 3.69496365*10**-6
d_pp = 3.17691111*10**-6
d_100mg = 3.30461120*10**-7


wavelength = .151201*10**-9 # [m] 8.2 keV xrays

L = 500*10**-6 # [m] target diameter, taking lineouts at max width

delta_phase = lambda delta : 2*np.pi*delta*L/wavelength
# gives expected change in phase angle after passing through material with
# given real part of refractive index delta

#%%
"""
FILE SELECT
"""
ui = utils.UI()
# choose transmission and integrated phase csv
phase_file = ui.getfile("choose integrated phase csv")
phase = np.loadtxt(phase_file, delimiter=",", skiprows=1) # [px], [radians]
# phase[:,0] = phase[:,0]*px2um   # convert -> [um], [radians]
# ^ already converted in imagej

#%%
"""
PLOT
"""
fig, ax = plt.subplots()
# phase gradient from TNT, integrated manually with initial value from
# known polypropylene ablator beta and target width
# lineout in y, across layers from cone to aerogel foam at ~max width 
# (for now, just using middle of image)
# FOV is 204 um at the target, which is half the target diameter, meaning
# the path length at either end (if the middle is max width) is 86.66%
# of the full width 
plt.plot(phase[:,0], phase[:,1], color='C0', label="Lineout")

# expected attenuation from materials' beta
plt.axhline(y=delta_phase(d_al), color='C1', linestyle='--', label="Aluminum")
plt.axhline(y=delta_phase(d_pn), color='C2', linestyle='--', label="Parylene-N")
plt.axhline(y=delta_phase(d_pp), color='C3', linestyle='--', 
            label="Polypropylene")
plt.axhline(y=delta_phase(d_100mg), color='C4', linestyle='--', 
            label="C15H20O6 Foam")

# labels
ax.legend()
ax.set_xlabel("Distance [µm]")
ax.set_ylabel("Phase Change [radians]")