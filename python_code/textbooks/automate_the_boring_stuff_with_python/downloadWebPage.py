import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()

# print(type(res))
# print(res.status_code == requests.codes.ok)

# print(len(res.text))
# print(res.text[:250])


newFile = open('romeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100_000):
	newFile.write(chunk)

newFile.close()