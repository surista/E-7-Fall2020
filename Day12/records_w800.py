#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""
import pandas as pd
import matplotlib.pyplot as plt
filename = "WorldRecords.csv"
# read in data
df = pd.read_csv(filename)
# filter to women's 800m
df2 = df[(df['Event'] =='Womens 800m')]
nats = {}
for index, row in df2.iterrows():
    if row['Nationality'] not in nats:
        nats[row['Nationality']] = 1
    else:
        nats[row['Nationality']] += 1

nats = sorted(nats.items())
x = [k[0] for k in nats]
y = [k[1] for k in nats]

plt.bar(x,y)
plt.show()