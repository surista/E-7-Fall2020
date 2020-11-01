#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""
import csv


x = 14+25
if x >= 24:
    x %= 24
if x >=13:
    period = "PM"
else:
    period = "AM"

if x > 12:
    x -= 12

print(x, period)
