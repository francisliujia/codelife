import pyautogui
print("Press Ctr_C to quit")

try:
	while True:
		x, y = pyautogui.position()
		positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		pixel_color = pyautogui.screenshot().getpixel((x, y))
		positionStr += ' RGB: (' + str(pixel_color[0]).rjust(3)
		positionStr +=  ', ' + str(pixel_color[1]).rjust(3)
		positionStr += ', ' +str(pixel_color[2]).rjust(3) + ')'
		print(positionStr, end='')
		print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
	print('\nDone')