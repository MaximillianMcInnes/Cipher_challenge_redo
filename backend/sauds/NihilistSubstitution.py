import HillClimb
from random import randrange
def search_polybius(key: str, letter: list | tuple | str):
	if len(letter) == 1:
		index = key.index(letter)
		return (index//5)+1, (index%5)+1	# If you are finding the row, column
#		return (index%5)+1, (index//5)+1	# If you are finding the column, row
	elif len(letter) == 2:
		return key[((int(letter[0])-1)*5)+(int(letter[1])-1)]	# If you are finding the letter at the row, column
#		return key[((letter[1]-1)*5)+(letter[0]-1)]				# If you are finding the letter at the column, row
	else:
		exit(f"Incorrect key given: {letter}")
def shift_nihilist(key, cipher: list | tuple):
	return [cipher[i]-key[i%len(key)] for i in range(len(cipher))]	# Subtract shifts from ciphertext
def convert_shift_key(polybius_key, shift_key: str | list | tuple):
	if isinstance(shift_key, str):
		return [int("".join([str(j) for j in search_polybius(polybius_key, i)])) for i in shift_key]
	else:
		return ''.join([search_polybius(polybius_key, str(i)) for i in shift_key])
def decrypt_nihilist(key, cipher: list | tuple):	# Polybius square key
	text = []
	for i in range(0, len(cipher)):
		coord = str(cipher[i])
		text.append(search_polybius(key, coord))
	return "".join(text)
def modify_key(key: str):
	key = list(key)
	letters_to_swap = (						# swap 2 random letters in the key
		randrange(len(key)),
		randrange(len(key))
	)
	key[letters_to_swap[0]], key[letters_to_swap[1]] = key[letters_to_swap[1]], key[letters_to_swap[0]]
	return "".join(key)
def remove_repeats(x: list):
	filtered = []
	for i in x:
		if i not in filtered:
			filtered.append(i)
	return filtered
def find_shift_key(cipher: list | tuple):
	if isinstance(cipher[0], int):
		cipher = [str(i) for i in cipher]
	nums_used = remove_repeats(cipher)
	columns = IOC_columns(cipher, alphabet=nums_used)[0]	# Gets how long the key could be
	occurences = cal_split_IOC(cipher, columns, do_occurences=1, alphabet=nums_used)['occurences']	# gets which numbers where used in each section of the key they were applied to
	numbers_in_each_column = [[] for i in range(columns)]
	for i in range(columns):
		for num in range(len(nums_used)):
			if occurences[i][num] != 0:
				numbers_in_each_column[i].append(nums_used[num])
	possible_keys = []
	for i in range(len(numbers_in_each_column)):	# Find possible column shifts
		minimum = int(min(numbers_in_each_column[i], key=(lambda x:int(x))))
		maximum = int(max(numbers_in_each_column[i], key=(lambda x:int(x))))
		highest, lowest = max(minimum-11, maximum-55), min(minimum-11, maximum-55)
		possible_keys.append([i for i in range(lowest, highest+1) if 0<=i])
#		possible_keys.append([i for i in range(maximum-55, minimum-11+1) if 0<=i])
#		key.append(min(minimum-11, maximum-55))
	# shift = lowest-11 or highest-55
	key = []
	for i in range(len(possible_keys)):	# For each column
		for shift in range(len(possible_keys[i])):	# For each possible shift in each column
			shift_str = str(possible_keys[i][shift])
			if len(shift_str) == 2 and 47<ord(shift_str[0])<54 and 47<ord(shift_str[1])<54:	# If the key seems valid
				for number in range(len(numbers_in_each_column[i])):	# Check if the shift produces valid numbers
					shifted_number_str = str(int(numbers_in_each_column[i][number])-possible_keys[i][shift])				
					if not (len(shifted_number_str) == 2 and 47<ord(shifted_number_str[0])<54 and 47<ord(shifted_number_str[1])<54):
						break
					if int(shifted_number_str) > 55:
						exit(shifted_number_str)
				else:	# If all subtracted numbers seem valid
					key.append(possible_keys[i][shift])
					break
#	print(key)
#	print(possible_keys)
	return key
if __name__ == "__main__":
	import sys, os
	from clipboard import copy
	from wordninja import split
	sys.path.insert(0, os.path.realpath(__file__).replace("pypy\\"+os.path.basename(__file__),"CPython"))
	from IOC import IOC_columns, cal_split_IOC
	cipher = "97 26 57 58 105 68 57 69 58 35 58 73 88 58 79 45 74 98 104 110 56 80 26 36 97 106 69 75 100 28 54 58 63 108 95 67 39 35 87 102 89 98 78 28 68 57 85 68 67 100 48 46 68 96 67 97 106 49 36 79 64 88 75 106 67 76 58 63 109 78 106 69 74 100 74 89 85 78 48 78 87 96 67 57 67 48 46 68 96 67 98 89 69 37 58 102 107 99 69 45 46 90 85 78 77 69 38 54 57 64 67 96 67 26 78 68 65 77 68 70 29 37 58 74 69 68 68 55 74 68 84 106 99 106 37 45 79 105 90 95 78 65 37 100 74 69 57 106 39 57 98 106 67 75 88 28 36 97 82 106 67 100 65 46 67 85 77 67 69 27 57 100 93 108 56 110 69 37 77 104 106 79 68 48 36 96 63 77 79 79 37 46 59 95 67 67 100 26 36 76 63 100 78 80 26 45 60 63 110 67 96 28 78 67 102 97 56 68 48 58 98 63 67 87 98 28 36 68 86 79 95 108 56 74 100 95 89 68 110 65 44 69 63 96 58 108 67 35 86 74 106 58 110 28 66 58 85 68 56 89 69 65 96 105 70 58 68 37 57 100 74 86 58 68 66 45 79 106 97 95 86 28 47 98 93 100 78 80 26 58 57 63 110 86 67 26 38 98 84 77 78 97 56 35 100 63 97 67 69 67 37 67 63 106 67 106 45 57 67 74 69 68 96 59 35 87 86 88 77 69 38 36 59 94 98 56 68 37 37 99 85 107 56 106 37 57 86 65 110 86 106 37 74 59 106 69 87 78 59 35 87 65 110 78 78 65 37 100 74 100 78 78 65 45 90 65 79 97 97 55 37 100 74 106 99 79 26 46 59 86 67 56 109 29 76 59 84 67 86 89 36 46 90 63 96 68 68 48 46 59 64 90 68 78 37 68 57 105 89 99 69 27 74 67 105 88 89 69 68 35 79 73 86 56 108 67 57 67 105 88 75 69 27 75 60 104 89 85 67 48 78 87 102 78 87 67 26 76 67 64 106 88 100 37 46 90 85 78 67 100 65 45 96 105 70 58 68 37 57 100 74 96 58 108 67 35 86 74 106 58 110 28 66 58 85 68 56 90 28 37 97 73 77 89 69 38 76 87 64 67 98 89 65 78 90 63 68 56 106 69 38 58 102 80 78 78 26 68 79 106 97 66 86 59 35 58 63 106 85 89 69 64 79 64 67 87 69 27 74 68 66 68 58 70 26 36 98 84 106 78 109 36 37 58 64 88 67 69 59 35 79 64 78 89 89 37 56 59 75 86 95 108 67 58 57 82 106 67 100 56 36 79 82 106 99 99 57 36 59 105 78 89 67 27 57 86 63 98 58 68 58 37 70 63 68 99 69 27 57 67 102 107 99 69 45 46 90 85 78 75 89 36 57 86 96 67 57 106 36 68 57 93 89 98 90 65 46 96 65 110 95 89 68 45 69 64 67 77 69 38 54 59 75 108 86 100 48 48 57 94 106 97 108 26 65 68 96 67 57 69 67 35 76 102 78 89 97 65 45 68 102 110 85 78 65 37 100 86 79 67 78 59 35 58 63 86 95 108 67 58 57 65 78 89 67 27 54 79 84 77 67 69 36 35 58 76 67 78 110 56 74 68 96 106 99 107 47 37 69 85 68 56 68 65 67 90 74 78 89 89 37 46 90 63 77 67 68 48 78 89 63 97 56 89 37 68 59 94 77 67 89 69 76 57 84 106 66 108 26 45 76 65 79 97 97 59 57 70 63 79 99 97 26 36 99 102 110 56 97 47 37 69 64 96 78 109 29 57 96 95 110 75 67 66 78 59 82 86 89 89 37 67 59 73 77 95 70 55 57 100 93 69 95 110 37 68 57 73 109 78 108 67 54 59 64 108 86 69 57 36 90 65 97 56 106 36 76 79 106 97 66 69 55 74 57 74 88 78 110 56 56 59 75 68 58 70 29 37 100 63 110 67 77 45 37 69 104 97 89 89 39 35 68 85 107 56 110 58 36 57 85 78 59 108 26 57 67 75 68 56 106 69 45 60 63 96 68 108 48 46 96 106 99 58 110 37 68 57 75 110 56 87 29 76 79 102 110 56 97 56 35 79 74 100 95 110 47 37 69 64 100 58 109 26 57 67 84 69 68 68 26 44 69 63 77 67 67 56 74 90 85 80 56 96 28 77 60 104 67 67 67 56 77 78 85 79 86 106 37 37 88 74 100 56 108 65 58 58 85 68 77 96 28 78 68 63 110 67 77 48 78 87 102 96 78 110 48 45 67 75 68 56 88 28 47 68 96 89 67 110 28 46 90 102 110 88 106 36 77 96 73 77 95 110 58 57 100 93 110 58 90 28 37 97 73 100 78 80 26 58 57 63 110 89 89 27 77 57 93 106 75 106 67 76 59 94 96 58 79 27 45 57 92 69 99 78 65 78 69 63 78 58 70 27 37 68 63 96 67 78 59 35 99 85 110 86 106 59 37 60 63 88 58 79 45 74 98 104 89 88 68 26 35 68 96 89 67 106 37 74 67 82 69 57 78 59 64 59 106 78 95 110 38 74 100 95 78 58 106 69 48 57 73 78 95 110 37 68 57 92 69 97 108 26 64 68 102 69 99 78 28 67 57 74 100 56 68 45 35 86 85 110 79 79 65 76 87 102 78 95 110 37 37 59 106 67 58 98 37 68 57 94 106 99 67 36 46 79 64 96 89 106 39 35 67 65 98 78 109 26 36 96 92 89 99 108 65 46 57 64 89 67 79 27 35 59 106 78 89 67 26 57 67 74 96 58 89 36 46 96 75 110 86 67 27 45 68 85 110 86 78 59 57 68 84 69 68 68 69 74 57 92 67 99 89 69 64 78 82 106 97 108 49 35 70 102 77 95 78 65 78 89 106 67 76 78 45 35 57 103 89 99 97 65 76 59 65 107 87 69 27 54 79 64 97 67 69 36 35 57 102 110 88 100 26 36 79 95 89 95 110 45 68 96 104 67 66 100 26 65 59 63 77 99 69 37 45 90 85 68 56 69 38 36 98 65 80 56 69 57 66 96 106 67 79 69 28 75 67 73 100 56 96 26 36 68 85 106 99 108 47 76 59 76 67 66 78 59 74 67 96 69 68 77 26 57 100 93 106 78 109 36 47 58 63 77 89 67 45 74 98 104 100 78 80 26 68 57 64 69 75 110 65 65 57 85 77 78 90 28 47 68 96 69 75 78 28 66 58 63 77 89 67 69 74 68 75 70 95 68 26 77 79 102 110 78 108 28 56 79 104 77 56 68 39 57 100 74 78 58 88 28 47 79 106 97 67 69 37 68 57 104 106 79 68 48 36 78 105 89 95 77 65 35"
	#cipher = "44 77 59 47 45 66 78 57 36 53 56 83 47 76 89 76 44 83 38 63 58 67 65 79 53 44 26 76 66 47 55 87 36 76 60 43 79 56 67 80 53 53 56 83 45 77 67 67 37 57 39 45 58 44 89 80 44 67 39 76 66 85 55 79 34 56 60 45 45 53 68 58 34 53 50 43 78 77 85 88 44 86 68 64 79 47 97 50 53 67 47 85 45 76 68 47 43 43 46 56 57 85 76 80 27 73 60 47 58 45 88 67 24 43 57 66 75 77 55 66 23 64 27 76 79 44 76 49 27 73 49 43 78 46 99 46 25 73 40 45 85 76 88 67 23 64 68 43 78 85 85 48 57 47 26 67 66 66 78 67 53 44 56 57 47 83 66 69 36 76 26 44 57 77 59 59 65 47 56 66 58 73 69 67 57 64 57 66 58 55 75 59 35 77 56 77 49 56 58 46 63 76 39 73 59 47 95 70 23 44 49 64 56 56 57 80 33 64 27 45 85 76 88 67 23 67 26 76 79 73 97 67 66 65 27 56 87 77 59 67 56 43 27 55 49 56 55 69 56 73 48 44 58 85 89 50 23 77 56 77 49 56 57 70 36 67 37 56 47 76 85 60 57 47 39 76 75 46 76 59 57 53 30 43 57 66 55 48 43 56 59 83 69 76 89 50 63 76 57 66 58 55 75 59 35 43 40 77 58 45 55 88 27 64 49 56 66 47 55 69 37 76 66 76 76 56 58 80 36 55 30 64 69 43 56 58 56 73 59 56 48 45 68 80 36 55 50 53 65 73 78 58 44 44 26 74 68 43 58 59 45 44 56 85 46 73 56 69 33 77 56 67 55 76 68 69 37"
	#cipher = "46 86 52 67 74 45 74 42 36 65 45 66 36 45 57 35 103 54 56 55 68 73 52 64 48 38 106 52 64 35 74 85 55 74 44 46 86 52 64 56 38 73 43 56 64 54 94 42 64 47 74 74 42 64 54 45 74 42 64 46 57 83 34 37 74 47 66 63 47 45 35 64 63 47 35 65 64 44 36 45 37 97 72 37 54 44 94 32 43 46 54 75 55 53 64 46 64 44 56 54 44 97 55 34 74 45 83 43 36 65 48 75 55 53 68 54 84 33 67 54 46 86 52 53 65 56 67 42 44 57 54 74 64 53 36 44 66 36 37 77 46 86 52 35 38 37 74 43 43 37 64 74 64 53 37 58 73 63 55 35 55 66 66 53 37 38 93 33 44 46 55 64 66 35 54 48 75 33 36 45 45 64 34 43 37 46 83 52 64 46 44 97 52 37 77 75 73 44 56 54 37 65 55 34 46 57 83 66 36 65 48 84 33 67 64 37 74 33 67 46 35 84 34 34 38 35 94 75 66 74 44 75 52 36 66 37 97 44 54 68 35 93 63 36 46 44 63 52 44 35 36 73 52 45 77 44 04 35 44 55 35 97 44 73 65 37 75 52 53 65 35 03 54 56 46 35 93 35 57 54 45 64 62 53 37 36 96 72 36 44 65 75 35 64 36 54 74 35 63 35 65 85 44 56 54 64 74 33 34 65 37 84 44 53 68 44 04 52 64 46 35 03 44 36 65 48 06 33 73 68 64 64 44 56 54 68 66 63 47 44 75 83 66 53 64 74 65 55 63 35 68 83 42 64 68 74 74 43 43 37 65 74 33 35 44 54 75 75 45 57 37 94 42 44 74 45 03 35 37 75 44 75 55 34 74 68 65 33 73 65 46 97 75 63 54 65 75 55 53 68 54 73 53 34 74 65 77 54 67 54 37 75 35 47 34 37 94 44 36 56 54 84 66 34 64 44 75 35 64 48 45 86 35 37 38 47 83 54 37 37 48 84 33 67 77 35 03 44 34 48 35 75 55 53 45 37 93 52 76 35 74 04 42 37 38 57 66 32 53 35 65 83 32 53 68 77 85 66 53 37 46 66 46 33 37 65 75 35 55 54 46 86 35 45 77 35 03 73 43 38 38 76 52 36 47 38 83 44 34 45 66 83 35 57 68 74 74 43 43 37 65 84 36 73 54 65 75 36 76 44 65 66 43 56 35 68 75 44 43 64 54"
	#cipher = "34 80 57 87 47 63 47 25 88 56 78 76 44 58 24 60 65 57 45 34 86 44 58 95 75 63 44 86 25 67 57 57 45 36 57 43 77 86 87 47 34 89 27 56 65 77 66 33 50 24 66 86 58 43 65 50 36 77 65 77 64 65 56 36 60 64 64 77 57 67 55 66 78 75 63 54 69 44 88 64 65 67 36 57 47 67 55 67 63 76 67 47 89 74 75 75 66 66 27 90 68 74 67 35 59 25 88 86 65 44 54 69 66 68 55 75 45 33 67 56 76 65 86 55 35 48 47 89 74 56 73 67 47 53 60 86 56 76 37 60 44 96 56 65 66 56 79 43 58 75 64 73 37 47 56 67 78 87 43 44 59 56 88 65 78 46 66 50 55 58 87 54 47 34 79 43 89 74 56 76 53 48 27 57 75 56 75 37 46 34 79 77 87 63 37 78 25 97 74 58 84 53 48 56 76 56 55 53 37 49 25 57 65 87 45 37 47 24 67 57 75 56 44 69 64 76 56 87 63 35 47 55 77 78 67 45 34 48 46 99 77 65 55 37 47 44 80 68 75 67 66 66 25 77 78 87 45 34 48 55 89 86 58 43 53 80 33 67 78 75 76 76 50 24 68 58 75 75 66 48 24 60 88 86 66 76 78 56 57 75 94 64 57 60 23 60 55 78 47 66 50 24 77 56 87 86 53 57 63 58 56 78 46 35 57 63 60 55 56 46 37 47 53 57 56 87 45 57 49 25 59 87 58 64 43 76 24 60 94 56 77 63 50 47 89 74 56 45 75 67 55 89 75 78 57 37 47 26 58 55 58 43 65 50 36 77 56 87 86 54 79 44 88 65 84 66 44 67 47 80 65 55 44 44 79 44 96 56 95 63 37 78 25 77 78 87 45 34 48 55 89 77 75 45 65 67 47 89 74 56 53 37 56 25 80 87 58 77 65 59 43 67 55 65 56 66 48 24 60 54 87 63 35 46 34 69 87 86 84 53 67 36 76 75 87 44 35 69 34 89 56 86 53 67 59 43 60 54 75 76 54 78 47 60 95 54 47 34 79 43 58 54 75 44 65 79 56 77 64 56 57 54 86 25 80 87 58 76 53 48 53 90 66 77 64 46 67 43 67 94 56 46 34 57 64 80 88 84 47 57 79 43 58 55 56 56 37 47 26 88 58 54 76 53 48 36 67 86 56 53 44 49 25 77 78 67 47 67 47 56 68 88 87 53 37 47 25 58 86 84 45 46 67 34 79 77 97 77 63 50 47 89 74 56 44 35 76 27 57 87 86 53 44 49 25 89 58 64 45 36 80 24 77 78 68 76 53 48 53 57 58 68 44 35 78 55 60 54 87 63 35 67 47 96 56 86 76 54 60 34 89 75 58 67 45 89 56 76 56 64 54 57 89 26 58 87 56 56 66 67 63 58 86 95 63 37 87 25 57 56 95 47 34 68 44 80 68 88 67 36 48 24 66 97 57 64 34 48 36 89 75 58 67"
	cipher = [int(i) for i in cipher.split(" ")]
	alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	def fill_key(key):
		key = list(key)
		for letter in alphabet:
			if not letter in key:
				key+=letter
		return "".join(key)
	if int(input("What do you want to do?\n\n0 - Decrypt with key\n1 - Decrypt with Hill Climbing\n\n")):
		shift_key = find_shift_key(cipher)
	#	exit(" ".join([str(i) for i in shift_nihilist(shift_key, cipher)]))
		text, polybius_key = HillClimb.hill_climb(
			decrypt_nihilist,
			shift_nihilist(shift_key, cipher),
			lambda x:x,
			alphabet,
			lambda best_fitness, time, polybius_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nShift Key (as numbers): {', '.join([str(i) for i in shift_key])}\nShift Key (as text): {convert_shift_key(polybius_key, shift_key)}\nPolybius key: {polybius_key}\n\nText decrypted with key:\n\n{decryption}"),
			modify_key
		)
	else:
		polybius_key = fill_key(input("Please enter the polybius key:\n\n"))
		if input("What format is the shift key in?\n\n0 - Numbers\n1 - Letters\n\n")=="1":
			shift_letters = input("What is the shift key? (as letters)\n\n").upper()
			shift_key = convert_shift_key(polybius_key, shift_letters)
		else:
			shift_key = [int(i) for i in input("Please enter the shift key (as numbers seperated by commas)\n\n").replace(" ", "").split(",")]
			shift_letters = convert_shift_key(polybius_key, shift_key)
		text = decrypt_nihilist(polybius_key, shift_nihilist(shift_key, cipher))
	if len(input(f"\033[H\033[JShift Key (as numbers): {', '.join(str(i) for i in shift_key)}\nShift Key (as text): {convert_shift_key(polybius_key, shift_key)}\nPolybius key: {polybius_key}\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)