#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

text = "AGGCTAGCT"
lst = [text[i:] for i in range(len(text))]
for x in sorted(lst):
    print(x)

for x in range(len(lst)-1):
