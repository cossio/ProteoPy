#!/usr/bin/env python

import argparse
import scipy.stats
import numpy
import ProteoPy


PARSER = argparse.ArgumentParser(description='Detect differences, t-tes',
                                 fromfile_prefix_chars='@')
PARSER.add_argument('--data', type=str, required=True,
                    help='data file')
PARSER.add_argument('--colname', type=int, required=True,
                    help='column number of names')
PARSER.add_argument('--groups', type=str, required=True,
                    help='file containing lists of columns for each group. Each line is a group (cols indices), beginning with group name')
PARSER.add_argument('--header', type=int,
                    help='header lines to skip', default=1)
PARSER.add_argument('--delim', type=str, default='\t',
                    help='delimiter between columns')
PARSER.add_argument('--fold', type=float, default=0.5,
                    help='fold-change threshold')
PARSER.add_argument('--out', type=str, help='out prefix')
ARGS = PARSER.parse_args()


groups = []
groupnames = []

with open(ARGS.groups) as gr:
    for i, line in enumerate(gr):
        words = line.split()
        groupnames.append(words[0])
        groups.append([int(w) for w in words[1:]])

# sanity check
for g in groups:
    for i in g:
        assert i >= 0


for g1, group1 in enumerate(groups):
    for g2, group2 in enumerate(groups):
        if g1 != g2:

            name = groupnames[g1] + '_vs_' + groupnames[g2]

            diff = {}

            with open(ARGS.data) as dat:

                for i, line in enumerate(dat):

                    words = line.split('\t')

                    if i < ARGS.header:
                        headers1 = [words[c - 1].strip() for c in groups[g1]]
                        headers2 = [words[c - 1].strip() for c in groups[g2]]
                        ProteoPy.util.printinfo('Header line, cols1 = ' + ' '.join(headers1) + '; cols2 = ' + ' '.join(headers2))
                        continue

                    x1 = [float(words[c - 1]) for c in groups[g1]]
                    x2 = [float(words[c - 1]) for c in groups[g2]]

                    t, p = scipy.stats.ttest_ind(x1, x2)

                    if p < 0.05:
                        m1 = scipy.mean(x1)
                        m2 = scipy.mean(x2)
                        assert m1 != m2
                        gene = words[ARGS.colname - 1]
                        diff[gene] = numpy.float64(m1)/m2

                    # if p < 0.05 and m1 != m2:
                    #     if m2 == 0 or m2 != 0 and m1/m2 < ARGS.fold:
                    #         gene = words[ARGS.colname - 1]
                    #         diff[gene] = m1/m2
                    #         out.write(gene + '\n')
            
            with open(ARGS.out + name + '.out', 'w') as out:
                for k,v in sorted(diff.iteritems(), key=lambda (k,v): (v,k)):
                    out.write(k + '\t' + str(v) + '\n')