#!/usr/bin/env python

import argparse
import gseapy
import ProteoPy


PARSER = argparse.ArgumentParser(description='Gene enrichment analysis',
                                 fromfile_prefix_chars='@')
PARSER.add_argument('--genes', type=str, nargs='+', help='gene list')
ARGS = PARSER.parse_args()



for gene in ARGS.genes