__author__ = 'sid'
# https://projecteuler.net/problem=20

from EulerUtils import *


def factorial_digit_sum(n):
    sum_of_digits = 0
    for digit in str(fact(n)):
        sum_of_digits += int(digit)

    return sum_of_digits

if __name__ == "__main__":
    print factorial_digit_sum(100)