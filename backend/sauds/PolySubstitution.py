# It may not give a perfect answer, but a good enough one
import HillClimb
from array import array
from random import shuffle, randrange, choice
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rand(start_num, x = 1, y = 5):
	while randrange(0, y + 1) <= x:
		start_num += 1
	return start_num

def invert_key(key):
	inverted = [["" for j in range(26)] for i in range(len(key))]
	for j in range(len(key)):
		for i in range(26):
			inverted[j][i] = alphabet[key[j].index(alphabet[i])]
	return inverted

def fill_key(combination):
	for letter in alphabet:
		if not letter in combination:
			combination+=letter
	return combination

def remove_repeats(x: list):
	filtered = array("u")
	for i in x:
		if i not in filtered:
			filtered.append(i)
	return filtered

def generate_custom_key(cipher: list[str]):
	grams = {}
	letter = 0
	for i in range(len(cipher)):
		if cipher[i] not in grams.keys():
			grams[cipher[i]] = alphabet[letter]
			letter += 1
	return grams

def modify_key(key: list[list[str]]):
#	key = deepcopy(key)
	key = key.copy()
	for i in range(rand(3, 1, 10)):
		key_to_randomise = randrange(len(key))
		key[key_to_randomise] = array("u", key[key_to_randomise])
		while 1:
			letters_to_swap = (						# swap 2 random letters in a random part of the key
				randrange(len(key[key_to_randomise])),
				randrange(len(key[key_to_randomise]))
			)
			if letters_to_swap[0] != letters_to_swap[1]:
				break

		key[key_to_randomise][letters_to_swap[0]], key[key_to_randomise][letters_to_swap[1]] = \
		key[key_to_randomise][letters_to_swap[1]], key[key_to_randomise][letters_to_swap[0]]

		key[key_to_randomise] = "".join(key[key_to_randomise])

	return key

def encrypt_polysubstitution(combination: list[list[str]], cipher: str):
	text =	array("u")
	for index in range(len(cipher)):
		letter = cipher[index]
		ordinal = ord(letter)

		if letter.isupper():
#		if 64<ordinal<91:
			text.append(combination[index%len(combination)][(ordinal-65)])

		else:
#		elif 96<ordinal<123:
			text.append(combination[index%len(combination)][(ordinal-97)].lower())

#		else:
#			text.append(cipher[index])
	return "".join(text)

def encrypt_custom_alphabet_polysubstitution(grams: list[dict[str,str]], cipher: list[str]):
	text = array("u")
	columns = len(grams)
	for i in range(len(cipher)):
		text.append(grams[i%columns][cipher[i]])
	return "".join(text)

def modify_custom_key(grams: list[dict[str, str]]):
	grams = grams.copy()
#	grams = deepcopy(grams)
	for i in range(rand(3, 1, 10)):
		key_to_randomise = randrange(len(grams))
		grams[key_to_randomise] = grams[key_to_randomise].copy()
		while 1:
			grams_to_swap = (
				choice(tuple(grams[key_to_randomise].keys())),
				choice(alphabet)
			)
			if grams[key_to_randomise][grams_to_swap[0]] != grams_to_swap[1]:
				break

		tmp = grams[key_to_randomise][grams_to_swap[0]]
		grams[key_to_randomise][grams_to_swap[0]] = grams_to_swap[1]
		count = 0
		for key in grams[key_to_randomise].keys():
			value = grams[key_to_randomise][key]
			if value == grams_to_swap[1] and key != grams_to_swap[0]:
				grams[key_to_randomise][key] = tmp
	#			break
				count += 1
		if count > 1:
			raise Exception(f"Double mappings found in {grams} when setting {grams_to_swap[0]} to {grams_to_swap[1]}")

	return grams

if __name__ == "__main__":
	
	from copy import deepcopy
	import sys, os
	sys.path.insert(0, os.path.realpath(__file__).replace("pypy\\"+os.path.basename(__file__),"CPython"))
	from clipboard import copy, paste
	from wordninja import split
	from Fitness import filter_text

