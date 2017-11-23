#!/usr/bin/env python

"""
Script to get the list of aliases of a gene symbol (or list of gene symbols).
"""

import argparse
import ProteoPy

PARSER = argparse.ArgumentParser(description='List of proteins with a GO annotation')
PARSER.add_argument('gene', type=str, help='gene symbol', nargs='+')
ARGS = PARSER.parse_args()

SERV = ProteoPy.Services()

for gene in ARGS.gene:
    try:
        prots = SERV.genealias(gene)
    except:
        print bcolors.WARNING + 'ERROR: ' + gene + bcolors.ENDC
        continue

    for p in prots:
        print p
