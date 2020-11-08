#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import numpy as np
import pandas as pd
import csv      # Read Comma Separated Values (CSV) files
import sys      # Read filename from command line


filename = "WorldRecords.csv"

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)
df = pd.read_csv(filename)
df['Year'] = pd.to_datetime(df['Year'],format="%Y")
df_mens = df.loc[df['Event']=='Mens Mile']
df_womens = df.loc[df['Event']=='Womens Mile']


df.set_index(['Year'])
df_type = df['Type']='100m'
x = df_mens['Year']
y = df_mens['Record']
x2 = df_womens['Record']
plt.plot(x,y)
plt.plot(x2,y)
plt.show()



# def mile_record(filename):
#     sol = {}
#     try:
#         with open(filename, 'r') as f:
#             csv_file = csv.DictReader(f)
#             for row in csv_file:
#                 print(row)
#
#     except FileNotFoundError:
#         print("Houston we have a problem, no such file exists:",filename)
#
#     return sol
#
# filename = "WorldRecords.csv"
#
# mile_record(filename)