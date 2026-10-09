dna_1 = "AUGAATCCGGTTCCCGGCCCTTTAAATCGGGCCTACGTTGCTAACGTAATAA"
print(len(dna_1))
n = len(dna_1)
print(dna_1.count("G"))
g = dna_1.count("G")
print(dna_1.count("C"))
c = dna_1.count("C")
gc = (g+c)/n
print("GC:", gc, "%")