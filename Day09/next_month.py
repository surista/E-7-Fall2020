#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""

month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']

def next_month(name: str) -> str:
    "Return a stream of the following months"
    if name not in month_names:
        raise ValueError
    month = month_names.index(name) + 1
    while (True):
        month = (month % 12)
        yield month_names[month]
        month += 1


def test_months():
    gen = next_month('October')
    lst = [next(gen) for i in range(15)]
    assert(lst == ['November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January'])

    gen = next_month('December')
    assert next(gen) == 'January'

    print('Success!')

test_months()