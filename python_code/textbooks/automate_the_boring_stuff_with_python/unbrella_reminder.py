import requests
import bs4
from twilio.rest import TwilioRestClient

def rain_check():
	url = 'https://weather.com/en-GB/'
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	weather_elem = soup.select('#styles-xz0ANuUJ_nowBlurb_17gst')
	weather = weather_elem[0].getText()

	if 'rain' in weather.lower():
		return True


account_sid = 'ACxxxxxxxx'
authToken = 'ACxxxxxxxx'
my_number = 'xxxxxxxxxx'
twilio_number = 'ACxxxxxxxx'

def text_myself(message):
	twilio_cli = TwilioRestClient(account_sid, authToken)
	twilio_cli.message.create(body=message,from_=twilio_number, to=my_number)

if rain_check():
	text_myself('Remenber to take  the umbrella.')
