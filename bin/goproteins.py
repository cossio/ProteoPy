#!/usr/bin/env python

"""
Script to get the list of proteins (Uniprot IDs) belonging to a GO annotation.
"""

import argparse
import ProteoPy

PARSER = argparse.ArgumentParser(description='List of proteins with a GO annotation')
PARSER.add_argument('go', type=str, help='GO terms', nargs='+')
ARGS = parser.parse_args()

SERV = ProteoPy.Services()

for go in ARGS.go:
    try:
        prots = SERV.goproteins(go)
    except:
        print go
        raise

    for p in prots:
        print p
