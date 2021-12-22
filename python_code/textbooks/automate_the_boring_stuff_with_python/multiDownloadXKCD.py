import requests, os, bs4, threding

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    print("Downloading from page: https://xkcd.com/%s..." %(urlNumber))
    res = requests.get('https://xkcd.com/%s' %(urlNumber))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("not image can be found.")
    else:
        comicUrl = comicElem[0].get('src')
        print('Downloading image %s ...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        imagefile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100_000):
            imagefile.write(chunk)
        imagefile.close()

download_threads = []
for i in range(0, 1400, 100):
    download_thread = threadingThread(target=downloadXkcd, args=(i, i+99))
    download_threads.append(download_thread)
    download_thread.start()

for download_thread in download_threads:
    download_thread.join()
print('Done')
