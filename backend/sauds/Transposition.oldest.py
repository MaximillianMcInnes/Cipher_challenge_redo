#from nostril import nonsense
import HillClimb
from itertools import permutations
from math import factorial
from clipboard import copy
from wordninja import split
from Fitness import filter_text
from math import ceil
#cipher=filter_text("""LWAU ARLMS ORYDA OOBYH HULST ROSEN INAEC TIIUH EIRTS EOOTF UHEEM SRONS ESIFH NGECN TOAID ENTMV EVCOA ATEIE YHIBI ITNEH HLRKV EEYIE IMVTY HEEAN OWDRT TFURH NSISF TNNSK DSAAM UMMER IATIV ETOBA LEPTS HETSR GEPAA EGMDS MUFYE IFPLN ITCKO HSUTH RMERI CANCY GOATT RNIGD IAVST ENHRA OAEEH EEISD TAHCL ETRTA RFWTU ROEYN GAAIT RNHLE SCRER AGKEY ESABN RACIS EUNIT COYST DEOBH HOEEN TTIRM ETLTE OVNUI BECES TDIAM WIYSA TREMI MTNRH SEKIE AARHE IYIFT DFTIM IAYNC LTLOA TRVND EOPOF OREUT EWERL ITNUR MTAEO OENPR ITVBE NOIHA TOGHT WHEAA MSTHS TBTVP NOHGN ONOTC FHIEN ICEIC GRMID YNAHH CEOIT SAMWD NTRCU EORIE NDRGS HIEIF RIRFO HEFET SNEKK NIARS TRUCN AEFGR LLOYL NEODN EHNSO REDAS TNMAH PGOIN EREAK EEIEM NPHIU ATLIR CVHPO UWREK TTINL BHLAR IEERN HPOTE ETEHN SDGET IUEAK HTENL ADEVO OEEMI ACCFP HNABO DTSSA CEFAA OILMM NRNEA AHNTR NRMLA ISNSI STADR RCKFA EOTRI BANET HLCGW LRHWU HIAEE AARDT TEMSQ TAUET EAECS IHNTE YRTAY SCNEN DNYIM ETIOA RRNVT NOMIU ROEVN FETCE OAELY BMRNE UEAHG VOLHA LILAG YOHTN TLHMO EELYW VTEET OAADF HHSSE PNTOE ITPBI HSILL SOLRP CATER OIEEN DYYPH GCSTH REFTN TTMCL WKOEA EHOSW ALUEO THLRA EYGRR EHBUC DIDAE INCNR OTADO FJERI FRKRH FCEIE EECWD ONNSW INSUV LWREO ODITB TOLEE EIPCO WEERN NEVLT ILHEI DDBEE SIUHW SAHEH YEIIB CANTN WPTHU IESFC EVTYE EHETS NMHTT FNETA SRTYE HEUFS OEOVO CYEEE MDELE ADIVU NNROT OSTSH ITHEO ASWTR LTEUL ASOEE AVSLO ATTCU TLTHC ADAIG VNEEO RIRAH FRTFN AASDT RKHEE AOWLF OTTML OREOO SOETW TREAS EBUSE YHLBE GHTIT HNMHE IERYT PGNRL NLCRC UAUTE EHPED PWEEN TCHBN EEETI CMOOA TEYNN KEMCT NOHAF SVIIE CEOOF REHSC RERCS ENREO EWIAW ULESE OAGRP UCELD REHPL NHAEA SEAYO RMVIE IFDSC RDRBC EDALC TBOHW TIIHS ETRLE KLLTA OTLNI AIKSN BYHSM KUIAI LLRRL EMSTA THSST LIEIR YCTWE OSPTE LENES HAMET SDNDG GEEGI HNTAI WCIHR EHRLT PBWAW MSIED OTNLN EOUOT MIIMN IROCC SNUHA OETIO TUDOR TAHCN ETATI DCERL TSILT LAEOR RNCBI IEWUC CHIEI TNPYR EPTLR EVTOC EIUTR LLHLH EIEOW GSTSU INTTM HEEAN OOOCF NDSCU TTEUN TAVHT EEHYO EGRTL FNITT WOODR SITLE SLAII DHPNO OTRDO CPFNE ITOOI HTELN ATEEO ARNRE OTORE HPTPT NIIGW TARSN AMAVE RHERE NREML TTIHO LKEWE EEAND ODWNR OYSTA COTUT ICTUM INHOD EISAC EVTXN HPSSE OTOHA ILLSF MMUEN UTNSR AYXAE EESIE HWDAH REIOI TPLLV TYIIM AAOCT MNNES IROUP FCCET TLSVP EEECL CLHHO LUOAI TTIRW WEIHR TAEIT HITGS""".upper())
cipher=filter_text("""AIYNA GKRCT ELUOI SGAEE LLSON OKONS NAAOT OWDSM SEAAT OEPNC EDTLV UNTRL IDDTH HEPTE FAIAD GOSWR EMUIR EINMO USRSG SIEHN YARSR ESNOR ROEDR ELEON PESEE HUAEM AIOCR BRMEI ISFEL TNIRT EYLVA OTTTE SROTR NWAOI QIIKN EANTO AETNT TIEOE TNTFU NIDFE ETMSR TMHEO CDIEE AYECY FIOHE SAPEC NRLDW DNSII LNTGE IOAAD SEEBS EDOUA SLITR TESRO SOSTA LEEIA YAGLN YOESO EAROO AMEOS NISGA IAHAL NSTEC ITTEU CDRSI WLGMN ITEMP ENNED WVUFY LLSNV YRDEE ELTRT ALODP ISSDP RSNTY LASED EPTRP ODNCI CBNAR NAYHS POAAL VYLEO ARRDI LNSSY IIECO ADEUE ETEAP ADSAP BREPO LSTIF LECCI VERSA EDOOC WRSGO OEUEN NOCLQ EFEES NRRCA RDQOS AACRR PLNIE HSTEB EMTER SDNLY ATREO TNMER TNELN LAIUI TFEEN TGIFL ISWDE NCMSE """.upper())
if len(cipher)==0:
	exit("You should have put in the text")
