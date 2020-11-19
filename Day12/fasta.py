#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""

# def read_fasta_file(filename: str) -> str:
#     with open(filename, 'r') as f:
#         temp = [line.strip() for line in f]
#
#     seq = ''.join(temp[1:])
#
#     repeat = []
#     max = (0,0,0)
#     for x in range(len(seq)):
#         for y in range(x+1, len(seq)):
#             if seq[x:y] in seq[y:]:
#                 repeat = [seq[x:y]]
#             else:
#                 if len(repeat[0]) > max[0]:
#                     max = (len(repeat[0]),repeat[0])
#                     sol = x, x+max[0], max[0], seq[x:x+max[0]]
#
#     return sol
#
# filename = 'pKLMF-FX.fasta'
# print(read_fasta_file(filename))





#
# def read_fasta_file(filename: str) -> str:
#     with open(filename, 'r') as f:
#         temp = [line.strip() for line in f]
#
#     seq = ''.join(temp[1:])
#
#     seq_length = len(seq)
#     seq_table = [[0 for x in range(seq_length + 1)] for y in range(seq_length + 1)]
#
#     sol = ""
#     sol_length = 0
#
#     index = 0
#     for i in range(1, seq_length + 1):
#         for j in range(i + 1, seq_length + 1):
#
#             if (seq[i - 1] == seq[j - 1] and
#                     seq_table[i - 1][j - 1] < (j - i)):
#                 seq_table[i][j] = seq_table[i - 1][j - 1] + 1
#
#                 if (seq_table[i][j] > sol_length):
#                     sol_length = seq_table[i][j]
#                     index = max(i, index)
#
#             else:
#                 seq_table[i][j] = 0
#
#     if (sol_length > 0):
#         for i in range(index - sol_length + 1,
#                        index + 1):
#             sol = sol + seq[i - 1]
#
#     return i, i-sol_length, sol_length
#
# filename = 'pKLMF-FX.fasta'
# print(read_fasta_file(filename))

from collections import defaultdict

def read_fasta_file(filename: str) -> str:
    with open(filename, 'r') as f:
        temp = [line.strip() for line in f]

    seq = ''.join(temp[1:])

    d = defaultdict(list)
    for i in range(len(seq)):
        for y in range(len(seq)-1):
            d[seq[i:i+y]].append(i)

    return d

filename = 'pKLMF-FX.fasta'
gen = read_fasta_file(filename)
print(gen.items())