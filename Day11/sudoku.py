#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Given three lists, produce list of legal sudoku movese
"""
def legal_values(row, col, square):
    full_moves=[1,2,3,4,5,6,7,8,9]
    full_list = row + col + square
    return [item for item in full_moves if item not in full_list]


def test_sudoku():
    assert (legal_values([1], [4], [7]) == [2, 3, 5, 6, 8, 9])
    assert (legal_values([1, 2, 3], [4, 5, 6], [7, 8, 9]) == [])
    assert (legal_values([1, 2, 3], [1, 2, 3], [7, 8, 9]) == [4, 5, 6])
    assert (legal_values([1, 3, 5], [1, 4, 8], [7, 8, 9]) == [2, 6])
    assert (legal_values([1, 3, 5, 7, 9], [2, 4, 6, 8], [7, 9]) == [])
    assert (legal_values([1, 5, 7, 9], [2, 4, 8], [7, 9]) == [3, 6])
    print('Pass!')


test_sudoku()