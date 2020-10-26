#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""

# month_names = ['January', 'February', 'March', 'April', 'May', 'June',
#                 'July', 'August', 'September', 'October', 'November', 'December']
#
# def next_month(name: str) -> str:
#     "Return a stream of the following months"
#     if name not in month_names:
#         raise ValueError
#     yield month_names

#
# gen = next_month('Octofber')
#

def squares(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = squares([1,2,3,4,5])

print(my_nums)