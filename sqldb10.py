# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:01:49 2015

@author: 806112
"""

import sqlite3;

conn = sqlite3.connect('c:\sqlite\student.db')
c= conn.cursor()
c.execute("SELECT * FROM grades;")
for i in c:
    print i
 
