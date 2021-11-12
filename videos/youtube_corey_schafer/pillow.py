from PIL import Image, imageFilter
import os

# size_300 = (300,300)
# size_300 = (700,700)

# for f in os.listdir('.'):
# 	if f.endswith('.jpg'):
# 		# print (f)
# 		i = Image.open(f)
# 		fn, fext = os.path.splitext(f)
# 		# print(fn)
# 		# print(fext)

# 		i.thumbnail(size_700)
# 		# i.save('pngs/{}.png'.format(fn))
# 		i.save('700/{}_7  00{}'.format(fn, fext))

# 		i.thumbnail(size_300)
# 		# i.save('pngs/{}.png'.format(fn))
# 		i.save('300/{}_300{}'.format(fn, fext))



image1 = Image.open('Screenshot.jpg')
# image1.show()
# image1.save('Screenshot.png')
# image1.rotate(90).save('screen_mod.jpg')
# image1.covert(mode='L').save('screen_mod2.jpg')
image1.filter(imageFilter.GassianBlur(15 )).save('screen_mod2.jpg')



