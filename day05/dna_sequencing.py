import sys

# Background:
# nucleotides = A, C, T, G
# string_example = "ACCGXXCXXGTTACTGGGCXTTGTXX"

input_sequence = sys.argv[1]


dna = input_sequence.split("X")
filtered_dna = list(filter(None, dna))
sorted_dne = sorted(filtered_dna, key=len, reverse=True)
d = print(filtered_dna)
print(sorted_dne)