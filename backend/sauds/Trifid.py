import HillClimb
from random import randrange
def find(to_find, to_find_in):
	try:
		index = to_find_in.index(to_find)
	except ValueError:
		exit(f"Could not find {to_find} in {to_find_in}")
#	y, x = divmod(index, 5)
#	return 0, y, x
#	return 0, x, y
#	return y, 0, x
#	return y, x, 0
#	return x, 0, y
#	return x, y, 0
	flat_index, x = divmod(index, 3)
	z, y = divmod(flat_index, 3)
	return z,y,x

def get_coords(key, chunk):
	nums = []
	for letter in range(len(chunk)):
#		print(chunk[letter], find(chunk[letter], key))
		nums.append("".join(str(i) for i in find(chunk[letter], key)))
	return "".join(nums)

def convert_coords(coords):
	mid = len(coords)//3
	new_coords = [coords[i]+coords[i+mid]+coords[i+(mid*2)] for i in range(mid)]
#	split_coords = [coords[i:i+mid] for i in range(0, len(coords), mid)]
#	print(split_coords, len(split_coords[0]))
	# new_coords = []
	# for i in range(mid):
	# 	new_coords.append(coords[i]+coords[i+mid]+coords[i+(mid*2)])
	return "".join(new_coords)

def decrypt_trifid_chunk(key, chunk):
	coords = convert_coords(get_coords(key, chunk))
#	text = [key[(int(coords[i+1])*5)+int(coords[i+2])] for i in range(0, len(coords)-2, 3)]
	text = [key[(int(coords[i])*9)+(int(coords[i+1])*3)+int(coords[i+2])] for i in range(0, len(coords)-2, 3)]
#	text = [key[(int(coords[i])*9)+int(coords[i+1])+(int(coords[i+2])*3)] for i in range(0, len(coords)-2, 3)]
#	text = [key[(int(coords[i])*3)+(int(coords[i+1])*9)+int(coords[i+2])] for i in range(0, len(coords)-2, 3)]
#	text = [key[(int(coords[i])*3)+int(coords[i+1])+(int(coords[i+2])*9)] for i in range(0, len(coords)-2, 3)]
#	text = [key[int(coords[i])+(int(coords[i+1])*9)+(int(coords[i+2])*3)] for i in range(0, len(coords)-2, 3)]
#	text = [key[int(coords[i])+(int(coords[i+1])*3)+(int(coords[i+2])*9)] for i in range(0, len(coords)-2, 3)]
	return "".join(text)

def decrypt_trifid(key, cipher):
	# key = [
	# 0: period
	# 1: key
	# ]
	text = []
	for i in range(0, len(cipher), key[0]):
		text.append(decrypt_trifid_chunk(key[1], cipher[i:i+key[0]]))
	return "".join(text)

def modify_key(key):
	period = key[0]
	key = list(key[1])
	letters_to_swap = (						# swap 2 random letters in the key
		randrange(len(key)),
		randrange(len(key))
	)
	key[letters_to_swap[0]], key[letters_to_swap[1]] = key[letters_to_swap[1]], key[letters_to_swap[0]]
	return (
		period,
		"".join(key)
	)

