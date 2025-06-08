import sys
from collections import Counter

filepath = "C:\\Inbal\\University\\Chemistry Msc Weizmann\\Courses\\Python Course\\day07\\DNA Sequence.txt"

codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}



with open(filepath, 'r') as file:
    plain_text = file.read().upper()
    plain_text = plain_text.replace("\n", "")
    codons_sep = [(plain_text[i:i+3]) for i in range(0, len(plain_text), 3)]


reverse_codon_table = {codon: aa for aa, codons in codon_table.items() for codon in codons}



amino_list = []
for codon in codons_sep:
    if len(codon) < 3:
        continue
    amino_list.append(reverse_codon_table[codon])
amino_count = Counter(amino_list)


for word, counts in amino_count.items():
    print(f"{word}: {counts}")