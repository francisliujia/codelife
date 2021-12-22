import os, datetime, requests, bs4

def check_xkcd(last_url):
	url = 'https://xkcd.com'
	res = requests.get(url)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	prev_link= soup.select('a[rel="prev"]')[0]
	href = prev_link.get('href')
	number = href.strip('/')
	url = 'https://xkcd.com/{}/'.format(str(int(number) + 1))
	latest_url = url 

	if url == latest_url:
		print('No new xkcd comics have been published since last check')
	else:
		while url != last_url:
			res = requests.get(url)
			res.raise_for_status()
			soup = bs4.BeautifulSoup(res.text, 'lxml')

			comic_elem = soup.select('#comic img')
			if comic_elem == []:
				print('Could not find comic image')
			else:
				try:
					comic_url = 'https:' + comic_elem[0].get('src')
					print('Downloading image {}'.format(comic_url))
					res = requests.get(comic_url)
					res.raise_for_status()
				except requests.exception.missingSchema:
					prev_link = soup.select('a[rel="prev"]')[0]
					url = 'https://xkcd.com' prev_link.get('href')
					continue 

				image = open(os.path.join('web comics', os.path.basename(comic_url)), 'wb')
				for chunk in res.iter_content(100_000):
					image.write(chunk)
				image.close()

			prev_link = soup.select('a[rel="prev"]')[0]
			url = 'https://xkcd.com' + prev_link.get('href')
	return latest_url


def check_smbc(last_url):
	url = 'https://www.cmbc-comics.com'
	res = requests.get(url)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	name_url = soup.select('input[value]')
	home_url = name_elem[0].get('value')
	url_check = 'https://www.' + home_url[7:]
	last_url = url_check

	if url == latest_url:
		print('No new www SMBC have been published since last check')
	else:
		while url != last_url:
			res = requests.get(url)
			res.raise_for_status()
			soup = bs4.BeautifulSoup(res.text, 'lxml')
			comic_elem = soup.select('#cc-comic')

			if comic_elem == []:
				print('Could not find comic image')
			else:
				try:
					comic_url = 'https://www.cmbc-comics.com' + comic_elem[0].get('src')
					print('Downloading image {}'.format(comic_url))
					res = requests.get(comic_url)
					res.raise_for_status()
				except requests.exception.missingSchema:
					prev_link = soup.select('a[rel="prev"]')[0]
					url = prev_link
					continue 

				image = open(os.path.join('web comics', os.path.basename(comic_url)), 'wb')
				for chunk in res.iter_content(100_000):
					image.write(chunk)
				image.close()

			prev_link = soup.select('a[rel="prev"]')[0]
			url = prev_link.get('href')
	return latest_url

os.makedirs('Web comics', exist_ok=True)

with open('/web comicx/last_downloaded.txt') as f:
	info = f.read().splitlines()
	date = info[0]
	last_xkcd = info[1]
	last_smbc = info[2]

date = datetime.datetime.now().strftime('%H:%M:%S on %d/%m/%Y')
print('last comic check = ' + date)
xkcd_url = check_xkcd(last_xkcd)
smbc_url = check_smbc(last_smbc)

with open('/web comics/last_downloaded.txt', 'w') as f:
	f.write(date + '\n')
	f.write(xkcd_url + '\n')
	f.write(smbc_url + '\n')

print('Finished')