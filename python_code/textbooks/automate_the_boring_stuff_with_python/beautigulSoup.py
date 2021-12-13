import bs4

examplefile = open('example.html')
exampleSoup = bs4.BeautifulSoup(examplefile.read())
elems = exampleSoup.select('#author')

# print(type(elems))
# print(type(elems[0]))
# print(elems[0].getText())
# print(str(elems[0]))
# print(elems[0].attrs)


pelems = exampleSoup.select('p')
print(str(pelems[0]))
print(pelems[0].getText())
print(pelems[1].getText())
print(pelems[2].getText())
print()

# print((len(elems))
