#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""
import re

def read_fasta_file(filename: str) -> str:
    with open(filename, 'r') as f:
        temp = [line.strip() for line in f]

    seq = ''.join(temp[1:])

    return seq

def find_repeating(length, n, seq):
    sol = set()
    for i in range(n-length+1):
        sub_string = seq[i:i+length]

        if sub_string in sol:
            return (sub_string)

        sol.add(sub_string)

    return False


def longest_repeat(seq):
    n = len(seq)
    left = 0
    right = n - 1

    while left < right:
        mid = left + (right - left + 1) // 2
        if find_repeating(mid, n, seq):
            x = find_repeating(mid,n, seq)
            left = mid

        else:
            right = mid - 1

    sol = [i.start() for i in list(re.finditer(x, seq))]
    return (sol[0], sol[1], left)

seq = read_fasta_file("pACYC184.fasta")
print(longest_repeat(seq))