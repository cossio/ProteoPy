#!/usr/bin/env python

"""
Get basic information from Uniprot (mass and/or sequence length) from a list of gene symbols.
"""

import sys
import argparse
import ProteoPy
import ColorPrintPy as COL  # https://github.com/cossio/ColorPrintPy


PARSER = argparse.ArgumentParser(
    description='Get basic information from Uniprot from a list of gene names')
PARSER.add_argument('--genes', type=str, help='list of genes')
PARSER.add_argument('--out', type=str, help='output file')
PARSER.add_argument('--uniprot', action='store_true', help='uniprot ID')
PARSER.add_argument('--mass', action='store_true', help='molar mass')
PARSER.add_argument('--length', action='store_true', help='sequence length')
ARGS = PARSER.parse_args()

SERV = ProteoPy.Services()


with open(args.genes) as genes_file, open(args.out, 'w', 1) as out_file:

    # column headers
    out_file.write('gene')
    if args.uniprot:
        out_file.write('\tuniprot')
    if args.mass:
        out_file.write('\tmass')
    if args.length:
        out_file.write('\tlength')
    out_file.write('\n')

    for (lno, gene_names) in enumerate(genes_file):
        if lno == 0: # skip first line
            continue

        for gene in gene_names.split(';'):
            gene = gene.rstrip()

            try:
                uniprotid = serv.uniprot_id(gene)
            except KeyboardInterrupt:
                raise
            except:
                print COL.colstr(COL.WARNING, 'error retrieving uniprot id of ' + gene)
                continue

            if args.mass or args.length:
                try:
                    mass, length = serv.uniprot_data(uniprotid)
                except KeyboardInterrupt:
                    raise
                except:
                    print COL.colstr(COL.WARNING, 'error retrieving mass or length of ' + gene)
                    raise

            out_file.write(gene)
            if args.uniprot:
                out_file.write('\t' + uniprotid)
            if args.mass:
                out_file.write('\t' + str(mass))
            if args.length:
                out_file.write('\t' + str(length))
            out_file.write('\n')
