__author__ = 'sid'
# https://projecteuler.net/problem=10

from EulerUtils import *


def summation_of_primes(n):
    print sum(seive_of_eratosthenes(n))


if __name__ == "__main__":
    summation_of_primes(2000000)

