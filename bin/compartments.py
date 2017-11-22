#!/usr/bin/env python

import ProteoPy
import argparse
import os


parser = argparse.ArgumentParser(description='Calculate proteome fractions')
parser.add_argument('--compartments', type=str, help='list of compartment definitions')
parser.add_argument('--proteome', type=str, help='proteome file. First column contains protein names')
parser.add_argument('--weights', type=str, help='optional, molecular weights of proteins')
parser.add_argument('--out', type=str)
args = parser.parse_args()


"""
Proteins are given in abundances.
"""


# determine number of samples
with open(args.proteome) as proteome_file:
    for line in args.proteome:
        words = line.split()
        samples = length(words) - 1  # first column is protein names
        sample_names = words[1:]
        break


# load weights if passed
if args.weights:
    weights = ProteoPy.io.read_weights(args.weights)


# read compartments
compartment_names, compartment_proteins = ProteoPy.io.read_compartments(args.compartments)

# initialize fractions
psi = [[0.] * samples] * len(compartment_names)


with open(args.proteome) as proteome_file:
    for line in args.proteome:
        words = line.split()
        assert len(words) == samples + 1
        protein = words[0]
        
        i = ProteoPy.util.compartmentidx(protein, compartment_proteins)

        for s in range(samples):
            psi[i][s] += float(words[s + 1])


with open(args.out, 'w') as out_file:
    # write sample names
    ProteoPy.io.write_list_tsv(out_file, sample_names)
    
    for i in range(len(compartment_names)):
        out_file.write(compartment_names[i])
        ProteoPy.io.write_list_tsv(out_file, psi[i])

