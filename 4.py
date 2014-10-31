__author__ = 'sid'
# https://projecteuler.net/problem=4


from EulerUtils import *


def largest_palindrome_product():
    largest = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if is_palindrome(i * j):
                if (i * j) > largest:
                    largest = i * j
    print largest

if __name__ == "__main__":
    largest_palindrome_product()