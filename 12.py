__author__ = 'sid'
# https://projecteuler.net/problem=12

# modified the code of prime factors
def number_of_factors(a):
    if a == 0:
        return 0
    if a == 1:
        return 1

    b = 2
    c = {}  # all prime numbers
    while a != 1:
        if a % b == 0:
            a /= b
            if b in c:
                c[b] += 1
            else:
                c[b] = 1
            b = 2
        else:
            b += 1

    div = 1
    for key, value in c.iteritems():
        div *= value + 1

    return div


def highly_divisible_triangular_number():
    tri_num = 0
    for i in range(1, 1000000):
        tri_num += i
        if number_of_factors(tri_num) >= 500:
            print tri_num
            break


if __name__ == "__main__":
    highly_divisible_triangular_number()