# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:06:40 2015

@author: 806112
"""

import matplotlib.pyplot as plt;
import numpy as np;

x= np.linspace(0,10,20)
y= 1.7*x + 12.3*np.sin(x*3)
plt.plot(x,y);
print(len(x))