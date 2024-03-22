# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:43:46 2024

@author: noahd
"""

import file_ui_utils as utils
import numpy as np

#%%

def ratio(transmission, phasechange):
    return -np.log(transmission/(2*phasechange))


def main():
    (files, images, folder) = utils.select_images(
        ["transmission", "phasechange"])
    r = ratio(images["transmission"], images["phasechange"])
    utils.save_images({"r":r}, "r", folder)

#%%
"""
MAIN
"""
if __name__ == "__main__":
    main()