"""
Honestly this would take many many many centuries (because of the 26! combinations) at most to complete (in brute force mode)...
Just don't waste your time...
Its not worth it at all...
"""
import HillClimb
from random import randrange
from math import sqrt
from array import array

def fill_key(key, pad_mode, alphabet):
	last_char = key[-1]
	key = key.upper()
	for i in (
			(
				(x+(ord(last_char)-65))%len(alphabet)
				for x in range(len(alphabet))
			)
			if pad_mode else
			range(len(alphabet))
		):
		letter = alphabet[i]
		if letter not in key:
			key += letter

	return key

def invert_key(key: str, alphabet: str):
	inverted = array("u", (" " for i in range(len(alphabet))))
	for i in range(len(alphabet)):
		index = key.index(alphabet[i])
		inverted[i] = alphabet[index]

	return "".join(inverted)

def decrypt_substitution(key, cipher: str):
	text = array("u")
	for i in range(len(cipher)):
		letter = cipher[i]
		if letter.isupper():
			text.append(key[(ord(letter)-65)])

		elif letter.islower():
			text.append(key[(ord(letter)-97)].lower())

		else:
			text.append(letter)

	return "".join(text)

def decrypt_polybius(key, cipher: str):
	text = array("u")
	offset = 0
	cipher_split = []
	grid_size = int(sqrt(len(key)))
	for i in range(0,(len(cipher)), 2):
		try:
			while 1:
				if 64<ord(cipher[i+offset])<91 or 96<ord(cipher[i+offset])<123:
					cipher_split.append(
						cipher[
							(i+offset):
							(i+2+offset)
						]
					)
					break
				else:
					cipher_split.append(cipher[i+offset])
					offset += 1
		except Exception:
			break

	for letter_pair in cipher_split:
		if len(letter_pair) == 2:
			text.append(
				key[
					((ord(letter_pair[0])-65)*grid_size)+
					(ord(letter_pair[1])-65)
				]
			)
		else:
			text.append(letter_pair)

	return "".join(text)

def modify_key(key):
	key = list(key)
	letters_to_swap = (						# swap 2 random letters in the key
		randrange(len(key)),
		randrange(len(key))
	)
	key[letters_to_swap[0]], key[letters_to_swap[1]] = \
	key[letters_to_swap[1]], key[letters_to_swap[0]]

	return "".join(key)