if __name__ == "__main__":
	from wordninja import split
	from clipboard import copy
	cipher = "CEUE_ZRJXRBCDGUDI__CPSONJTNGDCVGMZQSEAAZOBXTBOKURVYTZHPNFDVQSWBZVAVVGLDQYWNBFMUQSQAMQDZZJTPVGXMIZOVYGATQVIWNUTGYAYZOYWTWV_HZBGSUMRRRXTVBGUYEXRGXIU_NMXGEBFQMWLQJ_OPYTTMJQNPAHQGAYZJODXZSGF_VONGQYOZHBWDXPQBQDCATU_WV_RAAANUSTUGKMOEZHWIUSV_DZGWNETNHZL_JLLGOBFZFJVDNVVLMXAANUYGATQVGJIAWYK_WZCDHUVTQGPLCATU_GZSFXGQDQZG_DIXMIFHEJ_DNXWPSXM_CUBEPNAMWFQNIZNCURETGR_CSNT_NGCJULT_SNCX_JDNQF_EQBPS__KQSHXIMFQYPLYAJTYUAMZRJXRSGXMQIFQVWODPVRTZGCLBTVHAXHSBLYQEBED_ZGTT_U_GJO_VVKDLXNYFAQQSQDAZRK_RZCDHUVJUZJPNFDVQSLAMTZBONOGY_KZZBHXRPCWEUNPMKQ_CLLUDQUNJXRJLUC_KZNLOUVR_ESYVQRXZZKQGJNIZOVYCSJZB_EMWQPNNBNWZSILBXWVBRUZJPALQRWCQOEQ_RNPVD_XSNYOBFQVXWDNYLZTVOMNQYEEDZOSDBZVCXRODEZLMC_DU_RFZDQYTMGPJRUZJPDDZRVZKQNJVMZUVUFJKLP_O_JGATQVWYTTUY_DGZHXKNLYD_TVUKWXWTZSWNAQVJLIZ_HDYQANQ_JOBWBDUSRTZMPGBVJMALDTVRGPRZAG_DNZLONTLAKQBBZLHPGIZMESTROZUZBHXRGPQOQBEU_AHAPRJS_SMXCUYEXEAPZYNMMTVINFIP_RRXLMZRRBWQSIMNCUJESPAMQAAVJRDDQJUT_O_GBGUREKQGVZY_IZGWZMPGYUSE_OMLU_RMZVVCQ_QA__WBLIOOTJT_XLLPYCDHS_U_GMEVVWVVV_BOYLUWQN_ZYTQGPLDHMTHXC__LZYHLRDKTJRBTQJQJB_PVCXROBSOFJASTYMZNGUBEZRBLOL_GLCVYMMQCBQXNCUJQAWSSJZNCUREPGCNGVZHUBCQ_QACYGSHDKUNRKTBFAXZUGHTYXZNBCUREDHU_WMBPGTU_NMXAMFUYSQMEQJ_TPNLIUVWNSQSRJNFQSTUGKLMEWHRQB_ZSKPYQ_WKOOMPSGLLYZSMA_DQSVDKFRNWZSRNGFJQCPSS_MW_SLLBEPRUTBIXGNEMHQYQDDZQUBMZNCUREAWS_RXEZYZYNAHTQ_NMXFAOQNEZNHXCZYE_GFJQCTSMDMQBAMUJPMLQGWMZVP_SNXGODQVDNTSJTQGKMPJWFQSWBZVDNTSJGDIENAPVJLIZ_WDQMZRRNFUYEPGPLGBPRXA_XTNMRJZTVZBHXRCNBILHUSILDSGVMTYW_UZOUSWCAXTNTACPNWWUGCYQMHQPVVLM_EQGAPCRESU_NMXGZAEVZBILOJLMXVGACQRYTJZLCUYWLIO_VUROZJXKUSHMTC_XLT_EBGSG_MQXMTSJTDU_GSCMAQYZDZ_GIFQRMKQNJSRZMPLUGWLFZHGLGVSUXKIFURMKQNJKAVQSSQLEZOLLU_YPJZMXF_YQUFRKEALV_NTZGKNQHJYNTRJNFE"	# KEYWORD
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
	#alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

	def fill_key(combination):
		for letter in alphabet:
			if not letter in combination:
				combination+=letter
		return combination

	#print(decrypt_trifid((5, fill_key("KEYWORD")), cipher))
	if input("What do you want to do?\n\n0 - Hill climb\n1 - Solve with key\n\n")=="1":
		key = (int(input("What is the period?\n\n")), fill_key(input("What is the key?\n\n")))
		text = decrypt_trifid(key, cipher)

	else:
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

		text, key = HillClimb.threaded_hill_climb(
			decrypt_trifid,
			[cipher for i in range(len(periods))],
			lambda x:x,
			[(period, alphabet) for period in periods],
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nPeriod: {best_key[0]}\nKey: {best_key[1]}\nText decrypted with key:\n\n{decryption}"),
			modify_key
		)

	if len(input(f"\033[H\033[JPeriod: {key[0]}\nKey: {key[1]}\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)