#	text = """97 26 57 58 105 68 57 69 58 35 58 73 88 58 79 45 74 98 104 110 56 80 26 36 97 106 69 75 100 28 54 58 63 108 95 67 39 35 87 102 89 98 78 28 68 57 85 68 67 100 48 46 68 96 67 97 106 49 36 79 64 88 75 106 67 76 58 63 109 78 106 69 74 100 74 89 85 78 48 78 87 96 67 57 67 48 46 68 96 67 98 89 69 37 58 102 107 99 69 45 46 90 85 78 77 69 38 54 57 64 67 96 67 26 78 68 65 77 68 70 29 37 58 74 69 68 68 55 74 68 84 106 99 106 37 45 79 105 90 95 78 65 37 100 74 69 57 106 39 57 98 106 67 75 88 28 36 97 82 106 67 100 65 46 67 85 77 67 69 27 57 100 93 108 56 110 69 37 77 104 106 79 68 48 36 96 63 77 79 79 37 46 59 95 67 67 100 26 36 76 63 100 78 80 26 45 60 63 110 67 96 28 78 67 102 97 56 68 48 58 98 63 67 87 98 28 36 68 86 79 95 108 56 74 100 95 89 68 110 65 44 69 63 96 58 108 67 35 86 74 106 58 110 28 66 58 85 68 56 89 69 65 96 105 70 58 68 37 57 100 74 86 58 68 66 45 79 106 97 95 86 28 47 98 93 100 78 80 26 58 57 63 110 86 67 26 38 98 84 77 78 97 56 35 100 63 97 67 69 67 37 67 63 106 67 106 45 57 67 74 69 68 96 59 35 87 86 88 77 69 38 36 59 94 98 56 68 37 37 99 85 107 56 106 37 57 86 65 110 86 106 37 74 59 106 69 87 78 59 35 87 65 110 78 78 65 37 100 74 100 78 78 65 45 90 65 79 97 97 55 37 100 74 106 99 79 26 46 59 86 67 56 109 29 76 59 84 67 86 89 36 46 90 63 96 68 68 48 46 59 64 90 68 78 37 68 57 105 89 99 69 27 74 67 105 88 89 69 68 35 79 73 86 56 108 67 57 67 105 88 75 69 27 75 60 104 89 85 67 48 78 87 102 78 87 67 26 76 67 64 106 88 100 37 46 90 85 78 67 100 65 45 96 105 70 58 68 37 57 100 74 96 58 108 67 35 86 74 106 58 110 28 66 58 85 68 56 90 28 37 97 73 77 89 69 38 76 87 64 67 98 89 65 78 90 63 68 56 106 69 38 58 102 80 78 78 26 68 79 106 97 66 86 59 35 58 63 106 85 89 69 64 79 64 67 87 69 27 74 68 66 68 58 70 26 36 98 84 106 78 109 36 37 58 64 88 67 69 59 35 79 64 78 89 89 37 56 59 75 86 95 108 67 58 57 82 106 67 100 56 36 79 82 106 99 99 57 36 59 105 78 89 67 27 57 86 63 98 58 68 58 37 70 63 68 99 69 27 57 67 102 107 99 69 45 46 90 85 78 75 89 36 57 86 96 67 57 106 36 68 57 93 89 98 90 65 46 96 65 110 95 89 68 45 69 64 67 77 69 38 54 59 75 108 86 100 48 48 57 94 106 97 108 26 65 68 96 67 57 69 67 35 76 102 78 89 97 65 45 68 102 110 85 78 65 37 100 86 79 67 78 59 35 58 63 86 95 108 67 58 57 65 78 89 67 27 54 79 84 77 67 69 36 35 58 76 67 78 110 56 74 68 96 106 99 107 47 37 69 85 68 56 68 65 67 90 74 78 89 89 37 46 90 63 77 67 68 48 78 89 63 97 56 89 37 68 59 94 77 67 89 69 76 57 84 106 66 108 26 45 76 65 79 97 97 59 57 70 63 79 99 97 26 36 99 102 110 56 97 47 37 69 64 96 78 109 29 57 96 95 110 75 67 66 78 59 82 86 89 89 37 67 59 73 77 95 70 55 57 100 93 69 95 110 37 68 57 73 109 78 108 67 54 59 64 108 86 69 57 36 90 65 97 56 106 36 76 79 106 97 66 69 55 74 57 74 88 78 110 56 56 59 75 68 58 70 29 37 100 63 110 67 77 45 37 69 104 97 89 89 39 35 68 85 107 56 110 58 36 57 85 78 59 108 26 57 67 75 68 56 106 69 45 60 63 96 68 108 48 46 96 106 99 58 110 37 68 57 75 110 56 87 29 76 79 102 110 56 97 56 35 79 74 100 95 110 47 37 69 64 100 58 109 26 57 67 84 69 68 68 26 44 69 63 77 67 67 56 74 90 85 80 56 96 28 77 60 104 67 67 67 56 77 78 85 79 86 106 37 37 88 74 100 56 108 65 58 58 85 68 77 96 28 78 68 63 110 67 77 48 78 87 102 96 78 110 48 45 67 75 68 56 88 28 47 68 96 89 67 110 28 46 90 102 110 88 106 36 77 96 73 77 95 110 58 57 100 93 110 58 90 28 37 97 73 100 78 80 26 58 57 63 110 89 89 27 77 57 93 106 75 106 67 76 59 94 96 58 79 27 45 57 92 69 99 78 65 78 69 63 78 58 70 27 37 68 63 96 67 78 59 35 99 85 110 86 106 59 37 60 63 88 58 79 45 74 98 104 89 88 68 26 35 68 96 89 67 106 37 74 67 82 69 57 78 59 64 59 106 78 95 110 38 74 100 95 78 58 106 69 48 57 73 78 95 110 37 68 57 92 69 97 108 26 64 68 102 69 99 78 28 67 57 74 100 56 68 45 35 86 85 110 79 79 65 76 87 102 78 95 110 37 37 59 106 67 58 98 37 68 57 94 106 99 67 36 46 79 64 96 89 106 39 35 67 65 98 78 109 26 36 96 92 89 99 108 65 46 57 64 89 67 79 27 35 59 106 78 89 67 26 57 67 74 96 58 89 36 46 96 75 110 86 67 27 45 68 85 110 86 78 59 57 68 84 69 68 68 69 74 57 92 67 99 89 69 64 78 82 106 97 108 49 35 70 102 77 95 78 65 78 89 106 67 76 78 45 35 57 103 89 99 97 65 76 59 65 107 87 69 27 54 79 64 97 67 69 36 35 57 102 110 88 100 26 36 79 95 89 95 110 45 68 96 104 67 66 100 26 65 59 63 77 99 69 37 45 90 85 68 56 69 38 36 98 65 80 56 69 57 66 96 106 67 79 69 28 75 67 73 100 56 96 26 36 68 85 106 99 108 47 76 59 76 67 66 78 59 74 67 96 69 68 77 26 57 100 93 106 78 109 36 47 58 63 77 89 67 45 74 98 104 100 78 80 26 68 57 64 69 75 110 65 65 57 85 77 78 90 28 47 68 96 69 75 78 28 66 58 63 77 89 67 69 74 68 75 70 95 68 26 77 79 102 110 78 108 28 56 79 104 77 56 68 39 57 100 74 78 58 88 28 47 79 106 97 67 69 37 68 57 104 106 79 68 48 36 78 105 89 95 77 65 35""".split(" ")
	text = filter_text("NOGXI AVBUI WVJXS NLBFE CSKMH XLGTI RKCPX FHBAA EAMIR TVDRI VZFAT RUBEX RYRQH KVBAQ POMYI NVPWF VUHMQ ZURMP CTYPK VDYEX FZYKX YLJQE JAYZY EBQGE CUYYI RUBMR ZURQV ELREI RYATP ZUIQH ZARAE JWWRV FTRTI NHPAJ ZUBQT VUBQR TLRTI FYGSM EHJIE JSCMH VYMRX YLAGP GLPDM ENUTM TOBUH EAQQI DSGWI RJMUR TPBQR TLYZH RUMFL VYHGK FMAAJ WLCSE MLKQX ZTCFS VENXS ILRTI CPLWX YLMDM XPLMP TBJBI IYGZK NHQEI KBNNC NHQTM ENRAR RUBFE CSKMH XLRAW GFMZX YLZDM KPQTA RZFUR XAMZL RKQGK XLQFI UAFQR RTCMR UAYWI EPRRV FTAGP GLNQV TVSZX PCGDK ZUGMQ FZRAJ KOCUV RJRUZ ZAGQW NLPQJ FJSEW VKYDS LUBZI NFMDO TPRKA ZAFFL VHEQR KZYZH JWGQW ILADY ZACPJ IVKXS ENGEP RUBMR UJMZR VJRUG LARTI PDMDO VKDAV RIMGX WPTQC VHPEV VWMDX ZUEAR KOCNV ZAGEL KYMAT DVTQQ VUREY JPLSG FKCEE EKQBC TYYRX KVQFE PBLPI KLAFI UHQRE IHQUG FBJPW VLRTI ILUMW EVPQG FYBAJ KOCDM ENMBI IHRUR XPLAV RYMGR UJSXT VWCDA YPATQ RKCEI EZCZS FUCQZ VYATS FZCEE TVBQR RTCOS EUCOX VKUUX YAFQS GLPMX ZVLNY KAFMX CLDFQ VDMZH VYGZK NOWAY IUCIQ IAYXP DHBSI NHQAT VYYFM ENFQV VHLPA YHRFL VFUQV VBNFS FUYIL ZTGEI RYATI UHLZE JTGFL KHJXQ RKEQE EKRTI ILQGP KDYEE JBPBV ZZCNY KZKUX YPQMG FTKAR EHKQE EKGIE JUREY ILGFQ VHLFE EFRTM ENRTI SHLWZ RBJFA RZAXI RYJKM DWMDX RURNY KZGZG VAFQF FECEH ZKLFG FURMM EHLKX YPLSS KOCDX YHLZY DICDW ZAKGW KICFL VJYEI KOYFX YLLGQ SLPEX YLKEI CCCEL RCCMQ VHLUR XPUMW FURAQ PAFUV UQSSS WJMRJ VLZQJ FYCUJ FBLPX YLAGP GLPOS ULZAS BVLXM ELYZH KOGZK JZRMV KLBFS DHIQW VUQQM UBEAY KAFQP ZZRAJ SVVQW RUBZY DICDW KOYFN FKGQL RKEUZ VUKQE EKQFE IACPX FWSFM KAMSI KOCDF LASZJ FYRGR RACXC ABQFE JPZQK RUKKT YVLQV RUEMR UDFQR ZWGOO VKGFY GPFMH ILAQM MLBMR RBBUS DLQEE XLDDS DQMPM VPRIE JPLYS IZCOS ULYZH VUADC GACPM WZFQA RZRMO ZUEFL RAKGG YJYDI KOCZM BUCIA VTSEX SLGZF ZNRDS LIJQ")
