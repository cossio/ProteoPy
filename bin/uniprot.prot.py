#!/usr/bin/env python


import argparse
import ProteoPy
import sys


parser = argparse.ArgumentParser(description='Get basic information from Uniprot from a list of Uniprot IDs')
parser.add_argument('--prots', type=str, help='list of proteins')
parser.add_argument('--out', type=str, help='output file')
parser.add_argument('--mass', action='store_true', help='molar mass')
parser.add_argument('--length', action='store_true', help='sequence length')
args = parser.parse_args()


serv = ProteoPy.Services()


with open(args.prots) as prots_file, open(args.out, 'w', 1) as out_file:
    
    # column headers
    out_file.write('UniprotID')
    if args.mass: out_file.write('\tmass')
    if args.length: out_file.write('\tlength')
    out_file.write('\n')

    for (lno, names) in enumerate(prots_file):
        if lno == 0: # skip first line
            continue

        for pid in names.split(';'):
            pid = pid.rstrip()
            if args.mass or args.length:
                try:
                    mass, length = serv.uniprot_data(pid)
                except KeyboardInterrupt:
                    raise
                except:
                    print 'error retrieving mass or length of ' + pid + ' ... skipping'
                    continue

            out_file.write(pid)
            if args.mass:
                out_file.write('\t' + str(mass))
            if args.length:
                out_file.write('\t' + str(length))
            out_file.write('\n')
            
