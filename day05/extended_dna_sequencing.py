import sys
import re

# Background:
# nucleotides = A, C, T, G
# string_example = "ACCGXXTXXYYGTTQRACQQTGGGCXTTGTXX"
# input_sequence = sys.argv[1]
input_DNA_string = input("Please type in a sequence:")


dna = re.split(r'[^ACGT]+', input_DNA_string)
filtered_dna = list(filter(None, dna))
sorted_dne = sorted(filtered_dna, key=len, reverse=True)
print(sorted_dne)