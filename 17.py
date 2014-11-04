__author__ = 'sid'
# https://projecteuler.net/problem=17


def number_letter_counts():
    first9 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ten = "ten"
    first11_19 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    multiplesof10 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    extra = "hundredand"
    thousand = "onethousand"

    count1_9 = 0
    for i in first9:
        count1_9 += len(i)

    count11_19 = 0
    for j in first11_19:
        count11_19 += len(j)

    count1_99 = count1_9 + len(ten) + count11_19
    for k in multiplesof10:
        count1_99 += len(k)
        count1_99 += len(k) * 9 + count1_9

    count1_999 = count1_99
    for l in first9:
        count1_999 += len(l) + len("hundred")
        count1_999 += ((len(l) + len(extra)) * 99) + count1_99

    print count1_999 + len(thousand)


if __name__ == "__main__":
    number_letter_counts()
