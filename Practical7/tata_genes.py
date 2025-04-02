# import necessary libraries
import re

# define a function to check if the sequence has tataboxes
def has_tata_box(sequence):
    return bool(re.search(r'TATA[AT][AT]', sequence))

# read the input file and output a new file
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'tata_genes.fa'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    current_seq = ''
    current_name = ''
    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            # save the previous sequence
            if current_seq and has_tata_box(current_seq): # check whether the current_seq is not empty and the sequence have the TATA box
                gene_name = line.split()[0][1:].split('_')[0]  # get the gene name，remove '>' and '_mRNA'
                outfile.write(f'>{gene_name}\n{current_seq}\n') # write the information in the outfile
            current_name = line
            current_seq = ''
        else:
            current_seq += line# go for next line
    # process the last sequence just like those above
    if current_seq and has_tata_box(current_seq):
        gene_name = current_name.split()[0][1:]
        outfile.write(f'>{gene_name}\n{current_seq}\n')

print("TATA box genes have been written to tata_genes.fa")