# import necessary libraries
import re

# define the sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# match every intron that start with GT and end uo with AG
introns = re.findall(r'GT.*?AG', seq)

# calculate the max length of the longest intron
max_intron_length = max([len(intron) for intron in introns]) if introns else 0

print(f"The length of the largest intron is: {max_intron_length}")