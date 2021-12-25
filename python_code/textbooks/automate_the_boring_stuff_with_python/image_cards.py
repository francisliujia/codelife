import os 
from PIL import Image
from PIL import ImageDraw 
from PIL import ImageFont


def create_card(name):
	card = Image.new('RGBA', (360, 288), 'white')
	flower = Image.open('zophie.png')
	card.paste(flower, (10, 40))
	cut_guide = Image.new('RGBA', (364, 292), 'black')
	cut_guide.paste(card, (2, 2))

	draw_obj = ImageDraw.Draw(cut_guide)
	fonts_folder = 'user/share/fonts/TTF'
	custom_font = ImageFont.truetype(os.path.join(fonts_folder, 'ariel.ttf'), 72)
	draw_obj.text((120, 100), name, fill='blue', font=custom_font)
	cut_guide.save('{}-invite.png'.format(name))


with open('guests.txt') as f:
	guests = f.readlines()
print(guests)

for guest in guests:
	create_card(guest)

print('All invations cards have been sent.')