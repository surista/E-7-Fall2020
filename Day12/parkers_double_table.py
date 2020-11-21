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

    sol = (0,0,0)
    count = 2
    while True:

        d = defaultdict(list)
        for i in range(len(text)):
            d[text[i:i+count]].append(i)
        del_list = [(item, d[item]) for item in d if len(item) > 1 and len(d[item]) > 1]
        if len(del_list) == 0:
            return sol
        else:
            temp = [(item[1][0], item[1][1], len(item[0])) for item in del_list]
            sol = (temp[0][0], temp[0][1], temp[0][2])
            print(sol)
        count += 1


# text = read_fasta_file("pKLMF-FX.fasta")
# print(longest_repeat(text))
#
# text = read_fasta_file("pACYC184.fasta")
# print(longest_repeat(text))

text = read_fasta_file("ecoli.fasta")
print(longest_repeat(text))