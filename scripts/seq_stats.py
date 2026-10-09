sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)
print(len(sequences))
print(sequences[0],sequences[-1], sep="\n")
sequences.append("ATATATGC")
print(sequences)
print(len(sequences[0]))
sequences_lengths = [len(sequences[0]), len(sequences[1]), len(sequences[2]), len(sequences[3]), len(sequences[4])]
print(sequences_lengths)
print(max(sequences_lengths))
print(min(sequences_lengths))
average = sum(sequences_lengths)/len(sequences_lengths)
name, chrom, start, stop = gene
print(f"{name} is on {chrom} and is {stop-start} bases long")
# gene[0] = "BRCA2" # TypeError: 'tuple' object does not support item assignment
genes = [("BRCA1", 81188), ("TP53", 25759)]
print(genes[1][1])