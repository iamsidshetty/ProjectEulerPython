__author__ = 'sid'
# https://projecteuler.net/problem=22

from EulerUtils import *


def names_scores(names_list):
    # get the letter: number mapping
    alpha = alphabet_number()
    result = 0
    for position, name in enumerate(names_list):
        letter_sum = 0
        for letter in name:
            letter_sum += alpha[letter.lower()]
        result += (position + 1) * letter_sum

    return result


if __name__ == "__main__":
    for lines in open("p022_names.txt", "r").readlines():
        names = ([x[1:-1] for x in lines.split(",")])

    print names_scores(sorted(names))
