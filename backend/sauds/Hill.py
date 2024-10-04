#from math import sqrt
#import numpy as np
#from sympy import sympy.Matrix
import sympy
from statistics import mode
from itertools import product
from clipboard import copy, paste
#from IOC import cal_split_IOC
from wordninja import split
from random import randint
from time import time

def round_up(x, y):
	remainder = x % y
	if remainder == 0:
		return x
	else:
		return x+(y-remainder)
	
def chr_to_num(character:str):
	if chrs==26:
		return ord(character)-65
	else:
		return ord(character)
	
def num_to_chr(number:int):
	if chrs==26:
		return chr(number+65)
	else:
		return chr(number)
	
def invertable(matrix: sympy.Matrix):
	if matrix.det()%chrs==0:
		return 0
	try:
		matrix.inv_mod(chrs)
	except sympy.matrices.common.NonInvertibleMatrixError:
		return 0
	return 1

def iter_to_string(matrix: sympy.Matrix, seperator: str):
	return seperator.join(str(i) for i in matrix)

def find_matrix(ciphertext_matrix, plaintext_matrix):
#	ciphertext_matrix = sympy.Matrix.row_join(*(i for i in ciphertext_matrix)).T
#	plaintext_matrix = sympy.Matrix(plaintext_matrix)
#	try:
	matrix = ((ciphertext_matrix.inv_mod(chrs)*plaintext_matrix)%chrs).T
#	except sympy.matrices.common.NonInvertibleMatrixError:
#		matrix = ((ciphertext_matrix*plaintext_matrix.inv_mod(chrs))%chrs).T.inv_mod(chrs)
	return matrix

def find_most_occuring(values: list | tuple, most: int):
	top = []
	for i in range(most):
		newest = mode(values)
		top.append(newest)
		values = filter(lambda x: x != newest, values)
	return top

#chrs = 26
#print(find_matrix(sympy.Matrix([[0, 7],[11, 15]]), sympy.Matrix([[19,7],[7,4]])))
def text_to_matrix(text: str, side: int):
	return sympy.Matrix([
		[chr_to_num(text[i+j]) for j in range(side)]
		for i in range(0, len(text), side)
	])

def generate_cipher_matrices(cipher: int, side: int):
	chunked = [cipher[i:i+side] for i in range(0, len(cipher)-(side-1), side)]
	return [sympy.Matrix([[chr_to_num(letter)] for letter in chunk]) for chunk in chunked]

def decrypt_hill_cipher(matrix: sympy.Matrix, cipher_list: list | tuple):
	text = []
	for cipher_matrix in cipher_list:
#	for cipher_part in cipher_list:
#		cipher_matrix = sympy.Matrix([[chr_to_num(i)] for i in cipher_part])
		text.extend(num_to_chr(i%chrs) for i in (matrix*cipher_matrix))
	return "".join(text)

if int(input("Do you want to use the modified hill cipher or the regular hill cipher?\n\n1 - modified hill cipher\n0 - regular hill cipher\n\n")):
	chrs = input("What is the base? (leave blank for 55296)\n\n")
	if chrs == "":
		chrs = 114112
#		chrs = 55296
	else:
		chrs = int(chrs)
else:
	chrs=26
side = int(input("What type of hill cipher do you want to use? (e.g. 2 for 2x2 hill cipher)\n\n"))
key_size = side**2
while 1:
	if chrs != 26:
		print("As you are using the modified hill cipher, you may have trouble pasting and copying the ciphertext manually.")
	if int(input("Where do you want the text to taken from?\n1 - My clipboard\n0 - I want to type it\n\n"))==1:
		cipher = paste()
	else:
		cipher = input("What is the text that wish to change?\n\n")
	#cipher="""VNFB""".upper()
	if chrs == 26:
		cipher = cipher.upper()
		cleaned = []
		for i in cipher:
			num = ord(i)
			if 64<num<91:
				cleaned.append(i)
		if len(cipher) != 0:
			cipher="".join(cleaned)
			del num
		del cleaned
	if (len(cipher)%side) != 0:
		print(f"You need to have {side-(len(cipher)%side)} more {'letter' if (side-(len(cipher)%side))==1 else 'letters'} so that the text may be encrypted/decrypted")
	else:
		break

cipher_matrices = generate_cipher_matrices(cipher, side)
if int(input("Do you want to do with the hill cipher?\n0 - Encrypt\n1 - Decrypt\n\n")):
	keyword = input("Do you know the ENCRYPTION key (if you do enter it):\n").upper().replace(" ","")
	if keyword in {"", "NO"}:
		de_keyword = input("Do you know the DECRYPTION key (if you do enter it):\n").replace(" ","")
	else:
		de_keyword = ""
	if (keyword in {"", "NO"}) and (de_keyword in {"", "NO"}):
		brute = int(input("0 - Substution Equations\n1 - Brute Force (Recommended if you don't care how long it takes)\n\n"))
		# side = 2
		# cipher_matrices=[]
		# for cipher_part in cipher_list:
		# 	cipher_matrices.append(sympy.Matrix([[ord(i)-65] for i in list(cipher_part)]))
#		cipher_matrices = [sympy.Matrix([[chr_to_num(i)] for i in list(cipher_part)]) for cipher_part in cipher_list]
		if brute:	# Brute forcing key
			start = time()
			from nostril import nonsense
