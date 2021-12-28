import time 
import pyautogui

print("waker activated, press Ctrl-c to quit.")
try:
	while True:
		pyautogui.moveTo(100, 200, 0.25)
		pyautogui.moveTo(200, 100, 0.25)
		time.sleep(5)
except KeyboardInterrupt:
	print(' waker deactivated')