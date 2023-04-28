#!/usr/bin/env python3
import sys
import os
import pandas as pd
from pyfaidx import Fasta

termini = sys.argv[1] #a code for the genome such as AcerAcer or Bmori
genome_name = sys.argv[2] #in ../genomes - may be able to combine species and genome file into one arguement - same with b_result. Idealy there would be one input. - Not likely with bombyx being the search term.

b_result = "../b_results/" + genome_name + ".out"
genome = Fasta("../genomes/" + genome_name + ".fna")
flank=1000


def partial(no_match):
	print("There wasn't enough to match the C and N termini. Change your termini sequences.")
	#os. remove(b_result)
	dif_termini = open(no_match, "a")
	dif_termini.write(sys.argv[2] + "\n")
	dif_termini.close()
	exit()

def check_flank(caps):
	if caps.get('first') < -1:
		caps['first'] = 0
	contig_length = len(genome[caps.get('contig')])
	if caps.get('last') > contig_length:
		caps['last'] = contig_length
	print(caps)

def write_file(caps):
	if caps.get('correct_ori') == True:
		print("N to C = Negative")
		output = open("../genes/" + genome_name + "_gene.fa", "w")
		gene = genome[caps.get('contig')][int(caps.get('first')):int(caps.get('last'))]
		output.write(">" + genome_name + "_heavy_chain_fibroin\n" + str(gene))
		output.close()
		print("Gene extracted")
		'''
		found = "found_alt_phegnom.txt"
		gene = open(found, "a")
		gene.write(sys.argv[2] + "\n")
		gene.close()
		'''
	elif caps.get('correct_ori') == False:
		print("C to N = positive")
		output = open("../genes/" + genome_name + "_gene.fa", "w")
		gene = reverse_complement(genome[caps.get('contig')][int(caps.get('first')):int(caps.get('last'))])
		output.write(">"+ genome_name + "_heavy_chain_fibroin\n" + str(gene))
		output.close()
		print("Gene extracted")
		'''
		found = "found_alt_phegnom.txt"
		gene = open(found, "a")
		gene.write(sys.argv[2] + "\n")
		gene.close()
		'''
	
def gene_ext(b_reult, termini, flank):	#The df is made out of the ouput file of the blast run.
	no_match = "no_match.txt"
	
	df = pd.read_csv(b_result, sep="\t", header=None, names = ["query acc.ver", "subject acc.ver", "% identity", "alignment length", "mismatches", "gap opens", "q. start", "q. end", "s. start", "s. end", "evalue", "bit score"])
	#print(df)
	df = df.loc[(df["query acc.ver"]== termini + "_c_terminus") | (df["query acc.ver"]== termini + "_n_terminus")]
	print(df)
	if ((len(df) < 2) or df.empty):
		partial(no_match)
	df = df.sort_values(by=["subject acc.ver", "% identity"], ascending=(False, False))
	df = df.loc[df['subject acc.ver'].duplicated(keep = False)]
	#print(df)
	if ((len(df) < 2) or df.empty):
		print(df)
		partial(no_match)
	df = df.sort_values(by=["% identity", "subject acc.ver"], ascending=(False, False))	
	df = df.drop_duplicates(subset = ["query acc.ver"], keep='first')
	
	if ((len(df) == 0) or df.empty):
		print(df)
		partial(no_match)
	print(df)
	#These if statements  determines the position of the N and C termini and retruns the start and end bp position. It also determines if we need the reverse of the string in order for the it to be in the correct 
	df = df.sort_values(by=["query acc.ver"]) #This ensures that the C terminus will always be first [0, "s.start"]
	df.set_axis([0, 1], axis=0, inplace=True)
	
	if (len(df) != 2):
		print(df)
		partial(no_match)
	elif ((df.at[0, "subject acc.ver"]) != (df.at[1, "subject acc.ver"])):
		print(df)
		partial(no_match)
	#print(df)	
	
	contig = df.at[0, "subject acc.ver"]
	
	if bool(df.loc[0, "s. start"] < df.loc[1, "s. start"]): #C terminus is before N terminus. The orientation is reversed.
		if bool(df.loc[0, "s. end"] < df.loc[0, "s. start"] < df.loc[1, "s. end"] < df.loc[1, "s. start"]): #C terminus is before N terminus - negative strand
			start = int(df.at[0, "s. start"]) - flank
			end = int(df.at[1, "s. end"]) + flank	
			caps = {'first':start, 'last':end, 'contig':contig,"correct_ori":False}
		else:
			print(df)
			print("The orientation was wrong.")
			#os.remove(b_result)
			dif_termini = open(no_match, "a")
			dif_termini.write(sys.argv[2] + "\n")
			dif_termini.close()
			exit()
	elif bool(df.loc[0, "s. start"] > df.loc[1, "s. start"]): #the N terminus is before the C terminus - correction orientation
		if bool(df.loc[1, "s. start"] < df.loc[1, "s. end"] < df.loc[0, "s. start"] < df.loc[0, "s. end"]): #C terminus is before N terminus - negative strand
			start = int(df.at[1, "s. start"]) - flank #This should be pulling the N terminus and storing it in start
			end = int(df.at[0, "s. end"]) + flank
			caps = {'first':start, 'last':end, 'contig':contig, "correct_ori":True}
		else:
			print(df)
			print("The orientation was wrong.")
			#os.remove(b_result)
			dif_termini = open(no_match, "a")
			dif_termini.write(sys.argv[2] + "\n")
			dif_termini.close()
			exit()	
	else:
		print("something went terribly wrong")
	return(caps)
def reverse_complement(seq):
	new_seq = ""
	complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N', 'n':'n', 'a':'t', 't':'a', 'c':'g', 'g':'c'}
	for nuc in seq:
		new_seq = new_seq + str(complement.get(str(nuc)))
	return new_seq[::-1]

if (not os.path.isfile(b_result)):
	print("No blast result file")
	exit()

caps = gene_ext(b_result, termini, flank)

check_flank(caps)

write_file(caps)

