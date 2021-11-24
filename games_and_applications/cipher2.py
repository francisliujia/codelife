# import string
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!@£$%^&*()Œ„‰ÂÊÁËÈØ∏ÅÍÎÏÌÓÔÒÛÙÇ◊ıˆ˜'
MAX_KEY_SIZE = (len(SYMBOLS))

def get_mode():
	while True:
		print("Do you wish to encrypt or decrypt or brute-force a message?")
		mode = input().lower()
		if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:
			return mode
		else:
			print('Enter the "encrypt", "e", "decrypt" or "d", "brute" or "b".')


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
if mode[0]!= 'b':
	key = get_key()
	print(get_translated_message(mode, message, key))
else:
	for key in range(1, MAX_KEY_SIZE+1):
		print(key, get_translated_message('decrypt', message, key))











