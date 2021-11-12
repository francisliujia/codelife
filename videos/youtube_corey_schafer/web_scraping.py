from bs4 import BeautifulSoup
import requests

with open('simple.html', 'r') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

# print(soup)
print(soup.prettify())
print("\n")
# match = soup.title
# print(match)

# match = soup.title.text
# print(match)

# match = soup.div
# print(match)

# use a undersocre '_' before class to avoid the conflict with the class
# match = soup.find('div', class_='footer')
# print(match)


# returns only the first match of the arguments
article = soup.find('div', class_='article')
# print(article)

# return all the matches of the arguments
# article = soup.find_all('div', class_='article')
# print(article)


# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)


# //////////////// 2 ///////////////


# return all the matches of the arguments
for article in soup.find_all('div', class_='article'):
# print(article)

	headline = article.h2.a.text
	print(headline)

	summary = article.p.text
	print(summary)

	print()







