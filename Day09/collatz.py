#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S. Urista
Oct 2020
Module documentation goes here
"""
def collatz(n):
    if n == 1:
        raise StopIteration
    while n != 1:
        yield n
        n = n * 3 + 1 if n % 2 else n / 2
    yield 1


def test_collatz():
    g = collatz(4)
    lst = [n for n in g]
    assert lst == [4, 2, 1]

    g = collatz(11)
    lst = [n for n in g]
    assert lst == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    g = collatz(29)
    lst = [n for n in g]
    assert lst == [29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    print('success!')


test_collatz()