#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Find complement of A/T and C/G
"""


def dna_complement(text: str) -> str:
    """Return the complement of string text"""

    dna_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    text = text.upper()

    sol = ''.join([dna_dict[char] for char in text])

    return sol
