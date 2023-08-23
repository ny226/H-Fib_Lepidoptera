# H-Fib_Lepidoptera

This project identifies the heavy chain fibroin gene in newly sequenced Lepidoptera genomes where annotation of the genome has not yet been completed. This gene has heavily repetitive regions making it difficult to find through pure blast alone.

The code found in this repo requires a Conda environment wherein Blast, Pyfaidx, and Pandas are available.

# Pipeline:
1.      Select the gene of interest and extract the termini regions from a gene already annotated. For example, bombyx.fa

2.      Generate a code for the selected species. For example, the species Acentria ephemerella would generate the code of AceEphe

3.      Download the genome of the related species into the directory genomes and rename the file to the [code].fna i.e. AceEphe.fna

4.      Run 'sh blash.sh AceEphe ' which will generate the database and blast the termini against the genome. These files will be stored in the directory b_results

5.      Run ' ' to check the blast file and see if there are any viable gene candidates. If there are, the file will be saved to as AceEphe.fa in the genes directory. The flanks of the extracted regions can be adjusted within gene_ext.py

6.      Run sh ausgustus for a preliminary annotation. It is best to check these annotations manually as heavy chain fibroin has proven difficult for many annotation softwares
