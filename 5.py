__author__ = 'sid'
# https://projecteuler.net/problem=5


from EulerUtils import *
import math

# Brute Force
# i = 20
# while i % 2 != 0 or i % 3 != 0 or i % 4 != 0 or i % 5 != 0 or i % 6 != 0 or i % 7 != 0 or i % 8 != 0 or i % 9 != 0 or
# i %10 != 0 or i %11 != 0 or i %12 != 0 or i %13 != 0 or i %14 != 0 or i %15 != 0 or i %16 != 0 or i %17 != 0
# or i %18 != 0 or i %19 != 0 or i %20 != 0:
# i += 20
#
# print i


def smallest_multiple(N):
    primes = seive_of_eratosthenes(N)
    result = 1

    for i in primes:
        powers = math.floor(math.log(N, 10) / math.log(i, 10))
        result *= math.pow(i, powers)

    print int(result)

if __name__ == "__main__":
    smallest_multiple(20)



