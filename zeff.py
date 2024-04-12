# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:43:46 2024

@author: noahd
"""

import file_ui_utils as utils
import numpy as np

#%%
"""
FUN
"""
def ratio(transmission, phasechange):
    return -np.log(np.abs(transmission))/(2*phasechange)

def inv_ratio(transmission, phasechange):
    return -(2*phasechange)/np.log(np.abs(transmission))

# remove <=0, to not mess w log
# 10^-4 for now, bc smaller than what we've seen
def truncate(image):
    image[image<=0] = 1*10**-4
    image[image>1] = 1
    return image

def truncate_selection(val):
    (files, images, folder) = utils.select_images(["truncate"])
    image = images["truncate"]
    image[image>val] = val
    image[image<-val] = -val
    images["truncated"] = image
    utils.save_images(images, ["truncated"], folder)

def main():
    (files, images, folder) = utils.select_images(
        ["transmission", "phasechange"])
    images["truncated_trans"] = truncate(images["transmission"])
    images["r"] = ratio(images["truncated_trans"], images["phasechange"])
    # images["r"] = inv_ratio(images["truncated_trans"], images["phasechange"])
    utils.save_images(images, ["truncated_trans", "r"], folder)

#%%
"""
MAIN
"""
if __name__ == "__main__":
    main()