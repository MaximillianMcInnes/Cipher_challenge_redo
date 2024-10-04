import HillClimb
from math import inf
from array import array
from random import random, randrange, choices
from copy import deepcopy
import Fitness

ngram = 4
Fitness.init(ngram)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = Fitness.filter_text("""R zbbbnjh nd njbfj Tbhj/Tdhrj nd b lprnj bn b prnp-fxbll pdnjx hdtbndtb. Npj ldjn dl fxbfj dbxx b dbbv fdpxh blldjh, bbh R fdpxhb’n lnbx npjjj zxljxl, jrjb rl R tbl db jvfjbljl. R nprbv rn tdpxh pbrj djjb njzfnrbn lbnj bbxtbx. Rl R fbb lrbh Tdhrj, R bz lpjj lpj fbb lrbh zj. Ldzjnprbn rb pjj xjnnjj njxxl zj lpj bxjjbhx pbl. Rb bbx fblj, R hjfrhjh nd vjjf b xdbn nbrx db pjj, rl dbxx nd brdrh lfddvrbn bbxdbj jxlj tpd zrnpn dj ldxxdtrbn pjj. R bz ldfplrbn db rbnjjfjfnrbn pjj fdzzl trnp Xxbb Ljbbv. Npjx bjj lnrxx plrbn lbrjxx xrnpn jbfjxfnrdb, bbh rn rl jblrjj nd njn bffjll nd Zl Ljbbv’l dllrfj npbb rn tdpxh dj nd rblrxnjbnj Tdhrj’l jddz bn npj pdnjx. Npdlj fxbfjl nbvj npj ljfpjrnx dl npjrj fxrjbnl jrjb zdjj ljjrdplxx npbb npj dbbvl. Npj bnnbfpjh xjnnjj lpdtl npbn Tdhrj rl njnnrbn zdjj fbpnrdpl, dpn rn bxld ljjzl nd dj bb rbrrnbnrdb nd njn rbrdxrjh. R bz bdn lpjj tpjjj nd nd ljdz pjjj. Bl Tdhrj lbxl rb npj xjnnjj, npj bpzdjjl rb npj lrnb-rb dddv lpnnjln ldzjnprbn dhh, dpn pbxrvj Tdhrj R tdb’n pbrj bffjll nd npj rbpxn nd fpjfv rn. Rl lpj prbnrbn npbn tj lpdpxh njbz pf, dj tbjbrbn zj npbn lpj vbdtl R bz pjjj bbh lpdpxh vjjf btbx? (Rl xdp bjj bdn lpjj tpbn R bz nbxvrbn bddpn, nbvj b rjjx fbjjlpx xddv bn xdpj hjfjxfn dl pjj xjnnjj. Xdp lpdpxh lrbh b prhhjb zjllbnj.) Dx npj tbx, npjjj rl ldzjnprbn bbnnrbn bn zj npbn R fbb’n hprnj fxbfj. Npjjj rl b bbzj rb npj lrnb-rb dddv npbn, rb zx pjbh bn xjbln, rl fdbbjfnjh rb ldzj tbx nd npj bbzj dl npj dbbv, bbh R fbb’n jjzjzdjj tpbn npbn fdbbjfnrdb rl. Zbxdj rn rl bdn rzfdjnbbn, dpn R tdb’n lxjjf fjdfjjxx pbnrx R fbb lrnpjj rn dpn. Dbfj xdp pbrj fjbfvjh Tdhrj’l xjnnjj, pjbh drjj nd npj fblj lrxjl bbh nbvj b xddv bn npj lrnbbnpjjl. Zbxdj xdp fbb lrnpjj rn dpn ldj zj. Pbjjx""").upper()
#cipher = Fitness.filter_text("""GFLLKILLJEAFHCJIEEBCHIEAFABCFKCBEAFLCCJEAFBCDEFICLBCCCHBCBCEBCLKCEHCBCEAILCCJBDGBHDABILLEFBAEFIHCBLBIEJDECFGCECJBCBCKCEIEIEECLCJBCBDEAFIAJDCAGIBLFBLDCCBFFHABIAFGCECJJDBCLALKIBFHIDIABIKCEJCEBCEAIBCJIBFJEJIFBIGLDHGECFIABCGFHEEEBCCMGCLACJAFECCFJAEFABDEGLDCCFECHIEAFFCECCEABCJDGEDIDCJLIJKHBFHCAIEECIEJIICHFABCBHCLLJBCEECJHFHCEHBFLFEKCBECJDELFHAFECEHDABCILBFABCBJDJEFALFFCLDCCGFLLKEDJCIFIEBFGGDBLEIEECELIJKLFEJJLACJABCHAFILDIAIEJABCKEBFAJGAHFEAFBDCEIGIDEABCKLIHCFJADEAFILFKCLKLFJEGDEGBFFHFJAEADLLEFEDGEFIJBCEECEABCLIJKGJEBCJIFJAAFEIEJIEFABCBHFHIEBJBBDCJDEABCEGFLLKHIEELDCEADIDLILLKHCIEJBCJIEJDEIEBFBAADHCIEJHFCBFIHFJCLEHCBCFBFJGBAIFBBCBDEEGCLADFEIEJIGGBFKILABCECHCBCGLILCJJGFEIFBHEIEJCKCBKJCEDBIFLCJCAIDLFIABCGFHEEHIEGFDEACJFJAAFIEECIEJABCGDBLE""")

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

