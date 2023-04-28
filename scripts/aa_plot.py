import matplotlib.pyplot as plt
import sys
import csv



protein_file = sys.argv[1]
genome=protein_file[:7]
print(genome)

x_axis = []
y_axis = []

with open(protein_file, "r")as protein:
	tsv_reader = csv.reader(protein, delimiter=" ")
	for row in tsv_reader:
		while("" in row):
			 row.remove("")
		#print(row)
		(count, amino) = row
		#print(f"amino {amino} count: {count}")
		x_axis.append(amino)
		y_axis.append(count)


plt.bar(x_axis, y_axis)
plt.title('AbrTrip Amino Acid Composition')
plt.xlabel('amino acid')
plt.ylabel('number in protein')
plt.savefig(genome+ ".png")
