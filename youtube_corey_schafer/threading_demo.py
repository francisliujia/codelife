import threading
import time


start = time.perf_counter()

# def do_something(seconds):
# 	print(f'sleeping {seconds} second...')
# 	time.sleep(seconds)
# 	print('done sleeping...')

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# do_something()
# do_something()

# threads = []
# for _ in range(10):
# 	t = threading.Thread(target=do_something, args=[1.5])
# 	t.start()
# 	threads.append(t)


# for thread in threads:
# 	thread.join()

# finish = time.perf_counter()
# print(f'finished in {round(finish-start, 2)} second(s)')

import requests

img_urls = [
		'https://unsplash.com/photos/rRyr4meFomc',
		'https://unsplash.com/photos/UChNjL5Zpk4',
		'https://unsplash.com/photos/MHlVX-n91yI'

]

t1 = time.perf_counter()
for img_url in img_urls:
	img_bytes = requests.get(img_url).content
	img_name = img_url.split('/')[4]
	img_name = f'{img_name}.jpg'
	with open(img_name, 'wb') as img_file:
		img_file.write(img_bytes)
		print(f'{img_name} was downloaded...')

t2 = time.perf_counter()
print(f'finished in {t2-t1} seconds')










