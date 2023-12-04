#!/usr/bin/python3


import sys


def generate_result(row, column):
    res= [[]]
    for queen in range(row):
        res = place_queen(queen, column, res)
    return res


def place_queen(queen, column, prev_solution):
    position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                position.append(array + [x])
    return position


def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))

def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n



def queens():

    n = init()
    # generate all solutions
    solutions = generate_result(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    queens()
