#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S. Urista
Nov 2020
Module documentation goes here
"""
# Take a string and look for the longest repeat
# Return a tuple: (pos1, pos2, length) or None if there are no repeats
# pos1 != pos2 and text[pos1:pos1+length)] == text[pos2:pos2+length]
def read_fasta_file(filename: str) -> str:
    with open(filename, 'r') as f:
        temp = [line.strip() for line in f]
    seq = ''.join(temp[1:])
    return seq


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        D = [ord(c) - ord('a') for c in S]
        P = 26
        MOD = 2 ** 32

        def rolling_hash(L):
            # initial window
            h = 0
            for c in D[:L]: h = (h * P + c) % MOD
            seen = {h}

            PP = P ** L % MOD
            # sliding window
            for r, c in enumerate(D[L:], L):
                # update window
                #  shift left    emit the old left    adding the new right
                h = (h * P - D[r - L] * PP + c) % MOD
                if h in seen: return r - L + 1  # return start index for the duplicated window
                seen.add(h)
            return None

        # use binary search to find the max length of duplicated windows
        l, h = 0, len(S)
        while l < h:
            m = (l + h) // 2
            if rolling_hash(m):
                l = m + 1
            else:
                h = m
        start = rolling_hash(l - 1)
        return S[start: start + l - 1]

text = read_fasta_file("Human22.fasta")
gen = Solution()
print(gen.longestDupSubstring(text))