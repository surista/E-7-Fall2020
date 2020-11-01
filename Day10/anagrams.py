#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
find anagrams in list of words
"""
import cProfile
def are_anagrams(word1, word2):
    # Are the two words anagrams?

    # must be same length
    if len(word1) != len(word2):
        return False

    # can't be the same word
    if word1 == word2:
        return False

    # sort each string alphabetically and compare
    return sorted(word1.lower()) == sorted(word2.lower())


def test_anagrams():
    assert (are_anagrams('abets', 'beats'))
    assert (are_anagrams('hash', 'shah'))
    assert (are_anagrams('Hash', 'Shah'))

    assert (not are_anagrams('hash', 'sash'))
    assert not are_anagrams("zombies", "pants")
    assert are_anagrams('streams', 'masters')
    assert are_anagrams('inlets', 'listen')

    return ('Success!')

cProfile.run("test = are_anagrams('abets', 'beats')")

print(test_anagrams())