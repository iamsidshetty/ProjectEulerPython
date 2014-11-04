__author__ = 'sid'
# https://projecteuler.net/problem=14
# make use of memoization

def longest_collatz_sequence(n):
    seq_len = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            seq_len += 1
        else:
            n = (3 * n) + 1
            seq_len += 1
    return seq_len


if __name__ == "__main__":
    count = 0
    number = 0
    for i in range(1000000, 0, -1):
        seq = longest_collatz_sequence(i)
        if seq > count:
            count = seq
            number = i

    print number, count

