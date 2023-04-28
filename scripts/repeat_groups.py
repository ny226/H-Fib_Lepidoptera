#!/usr/bin/env python3

import sys

gene = sys.argv[1]
with open(output_file) as out_file:
    for Nu in gene:
        print(Nu)

#Outline of fuzzy search:

#Step 1: Define empty group
#Step 2: For the first nucleotide, put it in the first group

#Finding ASVs:
#Find unique groups with k = 1
#Find unique groups with k = 2
#Find unique groups up to length of contig, name group according to k number
#Do a loop within a loop (one loop iterating from 1 to the genome size, inside loops creating unique groups for each k)


#Finding repeat clusters:
#Take groups with the largest k and find % similarity
#Map these groups on the gene / get the positions of nucleotides on the gene
#Assign all nucleotides where the group maps to to a certain color
#Assign all nucleotides not included with a different color
#Make a graph with showing the colors of nucleotides
#Repeat with different k numbers to show smaller repeat sections

#Compare genes to different species' genes

