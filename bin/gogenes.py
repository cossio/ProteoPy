#!/usr/bin/env python

import argparse
import ProteoPy

parser = argparse.ArgumentParser(description='List of genes with a GO annotation')
parser.add_argument('go', type=str, help='GO terms', nargs='+')
args = parser.parse_args()

serv = ProteoPy.Services()

for go in args.go:
    for g in serv.gogenes(go):
        print(g)