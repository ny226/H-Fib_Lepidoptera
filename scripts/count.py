#!/usr/bin/env python3

import sys
import numpy

verify=sys.argv[1] # + ".fa"


def findStopCodons(orf):
    catch = numpy.arange(0, len(orf), 3)
    startCodonPositions = []
    stopCodonPositions = []
    for i in catch:
        codon = orf[i:i + 3]
        if codon == 'ATG':
            startCodonPositions.append(i + 1)
        if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
            stopCodonPositions.append(i + 1)
    return stopCodonPositions

f=open(verify, "r")
stopCodons= len(findStopCodons(f.readline()))
print(stopCodons)
f.close()
