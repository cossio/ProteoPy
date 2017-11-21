#!/usr/bin/env python

import ProteoPy
import argparse

parser = argparse.ArgumentParser(description='Calculate proteome fractions')
parser.add_argument('--compartments', type=str, help='list of compartment definitions')
parser.add_argument('--proteome', type=str, help='proteome file')
parser.add_argument('--columns', type=int, nargs='+', help='sample columns')
parser.add_argument('--header', type=int, help='number of header lines')
parser.add_argument('--weights', type=str, help='optional, molecular weights of proteins')
parser.add_argument('--out', type=str)
args = parser.parse_args()


"""
Proteins are given in abundances.
"""


def read_compartment_file(path):
    compartments = {}
    with open(path) as compartment_file:
        for line in compartment_file:
            assert len(line.split())
    return compartments


with open(args.compartments) as compartments_list:
    for compartment in compartments_list:
        with open(compartment) as compartment_file:

        
        assert compartment not in compartments
        compartments[compartment] = []
       
            for line in compartment_file:
                assert len(line.split()) == 1
                compartments[compartment].append(line.rstrip())


phi = {}



# determine number of cell lines
for line in args.proteome:
    words = line.split()
    for col in args[columns]:
        p = float(words[col])



UNIP = bioservices.UniProt();
KEGG = bioservices.KEGG();
glycolysis_kegg = [s.split('\t')[-1] for s in KEGG.link('hsa', 'hsa00010').split('\n')];
fatty_acid_kegg = [s.split('\t')[-1] for s in KEGG.link('hsa', 'hsa00061').split('\n')];
pentose_ph_kegg = [s.split('\t')[-1] for s in KEGG.link('hsa', 'hsa00030').split('\n')];



