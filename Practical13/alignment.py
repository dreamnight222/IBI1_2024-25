# read the fasta files
def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        seq = ''.join([line.strip() for line in lines[1:]])
        # Using join to concatenate sequences has a time complexity of O(n), which is better than using a for loop to add elements one by one with a time complexity of O(n²) (learned from AI)
    return lines[0].strip(), seq  

# read the blosum matrix
def read_blosum(file_path):
    blosum = {}
    with open(file_path, 'r') as f:
        headers = f.readline().split()
        for line in f:
            row = line.split()
            aa = row[0]
            blosum[aa] = {}  
            for i, h in enumerate(headers):# get the index positions and corresponding values of the headers elements through enumerate (learned from AI)
                value = int(row[i+1])  # get the values starting from the second row, as the first row is the header
                blosum[aa][h] = value  # add the value to the dictionary
        return blosum

# comparison calculation
def align(seq1, seq2, blosum):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length")
    score = 0
    identity = 0
    for i in range(len(seq1)):
        a = seq1[i]
        b = seq2[i]
        score += blosum[a][b]
        if a == b:
            identity += 1
    percent_identity = (identity / len(seq1)) * 100
    return score, percent_identity

# main program section

# read the data
human_header, human_seq = read_fasta("human.fasta")
mouse_header, mouse_seq = read_fasta("mouse.fasta")
random_header, random_seq = read_fasta("random.fasta")
blosum = read_blosum("BLOSUM62.txt")

# pairwise comparison
pairs = [("Human-Mouse", human_seq, mouse_seq),("Human-Random", human_seq, random_seq),("Mouse-Random", mouse_seq, random_seq)]

for name, s1, s2 in pairs:
    score, identity = align(s1, s2, blosum)
    print(f"{name}_comparison outcome：")
    print(f"BLOSUM62 score：{score}")
    print(f"identical percentage：{identity:.2f}%\n")