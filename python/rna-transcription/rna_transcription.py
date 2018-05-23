def to_rna(dna_strand):
    output = []
    for c in dna_strand:
        if c == "G":
            output.append("C")
        elif c == "C":
            output.append("G")
        elif c == "T":
            output.append("A")
        elif c == "A":
            output.append("U")
        else:
            raise ValueError("bad format")
    return "".join(output)
