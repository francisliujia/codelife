import time 
from PIL import Image, ImageFilter
import os 
import concurrent.futures

image_names = [
	'download1.jpeg',
	'download2.jpeg',
	'download3.jpeg',
]

image_folder = r'/Users/ji-axinliu/Downloads/test_folder'

t1 = time.perf_counter()
size = (1200, 1200)

# =========== use a for loop=======
# for image_name in image_names:
# 	img = Image.open(os.path.join(image_folder, image_name))

# 	img = img.filter(ImageFilter.GaussianBlur(15))

# 	img.thumbnail(size)
# 	img.save(f'{image_folder}/processed/{image_name}')
# 	print(f'{image_name} was processed...')


# use a function and mutiple processing pool 
def process_image(image_name):
	img = Image.open(os.path.join(image_folder, image_name))

	img = img.filter(ImageFilter.GaussianBlur(15))

	img.thumbnail(size)
	img.save(f'{image_folder}/processed/{image_name}')
	print(f'{image_name} was processed...')

if __name__ == "__main__":
	with concurrent.futures.ProcessPoolExecutor() as executor:
		executor.map(process_image, image_names)


t2 = time.perf_counter()
print(f'finished in {t2-t1} seconds')






