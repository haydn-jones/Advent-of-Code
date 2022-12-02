from itertools import groupby

def read_strip(path):
    with open(path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def groupify(lines, key):
    chunks = list(list(g) for k,g in groupby(lines, key=lambda x: x != key) if k)
    return chunks