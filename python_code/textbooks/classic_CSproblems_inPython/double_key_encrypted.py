from secrets import token_bytes
from typing import Tuple 

def random_key(length):
	tb = token_bytes(length)
	return int.from_bytes(tb, 'big')

def encrypt(origin):
	origin_bytes = origin.encode()
	dummy_key = random_key(len(origin_bytes))
	origin_key = int.from_bytes(origin_bytes, 'big')
	encrypted_key = origin_key ^ dummy_key
	return dummy_key, encrypted_key

def decrypt(key1, key2):
	decrypted = key1 ^ key2
	temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
	return temp.decode()

if __name__ == "__main__":
	key1, key2 = encrypt("out best time")
	print(key1, key2)
	result = decrypt(key1, key2)
	print(result)