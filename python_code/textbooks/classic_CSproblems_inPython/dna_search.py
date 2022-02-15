from enum import IntEnum
from typing import Tuple, List

Nucleotide = IntEnum('Nucleotide', ['A', 'C', 'G', 'T'])
Condon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Condon]

def string_to_gene(s):
	gene = []
	for i in range(0, len(s), 3):
		if (i+2) >= len(s):
			return gene 
		condon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
		gene.append(condon)
	return gene

# my_gene = string_to_gene(gene_str)
# pring(my_gene)

def linear_contains(gene, key_coden):
	for codon in gen:
		if codon == key_coden:
			return True
		return False

def binary_contains(gene, key_coden):
	low = 0 
	high = len(gene) - 1 
	while low <= high:
		mid = (low + high) // 2
		if gene[mid] < key_coden:
			low = mid + 1 
		elif gene[mid] > key_coden:
			high = mid - 1
		else:
			return True
	return False