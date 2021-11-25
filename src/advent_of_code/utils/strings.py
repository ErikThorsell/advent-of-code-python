def hamming_distance(string1, string2):
    return sum(c1 != c2 for c1, c2 in zip(string1, string2))
