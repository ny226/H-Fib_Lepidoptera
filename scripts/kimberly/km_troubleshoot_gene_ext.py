#!/usr/bin/env python3
import sys
import os
import pandas as pd
from pyfaidx import Fasta

termini = sys.argv[1] #a code for the genome such as AcerAcer or Bmori
genome_name = sys.argv[2] #in ../genomes - may be able to combine species and genome file into one arguement - same with b_result. Idealy there would be one input. - Not likely with bombyx being the search term.

b_result = "../b_results/" + genome_name + ".out"
genome = Fasta("../genomes/" + genome_name + ".fna")
flank=50



def blast_to_df(b_result, termini, flank):	#The df is made out of the ouput file of the blast run.
	no_match = "no_match.txt"
	
	df = pd.read_csv(b_result, sep="\t", header=None, names = ["query acc.ver", "subject acc.ver", "% identity", "alignment length", "mismatches", "gap opens", "q. start", "q. end", "s. start", "s. end", "evalue", "bit score"])
	df = df.loc[(df["query acc.ver"]== termini + "_c_terminus") | (df["query acc.ver"]== termini + "_n_terminus")]
	print(df)
	if (len(df) == 0):
		print("There wasn't enough to match the C and N termini. Change your termini sequences. Blast file was deleted.")
		#os. remove(b_result)
		dif_termini = open(no_match, "a")
		dif_termini.write(sys.argv[2] + "\n")
		dif_termini.close()
		exit()
	if (len(df) == 0):
		print("There wasn't enough to match the C and N termini. Change your termini sequences. Blast file was deleted.")
		#os. remove(b_result)
		dif_termini = open(no_match, "a")
		dif_termini.write(sys.argv[2] + "\n")
		dif_termini.close()
		exit()
	df = df.sort_values(by=["subject acc.ver", "% identity"], ascending=(False, False))
	print("this is the sorted data frame 1")
	print(df)
	best = df.iloc[0,1]
	print("the best contig is " + best)
	df = df.loc[df['subject acc.ver'].duplicated(keep = False)]
	print("this is the dataframe after deleting duplicates")
	print(df)
	if (len(df) == 0):
		print("There wasn't enough to match the C and N termini. Change your termini sequences. Blast file was deleted.")
		#os. remove(b_result)
		dif_termini = open(no_match, "a")
		dif_termini.write(sys.argv[2] + "\n")
		dif_termini.close()
		exit()
#	for line in df:
#		print(line)
#THIS IS NEW CODE TO FILTER FOR SUBJECTS WITH BOTH N AND C TERMINI
	print("This is the beginning of the NEW CODE!")
	print("This is the dataframe we're working with:")
	print(df)
#	for n in df["subject acc.ver"]:
#               print("these are the n values:")
#               print(n)
	n_list = df["subject acc.ver"].unique()
	print("These are the n list values:")
	print(n_list)
	for n in n_list:
		cond_ = (df["subject acc.ver"] == n)
		for row in df.iterrows():
			r = df.loc[cond_,:]
			#print(r["query acc.ver"]) 
			#print(r["query acc.ver"].nunique())
			if r["query acc.ver"].nunique() == 2:
				if r["subject acc.ver"].nunique() == 1:
					df = r
					#print("The unique subject acc.ver is:")
					#print(r["subject acc.ver"].nunique())
					#print("this should have n and c")
					#print(r)
					#print("this is the end of the loop")
	print("This is the moment of truth...")
	print(df)
#	for n in n_list:
#		print(df.loc[df['query acc.ver'] == n])
#THIS IS THE CODE FOR THE OPTIMAL PAIR BUT DOESN'T WORK
	#df = df.loc[df['subject acc.ver'] == best]
	#print("this should work")
	#print(df)
	#df = df.sort_values(by=["% identity", "subject acc.ver"], ascending=(False, False))
	#print("this is the sorted df 2")
	#print(df)
#THIS IS CODE THAT WAS TAKEN OUT 
	df = df.drop_duplicates(subset = ["query acc.ver"], keep='first')
	print("this is the drop_duplicates df")
	print(df)
	if (len(df) == 0):
		print("There wasn't enough to match the C and N termini. Change your termini sequences")
		#os. remove(b_result)
		dif_termini = open(no_match, "a")
		dif_termini.write(sys.argv[2] + "\n")
		dif_termini.close()
		exit()
	print("this is the dataframe with an error")
	print(df)
	#These if statements  determines the position of the N and C termini and retruns the start and end bp position. It also determines if we need the reverse of the string in order for the it to be in the correct 
	df = df.sort_values(by=["query acc.ver"]) #This ensures that the C terminus will always be first [0, "s.start"]
	df.set_axis([0, 1], axis=0, inplace=True)
	
	print(df)
	
	if len(df) != 2:
		print(df)	
		print("There wasn't enough to match the C and N termini or there were too many. Change your termini sequences. Blast file was deleted.")
		#os. remove(b_result)
		dif_termini = open(no_match, "a")
		dif_termini.write(sys.argv[2] + "\n")
		dif_termini.close()
		exit()
	
	elif ((df.at[0, "subject acc.ver"]) != (df.at[1, "subject acc.ver"])):
		print(df)
		print("The contigs didn't match up. Blast file was deleted")
		#os.remove(b_result)
		dif_termini = open(no_match, "a")
		dif_termini.write(sys.argv[2] + "\n")
		dif_termini.close()
		exit()
	print(df)	
	
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

caps = blast_to_df(b_result, termini, flank)


if caps.get('first') < 0:
    caps['first'] = 0
contig_length = len(genome[caps.get('contig')])

if caps.get('last') > contig_length:
    caps['last'] = contig_length

print(caps)

if caps.get('correct_ori') == True:
	print("N to C = Negative")
	output = open("../genes/" + genome_name + "_gene.fa", "w")
	gene = genome[caps.get('contig')][int(caps.get('first')):int(caps.get('last'))]
	output.write(">" + genome_name + "_heavy_chain_fibroin\n" + str(gene))
	output.close()

	print("Gene extracted")

elif caps.get('correct_ori') == False:
	print("C to N = positive")
	output = open("../genes/" + genome_name + "_gene.fa", "w")
	gene = reverse_complement(genome[caps.get('contig')][int(caps.get('first')):int(caps.get('last'))])
	output.write(">"+ genome_name + "_heavy_chain_fibroin\n" + str(gene))
	output.close()
	print("Gene extracted")
'''
	found = "gene.txt"
	gene = open(found, "a")
	gene.write(sys.argv[2] + "\n")
	gene.close()
'''
