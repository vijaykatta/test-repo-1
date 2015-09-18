# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:49:58 2015

@author: 806112
"""

import pandas as pd;
#df is dataframe
df  = pd.read_csv("irish_cities.txt", sep="\t", skiprows=1)
print df.head()

print sum(df["Population (2000)"])

#change populaiton unit to million
df["Population (2000)"] /= 1000000.0
print df.head()
df.to_csv("irish_cities_modifed.txt", sep="\t")

