
from random import randrange
from HillClimb import threaded_hill_climb
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
def find(to_find, to_find_in):
	try:
		index = to_find_in.index(to_find)
	except ValueError:
		exit(f"Could not find {to_find} in {to_find_in}")
	return index//5,index%5
#	return index%5,index//5
def get_coords(key, chunk):
	nums = []
	for letter in range(len(chunk)):
		nums.append("".join(str(i) for i in find(chunk[letter], key)))
	return "".join(nums)
def convert_coords(coords):
	mid = len(coords)//2
	new_coords = [coords[i]+coords[i+mid] for i in range(mid)]
	return "".join(new_coords)
def decrypt_bifid_chunk(key, chunk):
	coords = convert_coords(get_coords(key, chunk))
	text = [key[(int(coords[i])*5)+int(coords[i+1])] for i in range(0, len(coords)-1, 2)]
	return "".join(text)
def decrypt_bifid(key, cipher):
	# key = [
	# 0: period
	# 1: key
	# ]
	text = []
	for i in range(0, len(cipher), key[0]):
		text.append(decrypt_bifid_chunk(key[1], cipher[i:i+key[0]]))
	return "".join(text)
def modify_key(key):
	period = key[0]
	key = list(key[1])
	letters_to_swap = (						# swap 2 random letters in the key
		randrange(len(key)),
		randrange(len(key))
	)
	key[letters_to_swap[0]], key[letters_to_swap[1]] = key[letters_to_swap[1]], key[letters_to_swap[0]]
	return period, "".join(key)

if __name__ == "__main__":
	from wordninja import split
	from clipboard import copy
	from Fitness import filter_text
	cipher = filter_text("GDYFYVBKHRPECOYHKZVUAYMGVHCWHGRAFAZKPYDSKCHDYIDQZLENGGBFMYVAOGZAHOKDOXZKNWRHLIAYCYHGWNHELVRDFAVELNBONZDFRAWAUDVOKGEBIVWRFRADZXWUERMCLCWWTORZEFKLZEXRFYIFQXCWDECYSEAEDGRBFHNFURUNVERGFHKZZYPQNDOWOEUWIXBROFCYBIAQDNHPESLVADUHTMVDTGEBUBYEEOEVEFGBDYAYHSFSYCBWVETLAIOIPSECYFBZATFEHDBVWKSCLFFYDYDZUNHONODBOUDMTSRZYPKNULRRWUIHAPSLKQNRTEOLEYBDYAZIABCNWRUCRFTVRBVMMSDDWZYFECUBRMVNTNBKAAPKYANHTMYCDNYENORITBRHNASVMLSBOFVAUURVWRGMAYRECTSKCVEKOOUUDKYIKQDCFWXSRNESHGWEYOEAHTNFMEUXNTERNYQWEZETSMCOWVORGAPOPGCOTEMBDPDLKAQDSCQOCUAYGQSGYOEUBEHUFKNEPOQXTFTYYSGVVWKGOSFDYBWPOZOCPTRMHMYNYOGZAHEGELEDWVAUHWUDTEBDAZFCHDCWYEZQHLBZKOWVOTGOWTOVCRHWZHEWWYODDYMSGLBUAKIVDWZYFGHQVNXGKTOSFFYRBTATRUAMYNKNNCLVKRGLDRFLWVPFMNLSAYBHPSSLWKLETVWKLUTYRZHTKVAUFUUTFFEYCYDOVSRYCWHWBFHUXPWGCBGDPGLXPDVSFPBUVSKOWDEZFNWGBVGRNHEIUDHULTFRVDRAIASVNVERGRKRBRWVGTSGFOFBSBCRFIWIUXSFNYAGIZIROVEMQWRCDRFWAXYMYULKFRARCCLMBOGDHGLRDKAAKRWTEATUMUXRRYIOFEYAYHISUOIUWROAZCFOYLEZXFGXQHSCVBHPZSFFAPCPFDPRGRKDEIYEEOEKEBBYSQYAZOEEGYWWLDVOGCCBEAEIUTMKZDFYVXMKRQTOOWGGBLFKYADSCGWRRFAWTSFUYYREMXSFEYAPOLLCACEHGWOGCDLYYOCWRZBFFWADDYVOKGOEDNOIEQUGRGETZUMGOBYHQSVUHNSSLFAYDERNTHUSMLCUHNLNVWKGEBVPRMYCEHGARARAVYFLXDOGHYKWEFCYKXLMEYZCMNWYOGAYMVNVOMGCVOFLDHFPPVKOGLCFEIEXQBEAONFDYUYPDSVNFUDRNFZLTYQOOCWYWZGRPKCLPPHNRERLYPLEIEVASMSKBFYZZYPFNREECWFCWEOUYPENAOCCAWFULRVFYSANVWMGVAPFNBEFUN")	# QNSMPBDCRAXUZTVWEOKYIGLFH, 5
	def fill_key(combination):
		for letter in alphabet:
			if not letter in combination:
				combination+=letter
		return combination
	#print(decrypt_bifid((5, fill_key("KEYWORD")), cipher))
	#period = 2
	#print("".join(get_coords(alphabet, cipher[i:i+2]) for i in range(0, len(cipher), 2)))
	#exit()
	if int(input("0 - Solve with period and key\n1 - Hill Climb\n\n")):
		print(f"\033[H\033[JThe length of the text is: {len(cipher)}")
		periods=[]
		while True:
			tmp=input(f"Which periods should I try?(exit - to exit)\nPeriods I will try: {', '.join([str(i) for i in periods])}\n\n")
			if tmp=="" or tmp=="exit":
				if periods==[]:
					print("There must be at least one period chosen.")
				else:
					break
			elif tmp.isdigit():
				if 1<int(tmp):
					if int(tmp) in periods:
						periods.remove(int(tmp))
					else:
						periods.append(int(tmp))
			else:
				tmp = tmp.split("-")
				for i in range(max(int(tmp[0]), 2), int(tmp[1])+1):
					if i not in periods:
						periods.append(i)
			periods.sort()
		del tmp
		text, key = threaded_hill_climb(
			decrypt_bifid,
			cipher,
			lambda x:x,
			[(period, alphabet) for period in periods],
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nPeriod: {best_key[0]}\nKey: {best_key[1]}\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			iterations = 5000,
			adaptive_iterations = 1
		)
	else:
		key = (int(input("What is the period?\n\n")), fill_key(input("What is the grid key?\n\n")))
		text = decrypt_bifid(key, cipher)
	if len(input(f"\033[H\033[JPeriod: {key[0]}\nKey: {key[1]}\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)