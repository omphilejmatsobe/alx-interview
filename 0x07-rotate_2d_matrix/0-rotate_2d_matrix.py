#!/usr/bin/python3
"""Rotates 2-D matrix"""


def rotate_2d_matrix(m):
    """Arranges and Rotates a matrix in-place"""

    x = len(m)
    temp1, temp2 = 0, 0

    for j in range(0, len(m) // 2 + 1):
        for i in range(j, (x - 1)):
            temp1 = m[i][(x - 1)]
            m[i][x - 1] = m[j][i]

            temp2 = m[x - 1][x - 1 - i + j]
            m[x - 1][x - 1 - i + j] = temp1

            temp1 = m[x - 1 - i + j][j]
            m[x - 1 - i + j][j] = temp2

            m[j][i] = temp1

        n -= 1
