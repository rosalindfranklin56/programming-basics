sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]

# 1. Print each sequence with its length

for i in sequences:
    print(i, len(i))

# 2. Build a list of lengths, then print the average

lengths = []

for i in sequences:
    lengths.append(len(i))

print(lengths)
print(sum(lengths)/len(lengths))

# 3. Count how many sequences start with ATG

count = 0

for i in sequences:
    if i.startswith("ATG"):
        count = count + 1
        
print(count)

# 4. Print only the sequences longer than 5 bases

for i in sequences:
    if len(i) > 5:
        print(i)


# 5. For each sequence print its GC content (loop inside a loop!)
 
for i in sequences:
    count = 0
    for base in i:
        if base == "G" or base == "C":
            count = count + 1
    print(count/len(i)*100)


# Bonus: print the codons of the longest sequence, one per line

codon_length = 3

for i in sequences:
    if i == max(sequences, key = len):
        for base in range (0, len(i), codon_length):
            codon = i[base: base + codon_length]
            if len(codon) == codon_length:
                print(codon)