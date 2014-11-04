__author__ = 'sid'
# https://projecteuler.net/problem=25


def n_digit_fibonacci_number(n):
    n_1 = 0           # first fibonacci number
    n_2 = 1           # second fibonacci number
    count = 0
    while True:
        count += 1
        num = n_1 + n_2
        if len(str(num)) == n:
            break
        n_1 = n_2
        n_2 = num

    return count + 1


if __name__ == "__main__":
    print n_digit_fibonacci_number(1000)
