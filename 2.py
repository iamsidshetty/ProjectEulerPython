__author__ = 'sid'
# https://projecteuler.net/problem=2

# Fib = 0 1 1 2 3 5 8 13 21 34 .....
# Problem Fib = 1 2 3 5 8 13 21 34 .....

# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n - 1) + fib(n - 2)


def fib_prob(val):
    even_sum = 2
    n_1 = 1
    n_2 = 2
    num = 0
    while num < val:
        num = n_1 + n_2
        if num % 2 == 0:
            even_sum += num

        n_1 = n_2
        n_2 = num
    return even_sum

if __name__ == "__main__":
    print fib_prob(4000000)