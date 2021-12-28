import pyautogui, time 

name_fileld = (684, 319)
submit_button = (651, 817)
submit_button_color = (75, 141, 249)
submit_another_link = (760, 224)

formdata = [
{'name':'Alice', 'fear':'eaverdrops', 'source':'', 'robocop':'4', 'comments':'tell Bob i said it', },
{'name':'Bob', 'fear':'bees', 'source':'amulet', 'robocop':'4', 'comments':'n/a', },
{'name':'Carol', 'fear':'puppets', 'source':'crystal ball', 'robocop':'1', 'comments':'please take the puppets out of the break room', },
{'name':'Alex Murphy', 'fear':'Ed-209', 'source':'money', 'robocop':'5', 'comments':'protect the innocent, serve the public trust, uphold the law', },
]

for person in formdata:
	print('5 seconds pause to let user press Ctrl-c')
	time.sleep(5)

	while not pyautogui.pixelMatchsColor(submit_button[0], submit_button[1], submit_button_color):
		time.sleep(0.5)

	print('Entering %s info...' %(person['name']))
	pyautogui.click(name_fileld[0], name_fileld[1])
	pyautogui.typewrite(person['name'] + '\t')
	pyautogui.typewrite(person['fear'] + '\t')

	if person['source'] == 'wand':
		pyautogui.typewrite(['down', '\t'])
	elif person['source'] == 'amulet':
		pyautogui.typewrite(['down', 'down', '\t'])	
	elif person['source'] == 'crystal ball':
		pyautogui.typewrite(['down', 'down', 'down', '\t'])	
	elif person['source'] == 'money':
		pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])


	if person['robocop'] == 1:
		pyautogui.typewrite([' ', '\t'])
	elif person['robocop'] == 2:
		pyautogui.typewrite(['right','right', '\t'])
	elif person['robocop'] == 3:
		pyautogui.typewrite(['right','right','right', '\t'])
	elif person['robocop'] == 4:
		pyautogui.typewrite(['right','right','right', '\t'])
	elif person['robocop'] == 5:
		pyautogui.typewrite(['right','right','right','right', '\t'])


	pyautogui.typewrite(person['comments'], + '\t')
	pyautogui.press('enter')
	print('Click Submit')
	time.sleep(5)
	pyautogui.click(submit_another_link[0], submit_another_link[1])








