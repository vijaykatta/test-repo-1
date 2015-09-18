# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:21:45 2015

@author: 806112
"""

import numpy as np;


x= np.genfromtxt("np_test_data.txt")

print(x.T)

np.savetxt("np_test_data_plus_one_transposed.txt", x.T)

    