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
    for line in proteome_file:
        words = line.split()
        print words
        samples = len(words) - 1  # first column is protein names
        sample_names = words[1:]
        break

print 'Number of samples is ' + str(samples)


# load weights if passed
if args.weights:
    weights = ProteoPy.io.read_weights(args.weights)
    print 'Weights loaded'


# read compartments
compartment_names, compartment_proteins = ProteoPy.io.read_compartments(args.compartments)


# initialize fractions
psi = [[0.] * samples] * (1 + len(compartment_names))


with open(args.proteome) as proteome_file:
    for line in proteome_file:
        words = line.split()
        if len(words) == samples:
            words.insert(0, 'MissingName')
        assert len(words) == samples + 1
        
        protein = words[0]
        if args.weights and protein not in weights:
            continue

        i = ProteoPy.util.compartmentidx(protein, compartment_proteins)
        
        for s in range(samples):
            x = float(words[s + 1])
            if args.weights:
                x *= weights[protein]
            if i:
                psi[i][s] += x
            else:
                psi[-1][s] += x

# normalize
for s in range(samples):
    N = sum(psi[i][s] for i in range(len(psi)))
    for i in range(len([psi])):
        psi[i][s] /= N


with open(args.out, 'w') as out_file:
    # write sample names
    ProteoPy.io.write_list_tsv(out_file, sample_names)
    
    for i in range(len(psi)):
        if i < len(compartment_names):
            out_file.write(compartment_names[i])
        else:
            out_file.write('other')
        ProteoPy.io.write_list_tsv(out_file, psi[i])

