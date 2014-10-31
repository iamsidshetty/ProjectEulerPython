__author__ = 'sid'

# https://projecteuler.net/problem=7

from EulerUtils import *


def st_prime():
    print seive_of_eratosthenes(1000000)[10000]

if __name__ == "__main__":
    st_prime()
