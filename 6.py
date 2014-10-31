__author__ = 'sid'
# https://projecteuler.net/problem=6

import math


def sum_square_difference(N):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, N + 1):
        sum_of_squares += i * i
        square_of_sum += i

    print int(math.pow(square_of_sum, 2) - sum_of_squares)

if __name__ == "__main__":
    sum_square_difference(100)