def invert_key(key: dict[str, list[str]]):
	inverted = array("u", (" " for i in range(len(alphabet))))

	for i in key.keys():
		for letter in key[i]:
			inverted[alphabet.index(letter)] = i

	return "".join(inverted)

def modify_key(key: tuple[dict[str, list[str]], tuple[int]]):
	# key = [
	#	0: dictionary of ciphertext character : [list of possible plaintext characters]
	#	1: [list of indexes of which plaintext conversion to choose]
	#	2: max plaintext characters to ciphertext characters
	# ]
	key = deepcopy(key)

	for x in range(rand(1, 3, 10)):
		rand_num = random()

		if rand_num < 0.5:	# Remap a plaintext character
			while 1:
				to_modify = choices(
					symbols_used,
					k = 2
				)

				if (
						(1 < len(key[0][to_modify[0]])) and \
						(len(key[0][to_modify[1]]) < key[2])
					):
					break

			to_modify_lists = [key[0][to_modify[i]] for i in range(2)]

			original_size = len(to_modify_lists[0])
			to_move_index = randrange(original_size)
			to_move = to_modify_lists[0].pop(to_move_index)

			to_modify_lists[1].append(to_move)

			replace_with = randrange(len(key[0][to_modify[0]]))

			for i in range(len(cipher)):
				if cipher[i] == to_modify[0]:
					if to_move_index == key[1][i]:
						key[1][i] = replace_with

					elif to_move_index < key[1][i]:
						key[1][i] -= 1
	#				key[1][i] = randrange(len(to_modify_lists[0]))
				
				# elif (cipher[i] == to_modify[1]) and (random() < 0.5):
				# 	key[1][i] = len(to_modify_lists[1]) - 1
		
		else:	# Swap 2 ciphertext mappings
#		elif rand_num < 0.5:	# Swap 2 ciphertext mappings
			to_modify = choices(
				tuple(key[0].keys()),
				k = 2
			)

			to_swap = [
				randrange(len(key[0][to_modify[i]]))
				for i in range(2)
			]

			key[0][to_modify[0]][to_swap[0]], key[0][to_modify[1]][to_swap[1]] = \
			key[0][to_modify[1]][to_swap[1]], key[0][to_modify[0]][to_swap[0]]

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

		trimmed_key[1] = key[1][
			trimmed_indexes[0]:
			trimmed_indexes[1]
		]

		for replace_with in range(len(key[0][cipher[char_index]])):

			trimmed_key[1][char_index - trimmed_indexes[0]] = replace_with

			fitness = Fitness.cal_fitness(
				decrypt_polyphonic(
					trimmed_key, trimmed_cipher
				)
			)

			if best_fitness < fitness:
				best_fitness = fitness
				best_replace_with = replace_with

		key[1][char_index] = best_replace_with

	return key

def decrypt_polyphonic(key: list[dict[str, list[str]], tuple[int]], cipher):
	text = array("u")
	for i in range(len(cipher)):
		text.append(key[0][cipher[i]][key[1][i]])

	return "".join(text)

if __name__ == "__main__":
	from clipboard import copy
	from wordninja import split

	plain_per_ciphertext = len(alphabet) / len(symbols_used)

	starting_key = [
		{},
		[0 for i in range(len(cipher))],
#		3
		26
#		int(input("What is the maximum number of characters that can be represented by each ciphertext character?\n\n"))
	]

	for i in range(len(symbols_used)):
		starting_key[0][symbols_used[i]] = [alphabet[i]]
	
	starting_key[0][symbols_used[0]].extend(alphabet[i+1:])

	text, best_key = HillClimb.threaded_hill_climb(
#	text, best_key = HillClimb.hill_climb(
		decrypt_polyphonic,
		cipher,
		lambda x:x.copy(),
		starting_key,
		lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nInverted key: {invert_key(best_key[0])}\n\nText decrypted with key:\n\n{decryption}"),
		modify_key,
		iterations = 10000,
		same_key = True,
		fitness_ngram=ngram,
		adaptive_iterations = True,
		end = False
	)

	if len(input(f"\033cInverted Substitution table:\n\n{alphabet}\n{invert_key(best_key[0])}\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)