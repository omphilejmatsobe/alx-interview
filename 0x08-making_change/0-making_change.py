#!/usr/bin/python3
"""
Given a pile of coins of different values this program determines the fewest
number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Class makeChange that determines change in coins
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    sum = 0
    x = 0
    counter = 0
    coin_count = len(coins)
    while sum < total and x < coin_count:
        while coins[x] <= total - sum:
            sum += coins[x]
            counter += 1
            if sum == total:
                return counter
        x += 1
    return -1
