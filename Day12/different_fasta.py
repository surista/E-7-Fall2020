#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""
from collections import defaultdict
def read_fasta_file(filename: str) -> str:
    with open(filename, 'r') as f:
        temp = [line.strip() for line in f]

    seq = ''.join(temp[1:])

    return seq

def longest_repeat(text):

    cntr = 2
    d = defaultdict(list)
    for i in range(len(text)):
        d[text[i:i + cntr]].append(i)
    del_list = [(d[item]) for item in d if len(d[item]) > 1]
    sol = (0,0,0)
    while len(del_list) > 0:

        d = defaultdict(list)
        cntr += 1
        for item in del_list:
            for i in item:
                d[text[i:i + cntr]].append(i)
        del_list = [(d[item]) for item in d if len(d[item]) > 1]
        if len(del_list) != 0:
            sol = (del_list[0][0], del_list[0][1], cntr)

    return sol

text = read_fasta_file("Human22.fasta")
