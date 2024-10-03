from clipboard import copy, paste
from bitarray import bitarray
#import bee
import filetype, magic
from math import ceil
from os.path import split, basename, realpath
from base64 import a85decode, a85encode
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
root.attributes('-topmost', True)
root.overrideredirect(True)

def encrypt_text(key: bytes|bytearray, plaintext: bytes|bytearray, mode=0, offset=0):
	if mode == 0:	# Addition
		encrypted_bytes = bytearray((plaintext[i]+key[(i+offset)%len(key)])%256 for i in range(len(plaintext)))
	elif mode == 1:	# XOR
		encrypted_bytes = bytearray((plaintext[i]^key[(i+offset)%len(key)]) for i in range(len(plaintext)))
	else:	# XOR and Addition
		bits = bitarray()
#		bits.frombytes(key[:ceil(len(key)/8)])/
		bits.frombytes(key[offset:offset+ceil(len(key)/8)])
		while len(bits)<len(key):
			bits.frombytes(key[:ceil((len(key)-len(bits))/8)])
		encrypted_bytes = bytearray()
		for i in range(len(plaintext)):
			if bits[i%(len(bits))]:	# If bit i is 1 do an XOR operation
				encrypted_bytes.append((plaintext[i]^key[(i+offset)%len(key)]))
			else:	# Otherwise do an addition operation
				encrypted_bytes.append((plaintext[i]+key[(i+offset)%len(key)])%256)
	return encrypted_bytes
def decrypt_text(key: bytes|bytearray, ciphertext: bytes|bytearray, mode=0, offset=0):
	if mode == 0:	# Subtraction
		decrypted_bytes = bytearray((ciphertext[i]-key[(i+offset)%len(key)])%256 for i in range(len(ciphertext)))
	elif mode == 1:	# XOR
		decrypted_bytes = bytearray((ciphertext[i]^key[(i+offset)%len(key)]) for i in range(len(ciphertext)))
	else:	# XOR and Subtraction
		bits = bitarray()
#		bits.frombytes(key[:ceil(len(key)/8)])
		bits.frombytes(key[offset:offset+ceil(len(key)/8)])
		while len(bits)<len(key):
			bits.frombytes(key[:ceil((len(key)-len(bits))/8)])
		decrypted_bytes = bytearray()
		for i in range(len(ciphertext)):
			if bits[i%(len(bits))]:	# If bit i is 1 do an XOR operation
				decrypted_bytes.append((ciphertext[i]^key[(i+offset)%len(key)]))
			else:	# Otherwise do an addition operation
				decrypted_bytes.append((ciphertext[i]-key[(i+offset)%len(key)])%256)
	return decrypted_bytes

encrypt = int(input("What do you want to do?\n\n1 - Encrypt\n0 - Decrypt\n\n"))
if int(input(f"What should we {'encrypt' if encrypt else 'decrypt'}?\n\n1 - Text\n0 - File\n\n")):
	filename = ""
	if int(input("Where do you want the text to come from?\n\n1 - Clipboard\n0 - I want to type it in\n\n")):
		to_modify = paste()
	else:
		to_modify = input(f"What is the text that you want to {'encrypt' if encrypt else 'decrypt'}?\n\n")
	if encrypt:	# Turn text into bytes
		to_modify = to_modify.encode()
	else:	# Turn ascii85 into bytes
		to_modify = a85decode(to_modify)
else:
	print(f"A seperate window has been opened for you to select the file that you want to {'encrypt' if encrypt else 'decrypt'}.")
	filepath = filedialog.askopenfilename(filetypes=(("All Files", "*.*"),))
	filename = split(filepath)[-1]
	file = open(filepath, "rb")
	to_modify = file.read()
	file.close()
key_mode = int(input(f"Do you want to choose a key?\n{'(It is reccomended to have a key larger or equal than the data being hidden)' if encrypt else ''}\n\n0 - No, use the bee movie script\n1 - Yes, as text\n2 - Yes, as a file\n\n"))
if key_mode == 0:	# Reading the Bee Movie Script as the key
	file = open((realpath(__file__).replace(basename(__file__),"Bee.txt")), "rb")
	key = file.read()
	file.close()
elif key_mode == 1:	# Reading the key as text
	while 1:
		if int(input("Where do you want the key to come from?\n\n1 - Clipboard\n0 - I want to type it in\n\n")):
			key = paste()
		else:
			key = input("What is the key?\n\n")
		key = key.encode()
		if len(key) == 0:
			print("The key cannot be empty.")
else:	# Reading a file as the key
	while 1:
		print(f"A seperate window has been opened for you to select the file to be used as a key.")
		filepath = filedialog.askopenfilename(filetypes=(("All Files", "*.*"),))
		file = open(filepath, "rb")
		key = file.read()
		file.close()
		if len(key) == 0:
			print("The file to be used as a key cannot be empty.")
offset = int(input(f"What is {'the' if encrypt else 'was'} offset?\n(This is a number between (and including) 0 and {len(key)})\n(The number will be mod {len(key)})\n\n"))%len(key)

encryption_type = int(input("What mode would you like to use?\n\n0 - Addition mode, can be broken\n1 - XOR mode, can be broken\n2 - Addition + XOR mode, very secure (mixes in both modes)\n\n"))
if encrypt:
	modified = encrypt_text(key, to_modify, encryption_type, offset)
else:
	modified = bytes(decrypt_text(key, to_modify, encryption_type, offset))
	print(f"Type (from magic): {magic.from_buffer(modified)}\nFile MIME type (from magic): {magic.from_buffer(modified, mime=True)}\nFile extension (from filetype): {filetype.guess(modified).extension}\nFile MIME type (from filetype): {filetype.guess(modified).mime}")
if int(input(f"What format do you want the {'encrypted' if encrypt else 'decrypted'} data?\n\n1 - Text\n0 - A file\n\n")):
	if encrypt:
		modified = a85encode(modified).decode()
	else:
		modified = modified.decode()
	if len(input(f"\033[H\033[JText:\n\n{modified}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(modified)
else:
	print("A seperate window has been opened for you to select where and what to save the file as.")
	filepath = filedialog.asksaveasfilename(initialfile=filename, filetypes=(("All Files", "*.*"),))
	file = open(filepath, "wb")
	file.write(modified)
	file.close()