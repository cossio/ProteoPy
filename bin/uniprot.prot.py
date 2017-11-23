#!/usr/bin/env python


import sys
import argparse
import ProteoPy


PARSER = argparse.ArgumentParser(description='Get basic information from Uniprot from a list of Uniprot IDs')
PARSER.add_argument('--prots', type=str, help='list of proteins')
PARSER.add_argument('--out', type=str, help='output file')
PARSER.add_argument('--mass', action='store_true', help='molar mass')
PARSER.add_argument('--length', action='store_true', help='sequence length')
ARGS = PARSER.parse_args()


SERV = ProteoPy.Services()


with open(ARGS.prots) as prots_file, open(ARGS.out, 'w', 1) as out_file:

    # column headers
    out_file.write('UniprotID')
    if ARGS.mass:
        out_file.write('\tmass')
    if ARGS.length:
        out_file.write('\tlength')
    out_file.write('\n')

    for (lno, names) in enumerate(prots_file):
        if lno == 0: # skip first line
            continue

        for pid in names.split(';'):
            pid = pid.rstrip()
            if ARGS.mass or ARGS.length:
                try:
                    mass, length = SERV.uniprot_data(pid)
                except KeyboardInterrupt:
                    raise
                except:
                    ProteoPy.util.printwarn('error retrieving mass or length of ' + pid + ' ... skipping')
                    continue

            out_file.write(pid)
            if ARGS.mass:
                out_file.write('\t' + str(mass))
            if ARGS.length:
                out_file.write('\t' + str(length))
            out_file.write('\n')
            
