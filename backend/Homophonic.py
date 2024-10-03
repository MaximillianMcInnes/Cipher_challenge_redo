import HillClimb
from array import array
from random import choice
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt_homophonic(key: dict[str, str], cipher: list):
	text = array("u")
	for i in range(len(cipher)):
		text.append(key[cipher[i]])
	
	return "".join(text)

def modify_key(key: dict[str, str]):
	# key = dictionary where ciphertext symbol : plaintext symbol
	key = key.copy()
	index = choice(tuple(key.keys()))
	key[index] = choice(alphabet)

	return key

def key_to_table(key: dict[str, str]):
	table = [[] for i in range(len(alphabet))]
	for i in key.keys():
		table[alphabet.index(key[i])].append(i)

	return table

if __name__ == "__main__":
	from Fitness import filter_text
	from clipboard import copy
	from wordninja import split

	def check_input(text, datatype: type):
		while 1:
			response = input(text)
			try:
				return datatype(response)
			except ValueError:
				print("Please enter a valid number.")

	def remove_repeats(x: list):
		filtered = []
		for i in x:
			if i not in filtered:
				filtered.append(i)
		return filtered

	cipher = """1314410722191820023605853939601328205531393909272017374114222134362055182720601397551813480185050532329914182621973499963124963734556020850908141809361360490315361219400938979640424209312017321340995585453108961432073640105540979412944516270712214332271220311238489637499732554528212433143938480337343896968527302608054985095514281340241805024834324432973436123336961428182438174112210713214539364020322485059614363316422622244941481713144133143441344896993728430741033740336041970138343648013227973421971855142249191617600501180505363717402332433755414322061836114442604937961428074148030614221849021738973107331642442249244197171321103028969444150813279914024817558548279734552707424321341722966045440818979614321549290629101413403014411217061812143120109417172810963220961428482709373148340621033797410605496043339407443644282433189448060823292417291202274385109618059614284149273355292341063828301332492805183394459922203124181612204836130818490333025508130206149614222717229755102112341044292210242833249438553720054960433985481741103931483427973433184848360106020194060614360813604903363405602427151894060538232808363149452422268524060212176048961422152429552910140624606044436023224337979699163002971733183428103148349926080124270506551899064008944834370622330622203145052724403038336016423430363706142824321327101260492201604920600596143724299717604428242755389717299760493149181697340194074422443749131438011443402032102248453712606048222223284901141818992210313318202812214336018548973601963634134155140614371844374940960218971516559614400642360555093213604834362402121713140860942497361343249631074243212017281340456026372421962948171422493621123413144006061436081336243616449618181227131402434130322749331432344048972730090296145527424209313417324048340614372422109442061331453145162444490230361516961043020614413040011843096048122109372797202913404512061016492838554328409755404808961441481796143615319703232194075513274501073740240708410944604906219706159455103848333755143215181136103441201206011897963141482112080614029717855514222455142748121609153224990206439410551536551432013110220614279696142212164315322445961437093028392328101440233221092831972912172913271018485518430855143849341916171805018505052232153205604928410560169720961436019442263724338520361518850360480729972827972096144197171030554049552820558509310332302848993241341617601606961428422945068505151811379940973412164315364999061440061960204136144020172923371209364048201055312406223455854494960255961817329614364915160616970560245594122706324208191699552130381537174048430826148512282427971731972013142897294441330337343806164402142720493201282923223440972116203885433299992117280524604319603438373855133110021209184930283360203727973422970124084406222002053014321321305540030248175514219609943314012124379614221202031232131322439499961537021215021706491894154237"""
	cipher = [cipher[i:i+2] for i in range(0, (len(cipher)-1), 2)]

	symbols = remove_repeats(cipher)

	text, best_key = HillClimb.threaded_hill_climb(
		decrypt_homophonic,
		cipher.copy(),
		lambda x:x.copy(),
		{
			symbols[i]:(alphabet[i%len(alphabet)])
			for i in range(len(symbols))
		},
		lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\n\nText decrypted with key:\n\n{decryption}"),
		modify_key,
		iterations=10000,
		same_key=True
	)
	table = key_to_table(best_key)

	if len(input(f"\033cTable used:\n\n" + '\n'.join(f"{alphabet[i]} <- {', '.join(table[i])}" for i in range(len(alphabet)))+ f"\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)