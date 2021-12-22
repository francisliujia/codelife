accountID = 'XXXXXX'
authToken = 'XXXXXX'
my_number = 'XXXXXX'
twilio_number = 'XXXXXX'

from twilio.rest import TwilioRestClient

def test_myself(message):
	twilioCli = TwilioRestClient(accountID, authToken)
	twilioCli.message.create(body=message, from_=twilio_number, to=my_number)
	