#!/usr/bin/env python3
import sys
import os
import pandas as pd

directory = '../b_results'

for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isfile(f):
		df = pd.read_csv(f, sep="\t", header=None, names = ["query acc.ver", "subject acc.ver", "% identity", "alignment length", "mismatches", "gap opens", "q. start", "q. end", "s. start", "s. end", "evalue", "bit score"]) 
		print(f)
		print(df['% identity'])
