import HillClimb
from math import inf
from array import array
from random import random, randrange, choices
from copy import deepcopy
import Fitness

ngram = 4
Fitness.init(ngram)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = Fitness.filter_text("""QZAGUXPRKKVNFOTAPQBUWNQNVUWMAODHPAWMROHKFMBOCOBNJYUJWHRNOSOKNPAVQWNVUJRNUSWQAHMWPYAVOFUPRWRQWOFMBUPSSOPNJRCHRPBGUPYTYQPGMCTVPSQLAUSXUHWCNGUKNQSNJWCGQHRNMCUSQXQIOGQAUJAQXGYHCHOUJWAGUJWAOSRPNHQWQDXKXQNGPKXGPAGEQWWUHPKMWPRTUFVNVPYPNASQLNHMRXONIOUWJWWJMJUVQDPRJDYKMXOAJXUKMMUBDUQBBPTHQDUJZZOBORTOKHRBMJWNMCMJURQRWEUABQTHPYUHZCOBUWTUKJRBMJWAMZMJOIIHYYQDIQKPXUQNIQSRJNGFVNTQDQANBQTAJMWXONRUORHWUHAJWVQDKQDDTMWNSQKNKPDDLQFGYUZJNJUPPSUZQTTPKUWQRAVHKKJWDYUPAQDURGJDOMRUCUAKPPWMRGOSUOYPONGULMWZYJLNIGJTVOQLGRUINMSWCOWOSQNJQRLQWRQAXVARQDOPCQJRPNAGUWJTNQAHQWQCNVOQCUKQRNVHKTBQRUOWPTOWUNBJWCJWAVQNQXUBJTPRUDUXOWNNQIVHLGNVUUHTAQNJQWQZNGOPDUPFOQWPSODPAHMOYERQAVHWCPWUAGOIUPDAGQZAVOUSQXQAJLZJOYWXUTMFUKMXAHQVPJNJPTTBJQVPNVUBUZMBUAVQAJNVQPNUOWPMYHNNDONMTTGUUHAVQKNOORUWNOBOWXTARMNMOSECPSAGOCSUQNSTPKJQWPWUZSOWTVRQAUDJPNPRHAVAVUJSLMRLUWABPAJMRQWNGOYHZOJXXUWHQNODESMTWWNGOXHRNGOFPHWJCWMBUJAAGOUWDDHPGGQAURMSHOWHAPYJANYUNTARQAMZAOWPRWWMAIHAGFTTVJRPJDVAAVONSVNGKOUFPNMNUNGQNNVUUTSMGUQRWQNJQWKIHNVAGOHSPASQWDYHROPQZLDOQAQCUVPMOWHZCJLTDNEJRVWUUSKNQWWJWDUPTVMNVUBIVHYUAVUKTWUOSKAQWWPXUBJLPRMAPAPDDKNOUBUWQRWWKUUHRNVUHBMRRWQNJQWQDGSOBMKPUKPJMRKNGOESOCQBUMNGUBRQNJQWQYBSUBQKKUPPHMWPIJAGJRUJCZUSORTUPXQYOXOWNQBVMPAJDJAEAGOBUQBUUZLOGNHQWKNQNGHKKAPAUFOWNMCTMTSKOJPGUPSMWDKMZCOWOSQDAOWWURTJOKNGOASORWQZOMOWNPPHWLOAVURQSUAUWXQSUAGQRAVUIQSJAKOYZXSHWCPVQXUAMTPNGUZPLNAVPAAVUOTSMGUPWFJWWHPABJXQD""")

def remove_repeats(x):
	filtered = array("u")
	for i in x:
		if i not in filtered:
			filtered.append(i)
	return filtered

symbols_used = remove_repeats(cipher)

def rand(start_num, x = 1, y = 5):
	while randrange(0, y + 1) <= x:
		start_num += 1
	return start_num

def modify_key(key):
	# key = [
	#	0: dictionary of ciphertext character : [list of possible plaintext characters]
	#	1: dictionary of plaintext character : number of mappings to ciphertext characters
	#	2: [list of indexes of which plaintext conversion to choose]
	#	3: maximum plaintext mappings
	#	4: maximum ciphertext mappings
	# ]
	key = deepcopy(key)

	for x in range(rand(1, 3, 10)):
		rand_num = random()

		if rand_num < 0.33:	# Add a new mapping
			while 1:
				to_add_to = choices(
					symbols_used,
					k = 1
				)[0]

				to_add = choices(
					alphabet,
					k = 1
				)[0]

				if (
						(key[1][to_add] < key[3]) and \
						(len(key[0][to_add_to]) < key[4])
					):
					break
			
			key[0][to_add_to].append(to_add)
			key[1][to_add] += 1

		elif rand_num < 0.66:	# remove a mapping
			pass

		else:
			pass

	trimmed_key = key.copy()	# Find the best mapping for each ciphertext character in the text

	for char_index in range(len(cipher)):

		best_fitness = -inf
		best_replace_with = 0

		trimmed_indexes = (
			max(0, (char_index - (ngram - 1))),
			min(len(cipher), (char_index + ngram))
		)

		trimmed_cipher = cipher[
			trimmed_indexes[0]:
			trimmed_indexes[1]
		]

		trimmed_key[2] = key[2][
			trimmed_indexes[0]:
			trimmed_indexes[1]
		]

		for replace_with in range(len(key[0][cipher[char_index]])):

			trimmed_key[2][char_index - trimmed_indexes[0]] = replace_with

			fitness = Fitness.cal_fitness(
				decrypt_polyphonic(
					trimmed_key, trimmed_cipher
				)
			)

			if best_fitness < fitness:
				best_fitness = fitness
				best_replace_with = replace_with

		key[2][char_index] = best_replace_with

	return key

def decrypt_polyphonic(key: list[dict[str, list[str]], tuple[int]], cipher):
	text = array("u")
	for i in range(len(cipher)):
		text.append(key[0][cipher[i]][key[2][i]])

	return "".join(text)

if __name__ == "__main__":
	from clipboard import copy
	from wordninja import split

	plain_per_ciphertext = len(alphabet) / len(symbols_used)

	starting_key = [
		{},
		{i:1 for i in alphabet},
		[0 for i in range(len(cipher))],
		26,
		3
#		int(input("What is the maximum number of characters that can be represented by each ciphertext character?\n\n"))
	]

	for i in range(len(symbols_used)):
		starting_key[0][symbols_used[i]] = [alphabet[i]]
	
	starting_key[0][symbols_used[0]].extend(alphabet[i+1:])

	text, best_key = HillClimb.threaded_hill_climb(
#	text, best_key = HillClimb.hill_climb(
		decrypt_polyhomophonic,
		cipher,
		lambda x:x.copy(),
		starting_key,
		lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\n\nText decrypted with key:\n\n{decryption}"),
		modify_key,
		iterations = 10000,
		same_key = True,
		fitness_ngram=ngram,
		adaptive_iterations = True,
		end = False
	)

	if len(input(f"\033cText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)