#!/usr/bin/python3
""" Module for the Prime Game """


def isWinner(x, nums):
    """Solves the Prime Game"""

    if not nums or x < 1:
        return None
    n = max(nums)
    el = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not el[i]:
            continue
        for j in range(i*i, n + 1, i):
            el[j] = False

    el[0] = el[1] = False
    c = 0
    for i in range(len(el)):
        if el[i]:
            c += 1
        el[i] = c

    player1 = 0
    for n in nums:
        player1 += el[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
