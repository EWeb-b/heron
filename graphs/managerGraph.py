#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:50:06 2018

@author: ll14m3k
"""

import matplotlib.pyplot as plt
import numpy as np


def weeklyTakings(weekCommencing):
    x = np.array([0,1,2,3,4,5,6])
    y = np.array([0,1000,2000,3000])
    my_xticks = ['Monday','Tuesday','Wednesday','Thursday', 'Friday']
    plt.xticks(x, my_xticks)
    plt.plot(x, y)
    plt.show()