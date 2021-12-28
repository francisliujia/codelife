import pyautogui

def move_square():
	for i in range(10):
		pyautogui.moveTo(100, 100, duration=0.25)
		pyautogui.moveTo(200, 100, duration=0.25)
		pyautogui.moveTo(200, 200, duration=0.25)
		pyautogui.moveTo(100, 200, duration=0.25)

# move_square()
def move_rectangle():
	for i in range(10):
		pyautogui.moveTo(100, 0, duration=0.25)
		pyautogui.moveTo(0, 100, duration=0.25)
		pyautogui.moveTo(-100, 0, duration=0.25)
		pyautogui.moveTo(0, -100, duration=0.25)

