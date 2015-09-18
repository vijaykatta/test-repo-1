# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:22:25 2015

@author: 806112
"""

import numpy as np;

x= range(10)

y = np.array(x)+100

print(y.std())

grid = np.linspace(0,8,9)
print(grid)

lp = np.linspace(0,2,9)
print (lp)

print(grid+lp)

print(np.sin(grid))

i= np.random.uniform(10)
print (x)

print(np.linspace(10,11,10))

print(np.linspace(100,200,10))