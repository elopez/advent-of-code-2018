#!/usr/bin/env python3
from itertools import cycle

with open("in.txt") as infile:
    nums = map(int, infile.readlines())

    seen = {0}
    state = 0

    for num in cycle(nums):
        state += num

        if state in seen:
            print(state)
            break

        seen.add(state)
