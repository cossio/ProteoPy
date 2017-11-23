#!/usr/bin/env python

import argparse

PARSER = argparse.ArgumentParser(description='Detect fold-changes in two vectors',
                                 fromfile_prefix_chars='@')
PARSER.add_argument('--x1', type=str, help='vector 1')
PARSER.add_argument('--x2', type=str, help='vector 2')
PARSER.add_argument('--names', type=str, help='names')
PARSER.add_argument('--thresh', type=float, help='fold-change threshold')
PARSER.add_argument('--out', type=str)
ARGS = PARSER.parse_args()


def read_list(path, eltype):
    vec = []
    with open(path) as file:
        for line in file:
            vec.append(eltype(line))
    return vec


X1 = read_list(ARGS.x1, float)
X2 = read_list(ARGS.x2, float)
names = read_list(ARGS.names, str)


assert len(X1) == len(X2) == len(names)


for x1, x2, name in zip(X1, X2, names):
    if x2 / x1 > ARGS.thresh:
        print name.strip()