if __name__ == "__main__":
	from clipboard import copy, paste
	from wordninja import split
	if int(input("Where do you want the text to be from?\n\n1 - My clipboard\n0 - I want to type it\n\n")):
		cipher = paste()
	else:
		cipher = input("What is the text that you want to decrypt?\n\n")
	#cipher = "33512 53443 21114 22523 14422 53534 11352 24224 21253 45425 55213 44224 14432 15321 21343 33515 21221 51325 42221 33242 24143 42554 35133 25524 14432 12435 41215 54125 34312 11542 35341 12414 43214 11535 43255 52155 54322 11415 21432 55521 34542 14224 14424 22421 15214 41411 14543 53411 41251 51454 51423 51142 21143 22215 35333 35132 25531 51415 51143 45542 24144 22143 25552 13454 21413 52534 42114 23533 51213 34132 35512 11535 15144 23221 14114 21135 33213 53421 25342 42511 21334 13235 51332 13442 33151 53523 21151 12414 55413 21434 34215 54235 55353 41442 21422 42154 35323 22154 42253 53442 35422 42154 25425 13225 53151 41551 25343 51555 21154 23541 15353 33542 21242 51154 14334 11425 23342 23515 21322 15442 25353 44235 23354 32115 34351 55313 42422 42153 35353 11114 15212 21415 42353 54314 32131 45332 21423 52325 43211 44414 51143 45525 42251 12114 11514 23553 21322 52143 21422 41442 24214 43513 32552 41443 21421 52521 55423 51521 14322 51121 11353 32135 22422 41442 43143 21321 22351 52425 33112 13222 21114 12154 25143 23251 11253 45421 14342 13221 54422 53534 25111 43421 45412 13411 25432 15313 11253 42111 11253 43513 15114 21442 21422 42115 21141 52114 55432 11542 25112 13321 34421 14235 41131 55424 14112 11434 55253 42232 13213 44225 14324 12135 41322 14424 35342 12155 42355 32154 35344 32534 54215 54235 53145 43124 25332 54225 11335 15513 42511 41154 13114 23555 25143 43522 42242 15435 32322 15442 25353 44235 41153 54221 54422 54225 54143 43435 42322 14224 25335 52111 42153 55121 43211 55142 24253 42344 21241 44321 53132 53242 42352 32142 24211 52542 44141 13351 24354 12142 24144 25351 23144 22421 15253 42321 34351 32324 21432 55521 34542 14235 25345 41525 33253 41442 21242 53325 54351 33255 54353 44325 34542 13315 15352 32115 11423 53221 14432 14224 21322 55315 14155 11432 35342 12524 14432 11141 21344 25121 14151 15413 15144 22534 23254 21434 55254 25435 34421 42534 11331 43451 41152 15425 35131 12542 21331 12554 35133 25534 35425 32114 15423 53235 11212 54225 24144 32111 24354 43424 25334 22421 32214 24221 15112 21535 33412 53431 21154 23534 11143 45542 15252 15542 35152 11411 35344 42542 24242 53324 21251 14321 15511 43423 15514 42542 24332 11434 55312 12141 11111 45125 34234 22414 42422 42155 21144 22414 34554 22421 14424 22133 41422 15542 24212 24224 14553 43542 24253 42342 35553 54425 42242 42533 24212 51115 25232 44242 24144 24224 21152 12511 34354 22425 34235 43534 54321 31125 43212 53442 24212 14325 55213 45421 53134 21411 25413 52534 42215 53513 42423 52425 33422 42115 21553 52111 34354 23421 21554 23553 21143 45141 15353 52221 43213 44224 21111 31141 25542 53534 35222 42511 25344 33532 43213 32134 42443 51332 55112 14321 15213 25155 14331 42321 24251 11521 41134 21442 25353 41434 55443 51332 55552 11142 15355 12425 11542 41434 54213 52221 32215 44225 35342 42124 14114 22415 21144 22134 21554 23522 25152 13321 53134 22542 25111 43421 33414 25142 24152 11442 24215 41434 34354 21422 22351 55522 35153 32142 35421 43231 42354 22421 41152 11111 13344 22532 24211 42315 21211 14235 33515 52133 14345 51125 44253 23254 35344 22534 13214 23524 14151 41111 24253 31434 55423 55313 25325 53351 21432 55521 34542 13351 32255 31514 15513 31311 42532 14115 35422 15442 21551 44214 32325 43511 4211".replace(" ", "").replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D").replace("5", "E")

	spaces = input("0 - Leave out adding spaces\n1 - Place spaces back\n\n")
	spaces = 0 if spaces == "" else int(spaces)
	if spaces:
		cipher = cipher = cipher.replace(" ", "")

	mode = int(input("\033c0 - Solve substitution cipher with key\n1 - Solve substitution cipher via brute force (takes way too long do NOT try)\n2 - Solve substitution cipher via Hill climbing\n3 - Solve polybius cipher with key\n4 - Solve polybius cipher via hill climbing\n\n"))

	if mode in {0, 1, 2}:
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	else:
		alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

	if mode == 0:	# Solve substitution with key
		key = input("What is the key?\n\n")

		pad_mode = int(input("How do you want to fill the key\n\n0 - Pad alphabetically\n1 - Pad like keyword substitution\n\n"))
		key = fill_key(key, pad_mode, alphabet)

		if int(input("Do you want to invert the key?\n\n1 - yes\n0 - no\n\n")):
			key = invert_key(key, alphabet)

		text = decrypt_substitution(key, cipher)

	elif mode == 1:	# Brute force substitution (don't even try it's not worth it at all)
		exit("We will assume you will not want to waste your life waiting for eternity.")
		from itertools import permutations
		from math import factorial
		from nostril import nonsense
		num_combinations = factorial(26)
		i = 0
		for c in permutations(alphabet):
			i += 1
			print(f"\033[H\033[JTrying combinations {i} out of {num_combinations}\n{i/num_combinations}%")
			text = decrypt_substitution(c, cipher)
			if not nonsense(text):
				key = c
				break
		else:
			exit("No key could be found")

	elif mode == 2:	# Hill climb substitution
		text, key = HillClimb.threaded_hill_climb(
			decrypt_substitution,
			cipher,
			lambda x:x,
			alphabet,
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nKey used: {best_key}\nInverted key: {invert_key(best_key, alphabet)}\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			same_key = True
		)

	elif mode == 3:	# Solve polybius with key
		key = fill_key(input("What is the key?\n\n"), 0, alphabet)
		text = decrypt_polybius(key, cipher)

	elif mode == 4:	# Hill climb polybius
		text, key = HillClimb.threaded_hill_climb(
			decrypt_polybius,
			cipher,
			lambda x:x,
			alphabet,
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nKey used: {best_key}\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			same_key = True
		)

	if mode in {0, 1, 2}:
		inverted = invert_key(key, alphabet)
		print(f"\033[H\033[JSubstitution Table used:\n\n{alphabet}\n{key}\n\nInverted Substitiution Table:\n\n{alphabet}\n{inverted}")
	
	else:
		key_size = int(sqrt(len(key)))
		print(f"\033[H\033[JPolybius key used:\n\n{key}\n\nPolybius square:\n\n" + '\n'.join(key[i:i+key_size] for i in range(0, len(key) - (key_size - 1), key_size)))

	print(f"\nText:\n\n{text}")

	if spaces:
		print(f"\nText with spaces:\n\n{' '.join(split(text))}")


	if len(input("\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)