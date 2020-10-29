#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
splits a list of integers into odds & evens
"""

def odds_n_evens_alternate(lst):
    # re-orders list into odds and evens
    # concatenates two LCs

    odds = [i for i in lst if i % 2 == 1]
    evens = [i for i in lst if i % 2 == 0]

    return odds + evens


def odds_n_evens(lst):
    # re-orders list into odds and evens
    # uses nested LC

    return [x for rem in range(1, -1, -1) for x in lst if x % 2 == rem]

