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


if len(seq) < 30:
    print("too short")
elif "N" in seq:
    print("contain unknown bases")
elif seq.startswith("ATG") and len(seq) % 3 == 0:
    print("possible ORF")