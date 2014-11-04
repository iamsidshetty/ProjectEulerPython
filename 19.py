__author__ = 'sid'
# https://projecteuler.net/problem=19

from collections import OrderedDict


def counting_sundays(start_year, end_year):
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

    month_days = OrderedDict(
        [("January", 31),
         ("February", 28),
         ("March", 31),
         ("April", 30),
         ("May", 31),
         ("June", 30),
         ("July", 31),
         ("August", 31),
         ("September", 30),
         ("October", 31),
         ("November", 30),
         ("December", 31)])

    month_days_leap_year = OrderedDict(
        [("January", 31),
         ("February", 29),
         ("March", 31),
         ("April", 30),
         ("May", 31),
         ("June", 30),
         ("July", 31),
         ("August", 31),
         ("September", 30),
         ("October", 31),
         ("November", 30),
         ("December", 31)])

    day = 1                    # starting day
    count = 0                  # to get the count of Sundays
    for i in range(start_year, end_year):
        if i % 4 == 0 or i % 400 == 0:
            year = month_days_leap_year
        else:
            year = month_days
        for month, no_of_days in year.iteritems():
            extra_days = no_of_days % 7
            day = (day + extra_days) % 7

            if days[day] == "Sun":
                count += 1

    print count


if __name__ == "__main__":
    counting_sundays(1901, 2001)
