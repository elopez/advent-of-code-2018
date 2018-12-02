#!/usr/bin/env python3
import sys
from collections import Counter

# length of each ID
ID_LEN = 26

with open("in.txt") as ids:
    seen = [set() for _ in range(ID_LEN)]

    for id in ids:
        for l in range(ID_LEN):
            shorter_id = id[:l] + id[l+1:]
            if shorter_id in seen[l]:
                print(shorter_id)
                sys.exit()
            seen[l].add(shorter_id)
