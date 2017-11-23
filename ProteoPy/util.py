"""
Miscelanous utility functions
"""

import os
import sys
from termcolor import cprint, colored


def compartmentidx(element, compartment_elements):
    "Get the compartment of an element"
    for i, s in enumerate(compartment_elements):
        for e in element.split(';'):
            if e in s:
                return i
    else:
        return None


def getweight(protein, weights):
    "Get the weight of a protein"
    
    proteins = protein.split(';')
    for p in proteins:
        if p in weights:
            return weights[p]
    else:
        return None


def flatten(container):
    for x in container:
        if isinstance(x, (list,tuple)):
            for y in flatten(x):
                yield y
        else:
            yield x


def printwarn(text):
    '''
    Prints in the warning style
    '''

    cprint(text, 'yellow', 'on_blue', attrs=['bold'])


def printinfo(text):
    '''
    Prints in the info style
    '''

    cprint(text, 'blue', attrs=['bold'])