#			keyword_list = [0 for i in range(key_size)]
			for keyword_list in product(*(range(chrs) for i in range(key_size))):
			# while 1:
			# 	text, loop, j = "", 1, 0
			# 	while loop:
			# 		if keyword_list[j]<(chrs-1):
			# 			keyword_list[j]+=1
			# 			break
			# 		elif j+1<len(keyword_list):
			# 			keyword_list[j]=0
			# 			j+=1
			# 		else:
			# 			loop=0
			# 	if not loop:
			# 		break
				matrix = sympy.Matrix([keyword_list[i:i+side] for i in range(0,len(keyword_list),side)])
				if not invertable(matrix):
					continue
				if 2<(time()-start):
					print(f"\033[H\033[JTrying key: {', '.join(str(i).zfill(2) for i in keyword_list)}")
					start = time()
				text = decrypt_hill_cipher(matrix, cipher_matrices)
				try:
					if not nonsense(text):
						break
				except ValueError:
					pass
			inv_matrix = matrix.inv_mod(chrs)
		else:																		# Uses substitution equations to solve
			while 1:
				option = int(input("How do you plan to find the key?\n\n2 - Most common bigrams\n1 - Using a crib\n0 - Crib dragging\n\n"))
				if option == 2 and side != 2:
					print(f"You cannot use most common bigrams with a hill {side}x{side} cipher")
				else:
					break
			if option in {1,2}:
				if option == 2:	# Most common bigrams for 2x2
					cipher_list = [cipher[i:i+side] for i in range(0,(len(cipher)),side)]
					ciphertext_crib = "".join(find_most_occuring(cipher_list, side))
					plaintext_crib = "THHE"
				else:	# Using a crib
					print(f"The cribs must have been encrypted in no overlapping chunks. (Every {side})")
					while 1:
						ciphertext_crib = input("Enter the ciphertext crib:\n\n")[:key_size]
						plaintext_crib = input("Enter the plaintext crib:\n\n")[:key_size]
						if (len(ciphertext_crib) != key_size) or (len(plaintext_crib) != key_size):
							print(f"The cribs must be at least {key_size} characters in length")
						else:
							break
				ciphertext_matrix = text_to_matrix(ciphertext_crib, side)
				plaintext_matrix = text_to_matrix(plaintext_crib, side)
				matrix = find_matrix(ciphertext_matrix, plaintext_matrix)
			else:	# Crib dragging
				from nostril import nonsense
				plaintext_crib = input(F"What is the crib to drag?\n\n{(key_size)+side-1} is acceptable\nA minimum of {key_size} characters is acceptable\n\n")
				for i in range(len(cipher)-((key_size)-1)):
					ciphertext_crib_position = round_up(i, side)
					ciphertext_crib = cipher[
						ciphertext_crib_position:
						ciphertext_crib_position + (key_size)
					]
					difference = ciphertext_crib_position - i
					try:
						matrix = find_matrix(
							text_to_matrix(ciphertext_crib, side),
							text_to_matrix(plaintext_crib[difference:difference+(key_size)], side))
						text = decrypt_hill_cipher(matrix, cipher_matrices)
#						print(text)
#						sleep(1)
						if not nonsense(text):
							break
					except sympy.matrices.common.NonInvertibleMatrixError:
						continue
			inv_matrix = matrix.inv_mod(chrs)
			text = decrypt_hill_cipher(matrix, cipher_matrices)
#			text = decrypt_hill_cipher(matrix, cipher_list)

		print(f"\033[H\033[JEncryption Key: {iter_to_string(inv_matrix, ', ')}\nDecryption Key: {iter_to_string(matrix, ', ')}\n")
	else:									# Uses key to decrypt
		if keyword not in {"", "NO"}:
			keyword_list = keyword.split(",")
			matrix = sympy.Matrix([[int(keyword_list[row*side+column]) for column in range(side)] for row in range(side)])
			if not invertable(matrix):
				exit("Sorry but the key is not valid")
			matrix = sympy.Matrix(sympy.Matrix(sympy.Matrix.tolist(matrix)).inv_mod(chrs))
		else:
			matrix = sympy.Matrix([[int(de_keyword.split(",")[row*side+column]) for column in range(side)] for row in range(side)])
			if not invertable(matrix):
				exit("Sorry but the key is not valid")
		text = decrypt_hill_cipher(matrix, cipher_matrices)
		print("\033[H\033[J")
	if len(input("Text:\n\n"+text+("\n\nText with spaces:\n\n"+" ".join(split(text)) if chrs==26 else "")+"\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)
else:
	if input("Do you want to randomize a key?\n\n").lower() == "yes":
		while 1:																							# Key randomiser
			keyword_list = [[randint(0,chrs-1) for column in range(side)] for row in range(side)]
			matrix = sympy.Matrix(keyword_list)
			if invertable(matrix):
				break
	else:																									# Enter a custom key
		keyword = input("What is the encryption key?\n\n").replace(" ","")
		matrix = sympy.Matrix([[int(keyword.split(",")[(row*side)+column]) for column in range(side)] for row in range(side)])
		if not invertable(matrix):
			exit("Sorry but the key is not valid")
	text = decrypt_hill_cipher(matrix, cipher_matrices)
	if len(input(f"\033[H\033[JEncyption key: {iter_to_string(matrix, ', ')}\n\nText:\n\n{text}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)