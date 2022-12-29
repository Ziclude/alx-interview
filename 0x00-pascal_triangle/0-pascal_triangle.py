#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Return list of integers lists
    representing Pascal's triangle
    for n >= 0, return empty list"""

    if n <= 0:
        return []

    output = [[1]]

    for a in range(n - 1):
        tp = [0] + output[-1]+[0]
        rw = []
        for b in range(len(output[-1]) + 1):
            rw.append(tp[b] + tp[b + 1])
            output.append(rw)

    return (output)
