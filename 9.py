__author__ = 'sid'
# https://projecteuler.net/problem=9
# More info on triplets: http://www.mathsisfun.com/numbers/pythagorean-triples.html


def special_pythagorean_triplet():
    for c in xrange(2, 1000):
        for a in xrange(1, c):
            b = 1000 - a - c

            if a ** 2 + b ** 2 == c ** 2 and a < b < c:
                    print a * b * c


# Does not generate all the triplets
def special_pythagorean_triplet_euler():
    # a = n^2 - m^2
    # b = 2nm
    # c = n^2 + m^2
    for i in range(1, 50):
        m = i
        n = i + 1
        a = (n * n) - (m * m)
        b = 2 * n * m
        c = (n * n) + (m * m)
        if a + b + c == 1000 and a < b < c:
            print a * b * c


def special_pythagorean_triplet_brute_force():
    for c in xrange(1, 1000):
        for b in xrange(1, c):
            for a in range(1, b):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    print a * b * c


def special_pythagorean_triplet_brute_force_alternate():
    for a in xrange(1, 335):
        for b in xrange(1, 667):
            c = 1000 - b - a
            if a ** 2 + b ** 2 == c ** 2 and a < b < c:
                print a * b * c


if __name__ == "__main__":
    special_pythagorean_triplet()