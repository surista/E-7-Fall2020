#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""
import matplotlib.pyplot as plt
fig,ax = plt.subplots()

filename = "WorldRecords.csv"

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)
df = pd.read_csv(filename)
df['Year'] = pd.to_datetime(df['Year'],format="%Y")
df_mens = df.loc[df['Event']=='Mens Mile']
df_womens = df.loc[df['Event']=='Womens Mile']

for name in ['A','B','C']:
    ax.plot(df[df.name==name].Year,df[df.name==name].weight,label=name)

ax.set_xlabel("year")
ax.set_ylabel("weight")
ax.legend(loc='best')
