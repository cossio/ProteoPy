#!/usr/bin/env python


import argparse
import scipy.stats


PARSER = argparse.ArgumentParser(description='Detect differences, t-tes',
                                 fromfile_prefix_chars='@')
PARSER.add_argument('--data', type=str,
					help='data file')
PARSER.add_argument('--colname', type=int,
					help='column number of names')
PARSER.add_argument('--cols1', type=int, nargs='+',
                    help='replicas of 1st population, column indexes')
PARSER.add_argument('--cols2', type=int, nargs='+',
                    help='replicas of 2nd population, column indexes')
PARSER.add_argument('--header', type=int,
					help='header lines to skip', default=1)
PARSER.add_argument('--delim', type=str, default='\t',
					help='delimiter between columns')
ARGS = PARSER.parse_args()


with open(ARGS.data) as file:
	for i, line in enumerate(file):
		if i < ARGS.header:
			continue

		words = line.split('\t')

		x1 = [float(words[c]) for c in ARGS.cols1]
		x2 = [float(words[c]) for c in ARGS.cols2]

		t,p = scipy.stats.ttest_ind(x1,x2)

		if p < 0.05:
			print words[ARGS.colname]
