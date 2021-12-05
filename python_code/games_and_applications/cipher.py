# import string
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_SIZE = (len(SYMBOLS))

def get_mode():
	while True:
		print("Do you wish to encrypt or decrypt a message?")
		mode = input().lower()
		if mode in ['encrypt', 'e', 'decrypt', 'd']:
			return mode
		else:
			print('Enter the "encrypt", "e", "decrypt" or "d".')


def get_messgae():
	print('Enter your message')
	return input()


def get_key():
	key = 0
	while True:
		print('Enter the key number (1-%s)' %(MAX_KEY_SIZE))
		key = int(input())
		if (key >= 1 and key <= MAX_KEY_SIZE):
			return key


def get_translated_message(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''

	for symbol in message:
		symbol_index = SYMBOLS.find(symbol)
		if symbol_index == -1:
			translated += symbol
		else:
			symbol_index += key

			if symbol_index >= len(SYMBOLS):
				symbol_index -= len(SYMBOLS)
			elif symbol_index < 0:
				symbol_index += len(SYMBOLS)

			translated += SYMBOLS[symbol_index]
	return translated


mode = get_mode()
message = get_messgae()
key = get_key()
print('Your translated message is:')
print(get_translated_message(mode, message, key))











