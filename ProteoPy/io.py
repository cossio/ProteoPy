"""
I/O functions
"""

import os


def read_weights(path):
    """
    Reads a file of protein weights
    """
    weights = {}
    with open(path) as weights_file:
        for line in weights_file:
            words = line.split()
            assert len(words) == 2
            weights[words[0]] = float(words[1])
    return weights


def read_compartment(path):
    """
    Reads a compartment file
    """
    proteins = set()
    with open(path) as compartment_file:
        for line in compartment_file:
            proteins.add(line.rstrip())
    return proteins


def read_compartments(path):
    """
    Reads list of compartment names and compartment proteins
    """
    compartment_proteins = []
    compartment_names = []

    with open(path) as compartment_file:
        for line in compartment_file:
            p = line.rstrip()
            c = os.path.basename(p)

            compartment_proteins.append(read_compartment(p))
            compartment_names.append(c)

    return compartment_names, compartment_proteins


def write_list_tsv(out, l):
    """
    Write a list separated by tabs, with new line at the end
    """

    for i, v in enumerate(l):
        if i < len(l) - 1:
            out.write(str(v) + '\t')
        else:
            out.write(str(v) + '\n')
