import os, requests, bs4 

def image_downloader(extension):
	url = 'https://imgur.com/search?q=' + search
	os.makedirs('/Users/ji-axinliu/Downloads/imgur', exist_ok=True)

	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	image_elem = soup.select('.post> .image-list-link img')

	for i, image in enumerate(image_elem):
		image_url_s = 'https:' + image_elem[i].get('src')
		image_url = image_url_s[: -5] + '.' + extension

		print('Downloading image {}'.format(image_url))
		res = requests.get(image_url)
		res.raise_for_status()
		image_file = open(os.path.join('/Users/ji-axinliu/Downloads/imgur',
			os.path.basename(image_url)),'wb')
		for chunk in res.iter_content(100_000):
			image_file.write(chunk)
		image_file.close()
	return len(image_elem)

search = input("Enter desired search terms: ")
downloaded = image_downloader('jpg') + image_downloader('png')

if downloaded == 0:
	print('No image found.')
else:
	print('All ' + str(downloaded) + 'files successfully downloaded.')