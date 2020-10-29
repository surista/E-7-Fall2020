#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""


class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return '(%.d, %.d)' % (self.x, self.y)
        return '({self.x},{self.y})'.format(self = self)


    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


x = Point(3, 4)
print(x)

