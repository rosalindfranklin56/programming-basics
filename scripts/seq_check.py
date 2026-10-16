#1. If it is shorter than 30 bases → "too short"
#2. If it contains an N → "contains unknown bases"
#3. If its GC content is above 60% → "GC rich", below 40% → "AT rich", otherwise "balanced"

seq = "ATGAAATTTAAAATTTGCGTGCGTGTTGCGCGTAAAATGCCTAGATGC"

C = seq.count("C")
G = seq.count("G")
GC = G + C
gc = GC/len(seq)*100

if len(seq) < 30:
    print("too short")
elif "N" in seq:
    print("contain unknown bases")
elif gc > 60:
    print("GC rich")
elif gc < 40:
    print("AT rich")
else:
    print("balanced")

# 4. If it starts with ATG and its length divides by 3 (len(seq) % 3 == 0) → "possible ORF"
 
if len(seq) < 30:
    print("too short")
elif "N" in seq:
    print("contain unknown bases")
elif seq.startswith("ATG") and len(seq) % 3 == 0:
    print("possible ORF")