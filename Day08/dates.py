#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Description here
"""

class Date(object):
    "Represents a Calendar date"

    def __init__(self, month=0, day=0, year=0):
        "Initialize"
        pass

    def __str__(self):
        "Return a printable string representing the date: m/d/y"
        pass

    def before(self, other):
        "Is this date before that?"


def test_dates():
    t1 = Date(1, 2, 3)
    assert t1.__str__() == '2/1/3'
    t2 = Date(4, 5, 2)
    assert t2.__str__() == '5/4/2'

    assert not t1.before(t1)
    assert not t1.before(t2)
    assert t2.before(t1)

    t2 = Date(4, 1, 3)
    assert t2.__str__() == '1/4/3'

    assert not t1.before(t1)
    assert not t1.before(t2)

    t1 = Date(2, 2, 3)
    t2 = Date(1, 2, 3)
    assert t2.__str__() == '2/1/3'

    assert not t1.before(t1)
    assert not t1.before(t2)
    assert t2.before(t1)

    print("Success!")


test_dates()