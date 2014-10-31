__author__ = 'sid'
# https://projecteuler.net/problem=3

from EulerUtils import *


def largest_prime_factor(N):
    print max(prime_factors(N))

if __name__ == "__main__":
    largest_prime_factor(600851475143)