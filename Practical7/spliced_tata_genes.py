# spliced_tata_genes.py
import re

# define a function to count the number of TATA boxes
def has_tata_box(sequence):
    return len(re.findall(r'TATA[AT][AT]', sequence))  

def is_spliced(sequence, splice_combo):
    return bool(re.search(splice_combo, sequence))

# get input from user
splice_combo = input("Enter splice donor/acceptor combination (GTAG, GCAG, or ATAC): ")

output_file = f"{splice_combo}_spliced_genes.fa"

# read the input file and process it
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    current_seq = ''
    current_name = ''
    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            if current_seq:
                if is_spliced(current_seq, splice_combo):
                    tata_count = has_tata_box(current_seq)
                    if tata_count > 0:
                        gene_name = line.split()[0][1:].split('_')[0] 
                        output_line = '>' + gene_name + '_TATA' + str(tata_count) + '\n' + current_seq.replace('\n', '') + '\n'
                        outfile.write(output_line)
            current_name = line
            current_seq = ''
        else:
            current_seq += line
    # process the last sequence
    if current_seq:
        if is_spliced(current_seq, splice_combo):
            tata_count = has_tata_box(current_seq)
            if tata_count > 0:
                gene_name = current_name.split()[0][1:].split('_')[0]
                output_line = '>' + gene_name + '_TATA' + str(tata_count) + '\n' + current_seq.replace('\n', '') + '\n'
                outfile.write(output_line)

print(f"Spliced genes with TATA boxes have been written to {output_file}")