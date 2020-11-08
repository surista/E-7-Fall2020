#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Chart men's and women's mile timese
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def mile_record(filename):
    sol = {}
    desired_width=320
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns',10)
    df = pd.read_csv(filename)

    df2 = df[(df['Event'] =='Mens Mile') | (df['Event'] == 'Womens Mile')]

    x = df2['Year']
    y = df2['Record']

    sns.scatterplot(x=x, y=y, hue='Event', palette='deep', data=df2)

    plt.title("Men's and Women's Mile Records")
    plt.xlabel('Year')
    plt.ylabel('Time in seconds')
    plt.legend(loc='upper left')

    plt.show()

filename = "WorldRecords.csv"
print(mile_record(filename))