if input("Do you want it to be reversed?\n\n").lower()=="yes":
	cipher=cipher[::-1]
def modify_key(key: list[int]):
	key = key.copy()
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
	return key
def generate_table(columnar, columns, cipher):	# Generate a table to transpose
	rows=ceil(len(cipher)/columns)
	table = [["" for x in range(rows)] for y in range(columns)]
	if columnar:	# Rotate table
		for i in range(len(cipher)):
			table[i//rows][i%rows]=cipher[i]
#			table[column][row]
	else:			# Without rotation
		for i in range(len(cipher)):
			table[i%columns][i//columns]=cipher[i]
#			table[column][row]
	return table
def decrypt_transposition(key, table):	# Reorder and read table
	lowest_in_key=min(key)
	new_table, text, columns=[table[key[i]-lowest_in_key] for i in range(len(table))], "", len(table)		# Re-arrange table in the key order
	rows=len(max(table, key=len))
	for row in range(rows):							# Read the table back into text
		for column in range(columns):
			try:
				text+=new_table[column][row]
			except IndexError:
				pass
	return text
factors=[n for n in range(2, len(cipher)) if len(cipher) % n == 0]		# Gets factors of the length of the text (from the internet)
columnar=int(input("0 - Simple transposition\n1 - Columnar transposition\n\n"))
mode=int(input("\n0 - Key\n1 - Brute force\n2 - Hill climbing\n\n"))
if mode==1:
	from time import time
	import Fitness
	Fitness.init()
	decrypted, best_fitness, best_key = "", Fitness.low*(len(cipher)-(Fitness.ngram-1)), []
	ending=input("Do you know what the ending of the text is?\n\n").lower()
	if ending=="no" or ending=="":
		ending=""
	else:
		ending=filter_text(ending.upper())
	print("\033[H\033[JThe length of the text is:", len(cipher),"\nColumns that can be tried:",", ".join([str(i) for i in factors]))
	factors_to_try=[]
	while True:
		updated = time()
		tmp=input("".join(["Which factors should I try?(all - to try all of the factors, exit - to exit)\nFactors I will try: ",str(factors_to_try),"\n\n"])).lower()
		if tmp=="all":
			factors_to_try=factors
			break
		elif tmp=="" or tmp=="exit":
			break
		elif int(tmp) in factors:
			factors_to_try.append(int(tmp))
	if factors_to_try==[]:
		factors_to_try=factors
	del tmp
	combinations, combination = sum([factorial(i) for i in factors_to_try]), 0
	try:
		for columns in factors_to_try:
			rows, length=len(cipher)//columns, max(columns,10)
			table=generate_table(columnar, columns, cipher)
			for key in permutations(range(1, columns+1)):
				combination+=1
				if 3<time()-updated:	# Updates every 3 seconds
					print(f"\033[H\033[JTrying combination {str(combination).zfill(len(str(combinations)))} of {combinations} combinations\n{(combination*100)/combinations}% Completed\nFitness measure (higher is better): {best_fitness}\nKey used: {', '.join([str(i) for i in best_key])}\nText decrypted with key:\n\n{decrypted}")
					updated = time()
		#		text=""
				percentage, text = 0, decrypt_transposition(key, table)
				while 1:
					if text[-1]=="X":
						text=text[:-1]
					else:
						break
				if (ending!="" and text[len(text)-len(ending):]==ending) or ending=="":
					fitness=Fitness.cal_fitness(text)
					if fitness>best_fitness:
						decrypted=text
						best_fitness=fitness
						best_key=key
	except KeyboardInterrupt:
		pass
elif mode==0:
	best_key=[int(i) for i in input("What is the key?\n\n").replace(" ", "").split(",")]
	decrypted=decrypt_transposition(best_key, generate_table(columnar, len(best_key), cipher))
else:
	print("\033[H\033[JThe length of the text is:", len(cipher),"\nColumns that can be tried:",", ".join([str(i) for i in factors]))
	columns=[]
	while True:
		tmp=input("".join(["Which factors should I try?(all - to try all of the factors, exit - to exit)\nFactors I will try: ",str(columns),"\n\n"])).lower()
		if tmp=="all":
			columns.extend(factors)
			break
		elif tmp=="" or tmp=="exit":
			break
		else:
			columns.append(int(tmp))
	if columns==[]:
		columns.extend(factors)
	del tmp
	from random import random, randrange
	decrypted, best_key = HillClimb.threaded_hill_climb(
		decrypt_transposition,
		[generate_table(columnar, columns[j], cipher) for j in range(len(columns))],
		lambda x:x.copy(),
		[[i for i in range(1, columns[j]+1)] for j in range(len(columns))],
		lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nKey used: {', '.join([str(i) for i in best_key])}\nText decrypted with key:\n\n{decryption}"),
		modify_key
	)
if len(input("\033[H\033[J"+"Key: "+", ".join([str(i) for i in best_key])+"\n\nText:\n\n"+decrypted+"\n\nText with spaces:\n\n"+" ".join(split(decrypted))+"\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
	copy(decrypted)