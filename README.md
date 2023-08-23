# H-Fib_Lepidoptera

This project identifies the heavy chain fibroin gene in newly sequenced Lepidoptera genomes where annotation of the genome has not yet been completed. This gene has heavily repetitive regions making it difficult to find through pure blast alone.

The code found in this repo requires a Conda environment wherein Blast, Pyfaidx, and Pandas are available.

## Pipeline:
1. Select the gene of interest and extract the termini regions from a gene already annotated. Put this file in the termini directory following the format and naming system within that directory. In future examples, the termini file will be AntCard.fasta.

2. Generate a code for the selected species. For example, the species Acentria ephemerella would generate the code of AceEphe.

3. Download the genome of the related species into the directory genomes and rename the file to the {code}.fna i.e. AceEphe.fna.

4. Enter the conda environment and ensure all the packages are loaded (Blast, Pyfaidx, and Panda).

5.  Run 'sh blash.sh AceEphe AntCard' which will generate the database and blast the termini against the genome. These files will be stored in the directory b_results.

7. Run 'python3 gene_ext.py AceEphe AntCard' to check the blast file and see if there are any viable gene candidates. If there are, the file will be saved as AceEphe.fa in the genes directory. The flanks of the extracted regions can be adjusted within [gene_ext.py]

8. Run 'sh annotation AceEphe' for a preliminary annotation. The gff file will be saved in the annotation directory. It is best to check these annotations manually as heavy chain fibroin has proven difficult for many annotation softwares.
