import HillClimb
from math import floor
from random import random, randrange
from array import array
def invert_key(key: list|tuple):
	lowest_in_key = min(key)
	return [key.index(i+lowest_in_key)+lowest_in_key for i in range(len(key))]

# def decrypt_simple_transposition(key, cipher):
# 	text = array("u")
# 	lowest_in_key=min(key)
# 	for i in range(len(cipher)+len(key)):	# Attempt a few extra characters to make sure we arent missing anything
# 		remain = i%len(key)
# 		try:
# 			text.append(cipher[(i-remain)+key[remain]-lowest_in_key])
# 		except IndexError:
# 			pass
# 	text = "".join(text[:len(cipher)])
# 	return text

# def decrypt_columnar_transposition(key, cipher):
# 	text = array("u")
# 	lowest_in_key=min(key)
# 	rows = len(cipher)//len(key)
# 	for i in range(len(cipher)+len(key)):
# 		try:
# 			text.append(cipher[((key[i%len(key)]-lowest_in_key)*rows)+floor(i/len(key))])
# 		except IndexError:
# 			pass
# 	text = "".join(text[:len(cipher)])
# 	return text

def decrypt_simple_transposition(key, cipher):
	text = array("u")
	lowest_in_key = min(key)
	i = 0
	size = 0
	while size < len(cipher):
		remain = i%len(key)
		try:
			text.append(cipher[(i-remain)+key[remain]-lowest_in_key])
			size += 1
		except IndexError:
			pass
		i += 1
	return "".join(text)

def decrypt_columnar_transposition(key, cipher):
	text = array("u")
	lowest_in_key = min(key)
	rows = len(cipher)//len(key)
	i = 0
	size = 0
	while size < len(cipher):
		try:
			text.append(cipher[((key[i%len(key)]-lowest_in_key)*rows)+floor(i/len(key))])
			size += 1
		except IndexError:
			pass
		i += 1
	return "".join(text)

def get_name(x):
	return "Columnar Transposition" if x else "Simple Transposition"

def get_func(x):
	return decrypt_columnar_transposition if x else decrypt_simple_transposition

def decrypt_double_tranposition(first_key, second_key, transposition_func_1, transposition_func_2, cipher):
	return get_func(transposition_func_2)(
		second_key,
		get_func(transposition_func_1)(
			first_key,
			cipher
		)
	)

def modify_key(arguments):
	key_to_randomise = randrange(2)
	key = arguments[0][key_to_randomise]

	rand_num = random()
	if rand_num<0.25:					# Swap 2 random letters		25% chance
		numbers_to_swap = [
			randrange(len(key)),
			randrange(len(key))
		]
		key[numbers_to_swap[0]], key[numbers_to_swap[1]] = key[numbers_to_swap[1]], key[numbers_to_swap[0]]
	elif rand_num<0.5:					# Move a random chunk of the key to a random part of the same key	25% chance
		to_move = []
		key_from = randrange(len(key))
		for i in range(randrange(len(key)-(key_from))):
			to_move.append(key.pop(key_from))
		move_to = randrange(len(key))
		for i in range(len(to_move)):
			key.insert(move_to, to_move.pop(-1))
	elif rand_num<0.75:					# Shift the key to the right by a random amount		25% chance
		for i in range(randrange(len(key)-1)):
			key.insert(0, key.pop(-1))
	else:								# Shift the key to the left by a random amount		25% chance
		for i in range(randrange(len(key)-1)):
			key.append(key.pop(0))
	return arguments

