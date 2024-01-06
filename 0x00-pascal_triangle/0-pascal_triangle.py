#!/usr/bin/python3
"""
Pascal Triangle Tree
"""


def pascal_triangle(n):
    """
    Method to draw a pascal triangle throw given an integer n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        arr = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                arr[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(arr)

    return triangle
