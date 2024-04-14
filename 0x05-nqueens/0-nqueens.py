#!/usr/bin/python3

"""
The N queens is a puzzle of placing N non-attacking queens on N×N chessboard.
This program solves the N queens problem.
"""

import sys


def place(row, column):
    """
    Solves the placement
    """
    solver = [[]]
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver


def place_queen(q, column, prev_solver):
    """
    Places the queen
    """
    queen_arr = []
    for array in prev_solver:
        for x in range(column):
            if is_safe(q, x, array):
                queen_arr.append(array + [x])
    return queen_arr


def is_safe(q, i, array):
    """
    """
    if i in array:
        return (False)
    else:
        return all(abs(array[column] - i) != q - column
                   for column in range(q))


def init():
    """
    Init
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (queen)


def puzzle():
    """
    the module to solve the puzzle
    """
    queen = init()
    solver = place(queen, queen)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    puzzle()
