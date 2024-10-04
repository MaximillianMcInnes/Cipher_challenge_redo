import HillClimb
from random import random, randrange
if __name__ == "__main__":
	from itertools import permutations
	from math import factorial
	from clipboard import copy
	from wordninja import split
	from Fitness import filter_text
	from math import floor
	#cipher=filter_text("""SIEID ATTPW ADIVL SOLWO IYMRD AOSTT TDUHM AGTTT HSEOO TAEST EOGNU AEDLN HNRDH KIWOA MENEE INEAS NPAIT SLIAI AOJDN TCAET SOKEE EIULD HRAUE WSYSA IRBCT WNNSN TARHH SUHAS MNOAG SVEPI AGINE IOAIS EBGRS TTWYO GTLNO EVMRT WGTOI SAHHI ECAWP HTRAO TCRTS YRBYG""".upper())
	cipher=filter_text("""JDEFO IOLWI LONUO NGPYU LAORS MSSTE AETHG IOGTI UHSOL DHUSN YOEDU HATTE TCEDA HIIAL TSETR FTERM AIOMS EOTIT HPOVE RIECE DNBAC HRNOP NKFIE TNSRO SNVIE TAIEL WRESN RSIEL TOPYA EORRP THCHW IIAEB HVENN AEUBE OLLTO AERCT EDNGA IBTEE EWNHL ITENS THEII KECNW AASUN SMTAT EHMII EASHD OMACM SIOIS NDURE FTEIN HRVSI GETAI NSTOF LOWOL IGECN REPOF ITTEE PHROT NIROS EANLS DHTST AHWSC EAOTN UNIIG OFNTU DHENT EQIRN UYHUG TOHAN OIMTU EHSRO SEMWH AAEDN GTAON HTAIR ALBRA SSINA AYPLR IKRTN EOSUS NMTAE BHVEI VELED HTSTA HWSGE AODOR OFHRE BEDTS HEATR IAFES IEULL FLFNC OERPE DYTCM UNOMI AIOCT NBTWS EENHE ETMOH FBTOL WILON UONGP TILEH STEAN TRDTI NIHKE ILWWL EUSBB YRAKB EIGHO NTSCP HEIES VEROR HNETE XFWWT EEKTH ESEOS EMRSO EDLWM DWNEO BTEVU IETAL NULMN AYAGD OCETR CTHAK EIHEC PRNER UDNAH TETHC DEEOA DCANI NRMIP OSTAT EHYUI LOWLI DTFNH CNTEO ETINN STRST EEIGA INMSE PEISL EOULD THTSW AHTOU EHGTI GHMHH VETAB EGOEN IGNBN OUION TWDRF SEIHW SMEAI SNGSI SMTHO EIGMP NIOTN TRASE INHHT DTIEA TNHEI TPRSE HAIAS HWSOK DTCEO ERAHA BUTHO TEIUA STTOO FINME PLYMO ETHYR OGSHU HEOSN DEOEP ATXNO THDNA NRDTO OSHEE SFLOW OLTAT HHTOG TTUHO TNAIS TRLCU AOCUS NLINA VOHIG ARNCR EOUID TYWNM OEQIR NUISI TEWHO TECNM OARPR YAKRB NEODS CRIIC LTSER HAATT HSITE TAIOU TNHRE SEFRE DERTI THOSE IANFN CADII LFIUL FCTTA TYHRG RSOEM NIOET NDNOE IUERL RAIRI LEFEH SASIM IIOBT NAMUW SCLRG HAETA NRHHS UDIBG TNDEA IOCUT CRTME SOTAP EHTRA STHPH RASEE OFRTN OHVLU EAAIN ATONT ENDHE PLIWO CWSTY AOLOW ALHMO SITTG ATAEH FIFET HWSIE ANEGU LAEIH IWTSE THLSE HMANE YAEPH VLNED ANTSL LOESM OFOET EORHM EAUAV LBETE LIMFO MSRTE IBHLR RATAY ANCKK ODWPR ONIEO TCTHA REELS ODDFR ELRSA EADOC NTLIO NAMTE NSHIU ACERN TIWOH SUDLL LAOHM TWIOA OFPYF IDEHS BSNDT ATFND OUHSA MICPI NYAGO MGHUI TBECO JTHTH TAEOL DCUHV ACAEH EEDIV MRORO ELSTH ESEAE OSMUC METOB SLLYE IGHEN TBOSA OKTAE VFCAU BULET AINHV GOSTB AEFRS DOOEI MMTEB UTAOT EREHT AUESS RMIIE ASHDC QAAUR DFIEO HMIRI TOLDW UHVBE AEEIT ENNNE YESLM ARABR SIGTS NOITO GFNYH ELTLW RVOEA UDPLE ATOFR STEOL HCLCI OETNO HETTC TTHIY EEASR WASTH LOEIK TRSHT UYABE SOURW LHVED ABEAL ENETD TREOI NEHSE TSEDO LADTL NHTHE ATRSL TEUIG RINPC WULEO DAEBH VENOW ELETA NRHTE NSHIU ACERN VLATA UINTW OIOLC EUDRA NLTIY AEBHV ENDAE ANEOU GRSTA TSREY UTGBP RAPEH SHRIT ESWSW KAOTT ARHKN THIGE HDERO ILNDS AEETO LCRTW EAERN TMEOU HIVCG ETVON OTNFO IGRAK RBNUT ESPSP CALEI LTOSY HEHSE WODBS WETEE CCRAU UATML EATHD TEADT CRALO FBECU SEORI RGEFO RWSBS AEIDA HNSHM ECETD FROEA DHEUT ISREN URTEN SHIIS TTSRN ETAGH TEWAH ATDTN EHRBB EOEYN VRIET GASIT OENIN DDUTE BRMMB EEETA TRHNB OKOOS EEAWR CULLT AYTLE SONOO SSNIN FIGIC NCLAT AMOUI CLAIS DREIH NWTOO SIPSB EAILG NTAKI MESNS SEEHT HTAEO LDWUW NTHAT EHLEW OSRYA ORFAR FFIOG TTROE FRTNU HRNVE IETGA SITOM IINGT ASHEI YAVLH ERUGB OHHSR TIOEN TLIHT EFEHT OIGTL HPRMT EAETL NNYPI LSOIG ISNHE ETILC OCANN HCSND EAPRA PEHSV NLEEE DNGAI TAPEO SLOIN LFCRE RACAI NITOL OFOOK RADTW ROERI HANYU RGOTO GHHUT TESSH EDESI LPCLA EUTOS IINAE JOMNY NMYIG HLDAO IYETW BSIHS HSEAR RY""".upper())
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
	# def decrypt_transposition(key, cipher):
	# 	text = []
	# 	lowest_in_key=min(key)
	# 	if columnar:	# Rotate the table and read it back all in one go
	# 		rows = len(cipher)//len(key)
	# 		for i in range(len(cipher)):
	# 			try:
	# 				text.append(cipher[((key[i%len(key)]-lowest_in_key)*rows)+floor(i/len(key))])
	# 			except IndexError:
	# 				pass
	# 	else:
	# 		for i in range(len(cipher)+len(key)):	# Attempt a few extra characters to make sure we arent missing anything
	# 			remain = i%len(key)
	# 			try:
	# 				text.append(cipher[(i-remain)+key[remain]-lowest_in_key])
	# 			except IndexError:
	# 				pass
	# 	return "".join(text)
	factors=[n for n in range(2, len(cipher)) if len(cipher) % n == 0]		# Gets factors of the length of the text (from the internet)
