"""
I/O functions
"""

import os
from . import util


def read_weights(path):
    """
    Reads a file of protein weights
    """
    weights = {}
    with open(path) as weights_file:
        for lineidx, line in enumerate(weights_file):
            words = line.split()
            assert len(words) == 2
            try:
                weights[words[0]] = float(words[1])
            except ValueError:
                util.printwarn("Invalid weight in " + path + ", line number " + str(lineidx) + ' ... skipping')
                continue
    return weights


def read_compartment(path):
    """
    Reads a compartment file
    """
    elements = set()
    with open(path) as compartment_file:
        for line in compartment_file:
            elements.add(line.rstrip())
    return elements


def read_compartments(path):
    """
    Reads list of compartment names and compartment proteins
    """
    compartment_elements = []
    compartment_names = []

    with open(path) as compartment_file:
        for line in compartment_file:
            words = line.split('\t')
            name, path = words
            compartment_elements.append(read_compartment(path.rstrip()))
            compartment_names.append(name)

    return compartment_names, compartment_elements


def write_list_tsv(out, collection):
    """
    Write a list separated by tabs, with new line at the end
    """

    for i, value in enumerate(collection):
        if i < len(collection) - 1:
            out.write(str(value) + '\t')
        else:
            out.write(str(value) + '\n')
