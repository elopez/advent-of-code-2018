#!/usr/bin/env python3
from collections import Counter

with open("in.txt") as ids:
    appears_twice = 0
    appears_thrice = 0

    for id in ids:
        frequencies = Counter(id).values()
        if 2 in frequencies:
            appears_twice += 1
        if 3 in frequencies:
            appears_thrice += 1

    print(appears_twice * appears_thrice)