#	columnar=int(input("0 - Simple transposition\n1 - Columnar transposition\n\n"))
	if int(input("0 - Simple transposition\n1 - Columnar transposition\n\n")):
		def decrypt_transposition(key, cipher):
			text = []
			lowest_in_key=min(key)
			rows = len(cipher)//len(key)
			for i in range(len(cipher)):
				try:
					text.append(cipher[((key[i%len(key)]-lowest_in_key)*rows)+floor(i/len(key))])
				except IndexError:
					pass
			return "".join(text)
	else:
		def decrypt_transposition(key, cipher):
			text = []
			lowest_in_key=min(key)
			for i in range(len(cipher)+len(key)):	# Attempt a few extra characters to make sure we arent missing anything
				remain = i%len(key)
				try:
					text.append(cipher[(i-remain)+key[remain]-lowest_in_key])
				except IndexError:
					pass
			return "".join(text)
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
		print(f"\033[H\033[JThe length of the text is: {len(cipher)}\nColumns that can be tried: {', '.join([str(i) for i in factors])}")
		factors_to_try=[]
		while True:
			updated = time()
			tmp=input("".join(["Which factors should I try?(all - to try all of the factors, exit - to exit)\nFactors I will try: ",str(factors_to_try),"\n\n"])).lower()
			if tmp=="all":
				factors_to_try=factors
				break
			elif tmp=="" or tmp=="exit":
				break
			else:
				factors_to_try.append(int(tmp))
		if factors_to_try==[]:
			factors_to_try=factors
		del tmp
		combinations, combination = sum([factorial(i) for i in factors_to_try]), 0
		try:
			for columns in factors_to_try:
				rows, length=len(cipher)//columns, max(columns,10)
				for key in permutations(range(1, columns+1)):
					combination+=1
					if 3<time()-updated:	# Updates every 3-ish seconds
						print(f"\033[H\033[JTrying combination {str(combination).zfill(len(str(combinations)))} of {combinations} combinations\n{(combination*100)/combinations}% Completed\nFitness measure (higher is better): {best_fitness}\nKey used: {', '.join([str(i) for i in best_key])}\nText decrypted with key:\n\n{decrypted}")
						updated = time()
					percentage, text = 0, decrypt_transposition(key, cipher)
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
	#	decrypted=decrypt_transposition(best_key, generate_table(columnar, len(best_key), cipher))
		decrypted = decrypt_transposition(best_key, cipher)
	else:
		print(f"\033[H\033[JThe length of the text is: {len(cipher)}\nColumns that can be tried: {', '.join([str(i) for i in factors])}")
		columns=[]
		while True:
			tmp=input(f"Which factors should I try?(all - to try all of the factors, exit - to exit)\nFactors I will try: {', '.join([str(i) for i in columns])}\n\n")
			if tmp=="all":
				columns.extend(factors)
				break
			elif tmp=="" or tmp=="exit":
				break
			elif tmp.isdigit():
				if 1<int(tmp):
					if int(tmp) in columns:
						columns.remove(int(tmp))
					else:
						columns.append(int(tmp))
			else:
				tmp = tmp.split("-")
				for i in range(max(int(tmp[0]), 2), int(tmp[1])+1):
					if i not in columns:
						columns.append(i)
			columns.sort()
		if columns==[]:
			columns.extend(factors)
		del tmp
		decrypted, best_key = HillClimb.threaded_hill_climb(
			decrypt_transposition,
			cipher,
			lambda x:x.copy(),
			[[i for i in range(1, columns[j]+1)] for j in range(len(columns))],
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nKey used: {', '.join([str(i) for i in best_key])}\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			end = False
		)
	if len(input(f"\033[H\033[JKey: {', '.join([str(i) for i in best_key])}\n\nText:\n\n{decrypted}\n\nText with spaces:\n\n{' '.join(split(decrypted))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(decrypted)