__author__ = 'sid'
# https://projecteuler.net/problem=16

import math


def power_digit_sum(number, power):
    result = 0
    for i in str(int(math.pow(number, power))):
        result += int(i)

    print result


if __name__ == "__main__":
    power_digit_sum(2, 1000)

