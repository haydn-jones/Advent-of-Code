import numpy as np
import sys

from itertools import groupby

with open(f"{sys.path[0]}/input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    lines = [int(l) if l != "" else "" for l in lines]

chunks = list(list(g) for k,g in groupby(lines, key=lambda x: x != '') if k)
chunks = [sum(c) for c in chunks]
chunks = sum(sorted(chunks)[-3:])