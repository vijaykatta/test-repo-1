# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:51:48 2015

@author: 806112
"""

import pandas as pd;
import sqlite3;

con = sqlite3.connect('c:\sqlite\student.db')
df = pd.read_sql_query('select * from student',con)

print df.head()

df.to_csv("student_table_export_from_pandas.csv")
df.to_excel("student_table_export_from_pandas.xls")