def select_factors(factors):
	factors_to_try=[]
	while True:
		tmp=input(f"Which factors should I try?(all - to try all of the factors, exit - to exit)\nFactors I will try: {', '.join(map(str, factors_to_try))}\n\n")
		if tmp=="all":
			factors_to_try.extend(factors)
			break
		elif tmp=="" or tmp=="exit":
			break
		elif tmp.isdigit():
			tmp = int(tmp)
			if 1 < tmp:
				if tmp in factors_to_try:
					factors_to_try.remove(tmp)
				else:
					factors_to_try.append(tmp)
		else:
			tmp = tmp.split("-")
			for i in range(max(int(tmp[0]), 2), int(tmp[1])+1):
				if i not in factors_to_try:
					factors_to_try.append(i)
		factors_to_try.sort()
	if factors_to_try==[]:
		factors_to_try.extend(factors)
	del tmp
	return factors_to_try

if __name__ == "__main__":
	from clipboard import copy
	from wordninja import split
	from Fitness import filter_text
	from itertools import product
	from copy import deepcopy
#	cipher = filter_text("""MAYTTROITIAAAHAIBEIAFAAYWEHMHSHANVTOSTEETLLBRPTAAAMEOWNOESMTTEHOSIIUASAADTSEAUAEEHEEINTHHAHAHOSVOOHTEEYEUSHRFLETAGYHSHIHUGOTASIIARHNSHEESELNHTHRGBSTNNCCNLOUUTFNTRAAOHMNRSAOOAIAEEOATNNILNUOOJMAHWFATARMCSMDEMENLTILEASULWSAQOTNLNLFOAYCCGEERJFENCTOUNENLELLDGAPIOCDPAAOBTRORSTSOIAYUIHREVORITEHGPEFECSITELACIDOANEHOHCPEAELOOWVAWOINKLOECSEEAOETEEAHITIFYHAOEDIIOFROTBETDLETCDLPHABTRROYIDHNCTXUEYREBTOEODERMAITKHMNHGHLOTLPECBHYOAFGKITKTCIDSLLHEREBRAHFTOTHLTBIAOHSKSEEEEUECIBLLYANAVISCAITOMHLSUAEIUEEOAOMTOLATFATEWHDNHTRRAEIPHNCAOINIUDHTENHSSUOUETNHEIGTENRTNTLTNUFEONACHYRTRNEAOSNHSASOEDXOVHNFEEOARONILNDDXHNIEEECCHNEEDMPHTEOEGEHMDECEBRENONIENIOIBIEMYOYLREEEETNOTEVEHHTLRNOMRNRNLSLOOAAILIAGHNIOONHTUNBLNARMAUTMDOTULESEIETEREKNCSKOEORHTNGHHMTETFPHNAEASOENSWDEESRLPTGDCPTSFOISESKTPNQFATEOCCVIUMEARONLNAYEHBITOTEEAAACHTYEOSHIMRNIBETOTERMHEHOSEOREODALHCTANTOWCNUATNRCCUHCSOBNREANIWEXVADBSMFHOACRUEMGVDROCSRANTTLUBOTHPSRILULRYYPETGLADITWYOWOONAUKNUDSQNEIWAOPVEISNRSURHRNIELTTTVHNTRPYHAOFYSLEVTEWATOEOAMLNNRAAUNOSOCHEEHDOEYWERLRHWBSSNBSIEHGSYHDSTDXTRKEASTENWSTSTATNTNSRTXAETOOCRNSULGATSTNIFSVSROEESESTBPERAIIHCAIEREOIAAIUCMHDFXSECBETMITITDCTHHMHDECAOHDISWEOAYKSEPMUGYSYNNRIVOUUHIYSAODOSFYBIAEEUECYRTNNROCSAETMAEQAPFBETOAOLESTRHRESNNKSEWEITEEPFITSUERHANFNRTEMOHNMNEISEEANSDTIRFWICDLHYEITUHTNNTYIFSSKLMCEOOEHDETUERHMLNTLAETWCIORTINAIIDATEAEXAOCDEEHTSENUSEICSXILMFEVNENNONRSNVSNAHCFROOFYOWMNWTANIIHHTKBWMEATTEITOAHGNKKLMXTRWTOEAIRGTNLGFRULEDGHRYRBGTOMPSOOTBEDIYBHSUESAKYOAOENEWRIMLPOTAEOPETHGIAEHLTNRAOOHGLTHSARNOGENOLINUTLNSIACIWUDEDFLEECECRBCRNNRNBDITERROAWVFEETNERYOTGHICABETOHSERBDTAETENTRNYROHNAFRLEBTGTIEOEEIEMUASEYREECNSIIENAWHTSISLIIFEDURYOYOTIEIAIANUEIESRSRARXOAEIDORVNIPUYDNEOSSFUBETUEOFMUEREOEEENLEKNHAAREHHIAFAEINRYAPIYYEBAETAAESVSMSACDSOIVEOLEAITELTTHLLHKDHSNIESEITETXMAUSEHTSSRAYTHTSNHMOCBEHSTCSSENITCANTNESANOTERCMIANHOLSYAIDETRUITSWTTATADATOSUSOHNIIAOOCTTSIAHIEIFEDOHNNEUDEAIEELNIAEOOOSNEEERFIRYERINUEEEOSVIAHSWOHOUVBONNELLNINPTDNESEGENIIHBOLBCTAPESESNVWINLIPURTEREDIXETNTRTSTOYPVRALPSEEDRDAEESOCOMSEMNAHVDTSLLETTEWHNHGTTSNAMHREURSNNEITDERAECLCATIAHOBHLATHGDDMNWEUHSNNTEOTETLYNISVAMTNINENIGLRNEENIIUYHLEEUTYIETSTDOSETBWTIAHCUVEDYTDUUTEOEACNEC""")	# 2,1,3 2,1,3
	cipher = filter_text("""YMNRIEEKRUOETGHIHOREORITGTLCENOUOKMWLIEUHESSRRKIARHNSSOTEAIOETLOALTCEIVDUEHTUSMMWSTCTNOEMNUIUFDLCEBCTCVPAOAWIAEISNEEHTHRAISHESATLNNMAHMCHUMEEOEETTESLEEEMRAIUMNEORMTHNTIIRCMINNHOONNTHACHRNITEARCEKUNNNTOAADCOBTETITDNEEHYSDWYEAUERSIEWNCCOTNNUTHAOIORYEEACROOAINCUEERRITTOERTLHTUDTREPRINRODIPHEHGHGDUMRHIFAERFVITLLNVIUENSTSYIURSHATIETSBTEGRVRNADMYMESNLEIIOAFDGOVEDLGSBNAAMPEPOIRLENRAAAKREETVOIVLLFHIPTISWUEBFIENESLCDEYKELFEEAONEEEEETTEAYEAYMIHEHETTIIEOTEBMWNHITRLAIEERNSTPBTMWHLEHAEERFESHETRKELTEENRMMRASSBEOYAHNPOSHDEGEPFEREIHHRSTTNGLNNNVITTCTOLMHNVEIMETTLODRNTACEEPOBHSOSRCMTHRTSSDOSRSTUYOEESERNYMICHEWODTINOYEIVASVTWUEARANHSFTOSAFTEDTNERKSORSHEAOMDHESULREEECHLOHBRICCWTDLLNVSRLETTOSDLOKATTHFTHNALEHNIMIXEWEAEIEHWBNIEEIELSTERAEACNUUNRFNNFRGFMRIRTENETGEVLTOHEITPBAETEHRLHAWOAIKYEMHDUCTFENEMOAOEROPTBYTISSASOTASHETRNSAUOTDCAWSCONRIONOINEITRSLOOSOIDEHAEPCLGSOTTLTCPERTEAWILWOERETEDIYTNLNAECFVOIUUAHARYTHYEIREHICNORIBAHNRACMRSCEEAFSIADLTIRPFHTESAFHSEEEFIDDTACDILLSFSOYRRPTBNEEATDRTOITHEITOAEWTAOTCELOTREAEOWENEFPRTREHEVSETITIICIETEODHCMESGDHOIYTLMISRTRTNEWONANEEOHBYDIFLCSKCNAESACCAOLRTKOLWOEOTREWPYIAHTHLNBSGRERTTICACTKUBIEANLHTTTUEVUTIIUCVPRKWTHEOYIEOHOAVOLNGODIFPEMENRMPEACSNSCFSTWTHCELDUOIRRLTIMOIELRVTYLSOMALRVIOEHEEGREESFTTEACEHOEPTATHKHPSLDWMLOAIIARLLODITDYITENECLNSCNEESUAEGCNNTEATNVLAETMOCLANMVETOTSRHRRTOTYIAATGRHAUITESTAGEEULOSETRHSTLATUCWEAKNTLUYCSVHACRHECTWKENIRHIAYILTUSOPHUUVORWMSWARIIHITEDVAIRESCGSHFNNAPROHTHMEYUGNOFLHLNGSVSNUAEELITBEIYRLNNOOIEEOCEENREXDHDEEEAENIHYCFTEALINPPNNENPETTELCEFDARNAWMSRTNABDNDEESAELLAORUSWIEECPHDHLWECRTLUENNEEMSFTEOIAVLNBTOAYTNAWHHHEGRHOSTELNTFHTOIRCPIAEYERNIIDEILWILBSHADFYTEITOAGTLNOGTETHNNAOTCQHTIMTMIRMAULAUTETUPIHPVJYCHIASMDIOEITAKHDIRCAESENOOSAGTUETLNTWHNRTACOTNIIYYAGCEUCNHMLOHEAIHNNIDTHOLEASDWARIRNNPADAIRSRREINVTFTSIOBTSTOGNOVIRNOAHEICITOREARHOHYNEKRECMHWINREHBPHSEIMGESTWIEIATTAOOCTRECBEDOEAGEIOFOMYOUFEEOTTAUDIIFESTOILW""")
	if int(input("How would you like to decrypt?\n\n0 - Use a key\n1 - Hill climb\n\n")):
		factors = [n for n in range(2, len(cipher)) if len(cipher) % n == 0]		# Gets factors of the length of the text (from the internet)
		print(f"\033cThe length of the text is: {len(cipher)}\nFactors that can be tried: {', '.join(map(str, factors))}")
		key_lengths = []
		for i in (1, 2):
			print(f"Please choose the number of columns to use for step {i}.")
			key_lengths.append(select_factors(factors))
		transposition_types = product(range(2), repeat=2)

		starting_arguments = list(product(transposition_types, product(*key_lengths)))
		text, key = HillClimb.threaded_hill_climb(
			lambda key, cipher:decrypt_double_tranposition(*key[0], *key[1], cipher),
			[cipher for i in range(len(starting_arguments))],
			deepcopy,
			[
				[
					[list(range(i)) for i in keys],
					transposition_funcs
				]
				for transposition_funcs, keys in starting_arguments
			],
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nKeys used:\n\n" + '\n'.join((", ".join(map(str, best_key[0][i])) for i in range(2))) + f"\n\nTransposition types: {', '.join(map(get_name, best_key[1]))}\nText decrypted with key:\n\n{decryption}"),
			modify_key
		)
		key, transpositions = key
	else:
		inverted = int(input("Should it all be inverted?\n\n0 - no\n1 - yes\n\n"))
		transpositions = [
			int(input(f"What type of transposition should we do for step {i}?\n\n0 - Simple transposition\n1 - Columnar transposition\n\n"))
			for i in (1, 2)
		]
		key = [
			list(map(int, input(f"What is the key for step {i}?\n\n").replace(" ", "").split(",")))
			for i in (1, 2)
		]
		if inverted:
			key = list(map(invert_key, key[::-1]))
			transpositions.reverse()
		text = decrypt_double_tranposition(*key, *transpositions, cipher)
	if len(input("\033cKeys:\n\n"+"\n".join(", ".join(map(str, i)) for i in key)+f"\n\nTransposition types used: {', '.join(map(get_name, transpositions))}\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)