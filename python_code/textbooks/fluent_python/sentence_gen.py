import re, reprlib

RE_WORD = re.compile('\w+')

class Sentence:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__(self):
		return 'Sentence(%s)' %reprlib.repr(self.text)
	def __iter__(self):
		for w in self.words:
			yield word 
		return 


class Sentence2:
	def __init__(self, text):
		self.text = text

	def __repr__(self):
		return 'Sentence(%s)' %reprlib.repr(self.text)
	def __iter__(self):
		for match in RE_WORD.finditer(self.text):
			yield match.group()