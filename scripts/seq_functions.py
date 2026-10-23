sequences = ["AAAGCTATGCAGCTACCGTTGGTGCACTCTTCTTCGACGCGGCTATC",
 "ATATATATGATCGCGCGGCGAATTAGCGNNNC",
"AAATTTCCCGGGAAAATTTCCCGGGAAATTTGGGCCC"]
def gc_content(seq):
    count_c = seq.count("C")
    count_g = seq.count("G")
    count_gc = count_c + count_g
    gc_percent = count_gc/len(seq) * 100
    return round(gc_percent, 2)

for seq in sequences:
    print(gc_content(seq))

def reverse_complement(seq):
    reverse_seq = seq[::-1]
    return reverse_seq.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()

for seq in sequences:
    print(reverse_complement(seq))

def is_usable(seq, min_length=30):
    if len(seq) >= min_length and "N" not in seq:
        return True
    else:
        return False

for seq in sequences:
    print(is_usable(seq))


def first_atg(seq):
    atg = seq.find("ATG")
    if atg >= 0:
        return(atg)
    else:
        return -1

for seq in sequences:
    print(first_atg(seq))