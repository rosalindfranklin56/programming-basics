# Sequence statistics
# 1. How many sequences are in the list? Print the first and the last one

sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
print(len(sequences))
print(sequences[0],sequences[-1], sep="\n")

# 2. Add one more sequence of your own
sequences.append("ATATATGC")
print(sequences)

# 3. Make a list of their lengths (by hand is fine — 5 values)
sequences_lengths = [len(sequences[0]), len(sequences[1]), len(sequences[2]), len(sequences[3]), len(sequences[4])]
print(sequences_lengths)

# 4. Print the longest, shortest and average length 
print(max(sequences_lengths))
print(min(sequences_lengths))
average = sum(sequences_lengths)/len(sequences_lengths)

# 5. Unpack the tuple gene into name, chrom, start, stop
gene = ("BRCA1", "chr17", 43044295, 43125483)
name, chrom, start, stop = gene

# 6. Print: BRCA1 is on chr17 and is ... bases long (use an f-string)
print(f"{name} is on {chrom} and is {stop-start} bases long")

# 7. Try to change the gene name in the tuple — copy the error into a comment
gene[0] = "BRCA2" # TypeError: 'tuple' object does not support item assignment

# Bonus: a list of tuples! genes = [("BRCA1", 81188), ("TP53", 25759)] — print the length of TP53
genes = [("BRCA1", 81188), ("TP53", 25759)]
print(genes[1][1])