#	text = filter_text(paste() if int(input("Where do you want the text to come from?\n\n0 - I want to type it\n1 - My clipboard\n\n"))==1 else input("What is the text?\n\n"))

	mode = int(input("What do you want to do?\n\n0 - Encrypt with randomly generated key\n1 - Encrypt with typed key\n2 - Decrypt with key\n3 - Decrypt with hill climbing\n4 - Decrypt custom alphabet with hill climbing\n\n"))

	# import yappi
	# yappi.set_clock_type("cpu")
	# yappi.start()

	if mode == 0:
		columns = int(input("How many keys should the randomly generated key have?\n\n"))
		best_key = [alphabet for i in range(columns)]
		for j in range(columns):
			shuffle(best_key[j])
			print("".join(best_key[j]))
		text = encrypt_polysubstitution(best_key, text)

	if mode == 1:
		columns = int(input("How many keys does the key have?\n\n"))
		best_key = [fill_key(input(f"Please enter key number {i+1}:\n\n")) for i in range(columns)]
		text = encrypt_polysubstitution(best_key, text)

	if mode == 2:
		columns = int(input("How many keys does the key have?\n\n"))
		best_key = [fill_key(input(f"Please enter key number {i+1}:\n\n")) for i in range(columns)]
		if int(input("What key is this?\n\n0 - The ENCRYPTION key\n1 - The DECRYPTION/inverted key\n\n"))==0:
			best_key = invert_key(best_key)
		text = encrypt_polysubstitution(best_key, text)

	elif mode == 3:		# This can a solve polyalphabetic cipher which uses only alphebical characters
		from IOC import IOC_columns
		columns = IOC_columns(text)[0]
		text, best_key = HillClimb.threaded_hill_climb(
#		text, best_key = HillClimb.hill_climb(
			encrypt_polysubstitution,
			text,
			lambda x:x.copy(),
			[alphabet for i in range(columns)],
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nKey used:\n\n"+', '.join(best_key[j] for j in range(len(best_key)))+f"\n\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			iterations = 6000,
#			iterations = 10000*columns,
			same_key = True,
			adaptive_iterations = True,
			end = False
		)
		inverted = invert_key(best_key)

	else:	# This can solve Nihilist, Vigenere, pretty much anything polyalphabetic (can solve ciphers which don't use letters if each "symbol" is in the list called text)
		from IOC import IOC_columns
		columns = IOC_columns(text, alphabet = remove_repeats(text))[0]
		text, best_key = HillClimb.threaded_hill_climb(
#		text, best_key = HillClimb.hill_climb(
			encrypt_custom_alphabet_polysubstitution,
			text,
			deepcopy,
			[generate_custom_key([text[chunk] for chunk in range(i, len(text), columns)]) for i in range(columns)],
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\n\nMappings used: {columns}\n\nText decrypted with key:\n\n{decryption}"),
			modify_custom_key,
			iterations = 1000*columns,
			same_key = True,
			adaptive_iterations = True,
			threads = 6
		)
		if len(input(f"\033[H\033[JText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
			copy(text)

		# yappi.stop()
		# yappi.get_func_stats().print_all()
		# yappi.get_thread_stats().print_all()

		exit()

	# yappi.stop()
	# yappi.get_func_stats().print_all()
	# yappi.get_thread_stats().print_all()

	inverted = invert_key(best_key)
	if len(input(f"\033[H\033[JKeys used:\n\n"+'\n'.join(''.join(best_key[j]) for j in range(len(best_key)))+"\n\nInverted Keys:\n\n"+'\n'.join(''.join(inverted[j]) for j in range(len(inverted)))+f"\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)