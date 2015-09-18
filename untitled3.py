# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:38:46 2015

@author: 806112
"""

infile = open("file_of_integers.txt","r")
x=0

for line in infile:
    x=x+int(line)
    print(x)
    
infile.close()
