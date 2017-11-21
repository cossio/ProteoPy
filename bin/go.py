#!/usr/bin/env python


import argparse
import ProteoPy

parser = argparse.ArgumentParser(description='List of genes with a GO annotation')
parser.add_argument('--GO', type=str, help='list of genes')
args = parser.parse_args()

serv = ProteoPy.Services()
proteins = serv.gogenes('GO:' + args.GO)

for p in prots:
    print p
