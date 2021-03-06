#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Find complement of A/T and C/G
"""


def dna_complement(text):
    """Return the complement of reversed string"""

    # map complements, reverse string
    dna_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    text = text.upper()[::-1]

    sol = ''.join([dna_dict[char] for char in text])

    return sol


def test_complement():
    assert (dna_complement('A') == 'T')
    assert (dna_complement('a') == 'T')
    assert (dna_complement('c') == 'G')
    assert (dna_complement('CaT') == 'ATG')
    assert (dna_complement('AAAACCCGGT') == 'ACCGGGTTTT')

    print("Success!")


test_complement()