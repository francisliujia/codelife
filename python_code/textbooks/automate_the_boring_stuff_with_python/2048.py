from selenium import webdriver
from selenium.webdriver.common.keys import keys

browser = webdriver.Firefox()
browser.get('https://gabrieleciulli.github.io/2048')
html_elem = browser.find_element_by_tag_name('html')

while True:
	html_elem.send_keys(keys.UP)
	html_elem.send_keys(keys.RIGHT)
	html_elem.send_keys(keys.DOWN)
	html_elem.send_keys(keys.LEFT)