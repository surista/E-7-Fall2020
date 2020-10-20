#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
splits a list of integers into odds & evens
"""

def odds_n_evens(i_list):
    """splits a list of integers into two halves, odds then evens"""

    odds = ([i for i in i_list if i % 2 ==1])
    evens = ([i for i in i_list if i % 2 == 0])
    return odds + evens
