#!/usr/bin/env python

'''
Calculate compartment proteomic fractions from proteomics data.
'''

import os
import argparse
import ProteoPy


PARSER = argparse.ArgumentParser(description='Calculate proteome fractions',
                                 fromfile_prefix_chars='@')
PARSER.add_argument('--compartments_by_gene', type=str,
                    help='list of compartment definitions, by gene symbols')
PARSER.add_argument('--compartments_by_prot', type=str,
                    help='list of compartment definitions, by uniprot IDs')
PARSER.add_argument('--proteome', type=str,
                    help='proteome file. Columns: uniprot ids, gene symbols, samples')
PARSER.add_argument('--weights_by_gene', type=str, help='molecular weights')
PARSER.add_argument('--weights_by_prot', type=str, help='molecular weights')
PARSER.add_argument('--out', type=str)
ARGS = PARSER.parse_args()


"""
Proteins are given in abundances.
"""


# read sample names
with open(ARGS.proteome.strip()) as proteome_file:
    for line in proteome_file:
        words = line.split('\t')
        samples = len(words) - 2  # first columns are protein and gene names
        sample_names = [s.strip() for s in words[2:]]
        break


# load weights
gene_weights = ProteoPy.io.read_weights(ARGS.weights_by_gene.strip())
prot_weights = ProteoPy.io.read_weights(ARGS.weights_by_prot.strip())

# read compartments
compartments_by_gene_names, compartments_by_gene_proteins = ProteoPy.io.read_compartments(ARGS.compartments_by_gene.strip())
compartments_by_prot_names, compartments_by_prot_proteins = ProteoPy.io.read_compartments(ARGS.compartments_by_prot.strip())
compartment_names = set(compartments_by_gene_names).union(compartments_by_prot_names)
compartment_names.add('Other')

# initialize fractions
psi = {c: [0. for s in range(samples)] for c in compartment_names}


with open(ARGS.proteome.strip()) as proteome_file:
    for lineidx, line in enumerate(proteome_file):

        if lineidx == 0: # skip header line
            continue

        words = line.split('\t')
        if len(words) != samples + 2:
            ProteoPy.util.printwarn('Bad line in ' + ARGS.proteome + ' line number ' + str(lineidx) + ' ... skipping')
            continue
        assert len(words) == samples + 2

        '''
        Compartments can be defined by gene symbols or Uniprot IDs (in that priority order).
        This gives us some robustness.
        '''

        protids = words[0]
        geneids = words[1]
        i_by_gene = ProteoPy.util.compartmentidx(geneids, compartments_by_gene_proteins)
        i_by_prot = ProteoPy.util.compartmentidx(protids, compartments_by_prot_proteins)
        if i_by_gene != None:
            c = compartments_by_gene_names[i_by_gene]
        elif i_by_prot != None:
            c = compartments_by_prot_names[i_by_prot]
        else:
            c = 'Other'

        weight_by_gene = ProteoPy.util.getweight(geneids, gene_weights)
        weight_by_prot = ProteoPy.util.getweight(protids, prot_weights)
        if weight_by_gene != None:
            weight = weight_by_gene
        elif weight_by_prot != None:
            weight = weight_by_prot
        else:
            ProteoPy.util.printwarn('Gene ' + geneids + ' (protein ' + protids + ') has no weight... ignoring')
            continue
        
        if geneids == 'SHMT2':
            ProteoPy.util.printinfo(geneids + ', compartment=' + c + ', weight=' + str(weight))

        for s in range(samples):
            psi[c][s] += float(words[s + 2]) * weight

# sanity check
assert len(compartment_names) == len(psi)
for c in compartment_names:
    assert len(psi[c]) == samples


# normalize
for s in range(samples):
    N = sum(psi[c][s] for c in compartment_names)
    for c in compartment_names:
        psi[c][s] = psi[c][s] / N


with open(ARGS.out.strip(), 'w') as out_file:
    # write sample names
    out_file.write('compartment\t')
    ProteoPy.io.write_list_tsv(out_file, sample_names)

    for i, c in enumerate(compartment_names):
        out_file.write(c + '\t')
        ProteoPy.io.write_list_tsv(out_file, psi[c])
