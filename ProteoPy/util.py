"""
Miscelanous utility functions
"""

import os
import sys


def compartmentidx(protein, compartment_proteins):
    "Get the compartment of a protein"
    for i, s in enumerate(compartment_proteins):
        if protein in s:
            return i
    else:
        return None
