# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 04:33:33 2024

@author: noahd
"""
#%%
"""
IMPORTS
"""
import file_ui_utils as utils
import numpy as np
import matplotlib.pyplot as plt
import os

#%%
"""
CONSTANTS
"""
# px2um = 0.08 # pixel size [um], multiply pixels by it to convert to um
# refraction ratios (beta over delta) for sandwich materials
# from henke.lbl.gov (Lawrence Berkeley website) except aerogel, which
# is from files Pia gave me
pp_ratio = 0.001204 # ablator
pn_ratio = .00136389 # pusher
foam_ratio = .0020966 # foam
al_ratio = 0.01767 # shield
#%%
"""
FILE SELECT
"""
ui = utils.UI()
zeff50_f = ui.getfile("choose zeff.csv for 50mg")
zeff50 = np.loadtxt(zeff50_f, delimiter=",", skiprows=0) # [um], [unitless]

zeff100_f = ui.getfile("choose zeff.csv for 100mg")
zeff100 = np.loadtxt(zeff100_f, delimiter=",", skiprows=0) # [um], [unitless]

zeff500_f = ui.getfile("choose zeff.csv for 500mg")
zeff500 = np.loadtxt(zeff500_f, delimiter=",", skiprows=0) # [um], [unitless]

#%%
"""
PLOT
"""
fig, ax = plt.subplots()
ax.plot(zeff50[:,0], zeff50[:,1], color='C0', label="50 mg/cc target")
ax.plot(zeff100[:,0], zeff100[:,1], color='C1', label="100 mg/cc target")
ax.plot(zeff500[:,0], zeff500[:,1], color='C2', label="500 mg/cc target")
# materials
plt.axhline(y=al_ratio, color='C3', linestyle='--', label="Aluminum")
plt.axhline(y=foam_ratio, color='C4', linestyle='--', label="C15H2OO6 Foam")
plt.axhline(y=pn_ratio, color='C5', linestyle='--', label="Parylene-N")
plt.axhline(y=pp_ratio, color='C6', linestyle='--', label="Polypropylene")
ax.legend()
# ax.set_title("Zeff")
ax.set_xlabel("distance [μm]")
ax.set_ylabel("β/δ")
plt.show()