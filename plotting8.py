# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:12:59 2015

@author: 806112
"""

import matplotlib.pyplot as plt;
import numpy as np

x = np.linspace(0,20,21)
y =0.2*(np.power(0.7,x))
plt.plot(x,y)