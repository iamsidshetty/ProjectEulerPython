__author__ = 'sid'


#  prime number using seive_of_eratosthenes
# n log log n
def seive_of_eratosthenes(N):
    not_prime = [False] * (N + 1)
    primes = []

    for i in range(2, (N + 1)):
        if not_prime[i]:
            continue
        for f in xrange(i * 2, (N + 1), i):
            not_prime[f] = True

        primes.append(i)

    return primes


# prime factors
def prime_factors(a):
    if a == 0: return [0]
    if a == 1: return [1]
    b = 2
    c = [2] # all prime numbers
    while a != 1:
        if a % b == 0:
            a /= b
            c.append(b)
            b = 2
        else:
            b += 1

    return set(c)


