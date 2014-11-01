__author__ = 'sid'
# https://projecteuler.net/problem=9
# More info on triplets: http://www.mathsisfun.com/numbers/pythagorean-triples.html


def special_pythagorean_triplet():
    # a = n^2 - m^2
    # b = 2nm
    # c = n^2 + m^2
    for i in range(1, 50):
        m = i
        n = i + 1
        a = (n * n) - (m * m)
        b = 2 * n * m
        c = (n * n) + (m * m)
        print a, b, c
        if a + b + c == 1000:
            print a * b * c
            break

if __name__ == "__main__":
    special_pythagorean_triplet()