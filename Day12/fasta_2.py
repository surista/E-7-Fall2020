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
    count = 1
    d = defaultdict(list)
    for i in range(len(seq)):
        d[seq[i:i + count]].append(i)
    defdict(d, seq, count)



def defdict(d, seq, count):
    while count < len(seq):
        for i in range(len(seq)):
            d[seq[i:i + count]].append(i)

        for key in d:
            if len(d[key]) < 2:
                del d[key]
                count += 1

        defdict(d, seq, count)

    return(d)

filename = 'temp.fasta'
gen = read_fasta_file(filename)

print(gen)
