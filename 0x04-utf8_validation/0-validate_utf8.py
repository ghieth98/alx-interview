#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Method that determines if a given data set represents
     a valid utf-8 encoded string
    """
    def check(num):
        checker = 1 << (8 - 1)
        i = 0
        while num & checker:
            checker >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = check(data[i])
            if cur != 1:
                return False
            i += 1
    return True
