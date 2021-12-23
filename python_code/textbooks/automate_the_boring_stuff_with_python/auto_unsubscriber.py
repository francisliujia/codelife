import webbrowser
import imaplib
import bs4
import pyzmail


def unsub_scan(username, user_pass):
	unsub_links = []
	imaplib._MAXLINE = 10_000_000
	imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
	imap_obj.login(user_name, user_pass)
	imap_obj.select_folder('INBOX', readonly=True)
	unique_ids = imap_obj.search(['ALL'])

	for identifier in unique_ids:
		raw_message = imap_obj.fetch([identifier], ['BODY[]', 'FLAGS'])
		message = pyzmail.PyzMessage.factory(raw_message[identifier][b'BODY[]'])
		html = message.html_part.get_payload().decode(message.html_part.charset)
		soup = bs4.BeautifulSoup(html, 'lxml')
		link_elems = soup.select('a')
		for selected in link_elems:
			if 'unsubscribe' in str(selected):
				unsub_links.append(selected.get('href'))

	imap_obj.logout()
	return unsub_links

email = input('enter your username: ')
password = input('enter your password: ')
links = unsub_scan(email, password)

for link in links:
	webbrowser.open(link)

print('All unsubscribe links have been opened.')