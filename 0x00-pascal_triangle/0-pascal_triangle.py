#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Return list of integers lists
    representing Pascal's triangle
    for n >= 0, return empty list"""

    if n <= 0:
        return []

    output = [0] * n

    for a in range(n):
        tp = [0] * (a+1)
        tp[0] = 1
        tp[len(tp) - 1] = 1
        
        for b in range(1, a):
            if b > 0 and b < len(tp):
                i = output[a - 1][b]
                j = output[a - 1][b - 1]
                tp[b] = i + j
        output[a] = tp

    return (output)
