#!/usr/bin/env python

"""
Get basic information from Uniprot (mass and/or sequence length) from a list of gene symbols.
"""

import sys
import argparse
import ProteoPy


PARSER = argparse.ArgumentParser(
    description='Get gene names')
PARSER.add_argument('genes', type=str, help='list of genes', nargs='+')
ARGS = PARSER.parse_args()

SERV = ProteoPy.Services()


def printgenename(g):
    try:
        print(g + '\t' + SERV.genename(gene))
    except KeyboardInterrupt:
        raise
    except:
        ProteoPy.util.printwarn('No name found for ' + g)


for gene in ARGS.genes:
    if ';' in gene:
        for g in gene.split(';'):
            printgenename(g)
    else:
        printgenename(gene)
