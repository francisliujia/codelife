class CompressedGene:
	def __init__(self, gene):
		self._compress(gene)

	def _compress(self, gene):
		self.bit_string = 1  
		for nucleotide in gene.upper():
			self.bit_string <<=2 # shift left two bits 
			if nucleotide == 'A':
				self.bit_string |= 0b00
			elif nucleotide == 'C':
				self.bit_string |= 0b01
			elif nucleotide == 'G':
				self.bit_string |= 0b10
			elif nucleotide == 'T':
				self.bit_string |= 0b11
			else:
				raise ValueError('invalid nucleotide:{}'.format(nucleotide))
		print(bin(self.bit_string))


	def decompress(self):
		gene = ''
		for i in range(0, self.bit_string.bit_length() - 1, 2):
			bits = self.bit_string >> i & 0b11
			if bits == 0b00:
				gene += "A"
			elif bits == 0b01:
				gene  += 'C'
			elif bits == 0b10:
				gene  += 'G'
			elif bits == 0b11:
				gene  += 'T'
			else:
				raise ValueError('Invalid bits:{}'.format(bits))
		return gene[::-1] #reversing the string by slicing backwards

	def __str__(self):
		return self.decompress()

from sys import getsizeof
orignal = 'ATCGTGCAATCGTGCAATCGTGCAATCGTGCAATCGTGCAATCGTGCAATCGTGCA' * 100
print('orignal is {} bytes'.format(getsizeof(orignal)))

compressed = CompressedGene(orignal)
print('compressed is {} bytes'.format(getsizeof(compressed)))
print('orignal and decompressed are the same: {}'.format(orignal == compressed.decompress()))
