def find_cut_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    for seq in [dna_sequence, enzyme_sequence]:
        for char in seq:
            if char not in valid_nucleotides:
                return "Error: Sequence contains invalid nucleotides"
    
    cut_positions = []
    enzyme_len = len(enzyme_sequence)
    for i in range(len(dna_sequence) - enzyme_len + 1):
        if dna_sequence[i:i+enzyme_len] == enzyme_sequence:
            cut_positions.append(i + 1)  
    return cut_positions

# example
print(find_cut_sites("GATCGAT", "GAT"))  # output [1, 5]