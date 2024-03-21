#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    """

    if n < 2:
        return 0

    res = []
    x = 1
    while n != 1:
        x += 1
        if n % x == 0:
            while n % x == 0:
                n /= x
                res.append(x)

    return sum(res)
