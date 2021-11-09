glossary = {
    'string': 'a series of characters.',
    'list': 'a collections of items in a particular order.',
    'dictionary': 'a collection of key-value pairs.',
    'loop': 'work through a collection, once at a time.',
    'comment': 'a note in a program that Python interpreter ignores.',
}

for word, definition in glossary.items():
    print(word.title() + ": " + definition + "\n")

'''
print(f"\nString: \n\t{glossary['string']}")
print(f"\nList: \n\t{glossary['list']}")
print(f"\nDictionary: \n\t{glossary['dictionary']}")
print(f"\nLoop: \n\t{glossary['loop']}")
print(f"\ncomment: \n\t{glossary['comment']}")

word = 'string'
print(word.title() + ": \n\t" + glossary[word])
word = 'list'
print(word.title() + ": \n\t" + glossary[word])
word = 'dictionary'
print(word.title() + ": \n\t" + glossary[word])
word = 'loop'
print(word.title() + ": \n\t" + glossary[word])
word = 'comment'
print(word.title() + ": \n\t" + glossary[word])
'''
