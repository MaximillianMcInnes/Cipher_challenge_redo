import HillClimb
from random import random, randrange
from Fitness import filter_text
from itertools import product
#cipher = Fitness.filter_text("""XOLIM IHAZE AOVEF RPEKS QOBPP EXEWT LEVNZ ELTOG TTWOU HVREA QDAHI UNHBI ZHIUO DSRVN EYIUJ PHODA XEEIA HKYNI QDVNY SRRUG VRZHD DVNLE ZIXEW TLEQO WLGCB IBNNN IFZLZ OEITG LERAE PWIGT QEGTV IRECE RRTBJ FFRXT LEVNK IHEGT MAASM EHAFC LRTTH DBTCC KUZRV NGALA XGRNG MFEFO WRRRE AQDVA FUBBP EHDBT WOFST FMMVR KCNNX EQTTB TOWLK WVNZT LEVNZ ELTOG TTWOF SZYHA GPVRN NPMII AILHV RWEQF FOKEJ SEIAH URAWW RAMAH KGVBV RNAHO ZILLR AGENN ZWFOX EHOAH VRVOH EASLA QDTIS RRRRT HTPLE TLEFT HAAHA WSSEI AHURW WVNZT LETFJ EFOMH ASQOW LGCBI BNLEL IQNHT OIZER REAGO NAQDL IQNHT VEGED VEAVE ALDFF OFTLE MAXFR RSSKC NNXEW LTRUG VRUCB NBIHU HDHOT IZETT AHQMN NAIBN NNGDA SPPTE RRHDW RAMJU MLKCT IJELE QOGTV NYEWT TFHNW TLEBX PAFSW OBOYT LETIS RRRYA QDMAA SMEQO GTVNY EWTQC LRTTM IWDJP BNPIV DEAAH FOKEJ SPEYT LLAOL TPIWE GTZRI ELTTT XTVHA SVIGC RNNNA YWAEN AWVOH OYKJP VEAIH EPCEA MTLEM ABONW BTATL ECAZE TTAHT TMAAS MEWAL TPBEA WLKWH DHOTI ZEEIA HLERA QDHOM AVNTA VNAHP LJBRA PYQMI IAIGC BNBIH UHDHO TIZEV NAHIE SSPWV NUOYT LEVOM SPLCO SITGF FXEKT LETIS RRRSU GTTLZ HTPSS WEDAW AUWLE VIUOM THAYF RRBTV OAGAT MAZBA WAWVR HDBNE AQDAH TTAHA SKOFL JGRDK WVIGT LENNN ADSSS DDEAH EQDHO FEVEN UENHD HOAHE ATCHA SOZOE YWEVT WONAS AWUZI GSBTP RTTLE KTHAN ANLGS HDCAW EVUMT LEVIT OHNDA PEMTV RWRAM AHVRV OHEAS LAQDK IRYTI SRRRR TBNNN AYZHL HDDTF JEVEW TLETI SRRRA CZLPE VTWOG THTLE KIRYT OWLKW VNSMI IAIWS HETTH AQDAH CYAEV ENRBT VNZTH TPLSH VRAHT TTOWL KWVNG ANAKS WSEMR NHOYT LEQOW LGCBI BNAHC YKOFL EBYUN AMLXT OAECT PMTLE SIQDT FJEKT LEVES SBNAH MIRAX DBTZH KWHDA HTTMA LYTFA HVRRR EAQDV AFUBB PEBTQ MOWVR MISFC CYFKK WSBOB NAWSS ZVVRQ OIVKC XELIP CBNRE VTWOJ WBTAT LESRE ASIBO RALYT RUMGC BNREV THDEI AHAHJ FFRKE ZIWSA SBIWL ROGTX NKWDH XTLEI RUGVR CKREP TLEPO YKOWV RJFKK FBNTB TWEQM MUYLS KPLEG DVRNP ICKIE ANWSL TRDBN TTXTL EMAOW OKBOP TLEWR UUZWS SPOHN WTPBI EMPGS HDZYA HIEMP VRLSK OBKVN GAMTL EKIRY TISRR RKMYY FEFOK EJSNN PMIIA IAWVR ZVKCB IESTF WRUUE BZBCO CSPLP EJSVU MTLEP OYKOW VRFBI UNHBI FSMAW LBAVC LESAQ DBTRO WSGTW EQMTI OEJYA HTTAH CYAEV EPOAH VETET THDJY TOZLH DVNNN ACSSQ MIIAI WSBAM KXRIU QDVNP OYKGR WSVRV ABIBN ZHIUO DHAZE MAHEB TDOKS JBPET OYHVR HOHPH TTTPE SSLSA MSOYT LEFAO ELTLE RNNLG SHDPE MTVRW RAMMA ASMEH OFOKE JSROW SGTZH HDGUJ HTINH UBNTH NBITI CAPCR AMKAH VRWSH OMHVR LIRRG IBISA WLPHV VKGHT HOUOB NNFIE WLSKA WEAVE NLGSX TGSZL DITGA HASKY LTVRZ BNTLT TLYNH TKUBT XTLEV EPHVV XTLEF ROGVN LLPEM TVRBN KYHEC KVUYF IUQDN NRNTR NPXEF CDPGI ZMIIA IWSLI RRYAQ DAIPC MIBIJ RTTLE RAVIG TVRWS BITGK IWHVR PHVVE AMTCC LEWTH AOVVR AIBNT OKTLE KRIIR EWSHO KRJLX TQEXN KWNFA HCYRE HDLEA PNNLI EIWLD OLTGO QEAHV NOIGT LEPOK STOLU BPFOB AMLMO ZEKTL EAEOK RNKHR RPY""".upper())
cipher=filter_text("""IHRHG FTVEE EENNP OAIAO LARAE IEETI NNBKL SPREE ETNRM RAHSE NEUNI IUMND DTANW REAMO AYDMC DJNER ETSNA DAANF BYOAY MIDOI LJKRB GWHIU ANFTG BRESV MTFTA OAEEO OSERY OEEAS ANDTE TVODI OERSM SNNLC SHEEN NURYA LIAWN WPUDS UANNN EECMR CENAN ROITP LETBR RUYGH STNEN LOLGI OUEEG IASTF OLEEY RSMKI ITTIT DHCFS INSOU CEIIS EANOT EREME SINGI IANEA CVWEN MEIDR AEOTR DSRON RCOTT TTATG CUOLB EMEST DRFAI RIEAA NMTDU ROIEL DDLEE NFCUP AEWHT TLHNG CNRSN ATDRA NTELI ICNFD EEORE IVVEE SONIE HFSNH NATLR EAWUO OSTAT RISOS AOTSD SSASR ISIIE AROND ESTRU OWEAE SNLHT MENEI GKDDS TBELD UIPTN WAELM SDERT IOYEM GHWLO DPUUL VSTTD EMLGP CEODH PITRE AHFRH SYABT UNDOE COEEP RSSTD WIENM NMOID FRMEI NHYEC SSUDN MUNDS OSTAU CMDEN RADVT TAROT SNLAI SNISK UENCA EPELG ATSDE EAIRD SHBIT OEGPB ODEEF DISRO DNIST TSUEU CTSAC GWDRO ENOON IRWDE NNTOD ICINO MNLLO SSEOT FREOL MACSO OPSDO HDFIR GKTNE CIROE ROOHW BCCPN OARDI TNBKC AENOB IEUDT YEYOO FIGAM UDHGR CBONE ORHHI REHEE ROINS DRNUT ETIAA IXUAS OIEIE IDTRT ENNZM CTOLE CSCID NENCN PVOTT DOEGE OOOHD DRNFW UHENN AIURT SEDDD SSIYS RHHEL NEOSO USNEL VTMDG NWDTD AAMEL XANEF EIENR ECTOU NSKKO DTASH NGGEE IOTEE LEUEN RISOR OANGA LNTFC DRVUI NMDDA UHNLN MIVAD FNEBG OARRI TEEOA ERENN REIRE DERDI EDRUL DBITI SYATE NEOLF DSHER NRETB EIILO TOBDT OWRIR NSDAN HEEAU EETNS TNMRE MTSME OTLES TUHEI IIAIA TPGME HTEAA BMENT CNEAT EBNID ERGNT IDCRF NWCRH RNRDP REOOR RATOO USARC NBGTH HMLTE TPIAE EICFE FNLDT OPNNA INIHT AATTN TIDIO EETNR EEMRH EHABH GTTSE NUOEI ESTDE IOSIN HCTST BNNDR CANEN HNAWT NIYTH AITAS PSSCO EAOHA THBDO TBRDT MECIN WEGEG HEREE RNBOL HEKAN SNDFA SRXIY EOAGL TNESE MIAII YNGAX URETL ATEUG ENTPH NCCLS EHTID RLIAE PIBEA IYOOC VNIWR TLYEO AFITB HWOOL TATMP OFSGF LWIOD NFVTA TEDAD REUET HCOEW AMWNE NGNRE WPIAA TDEPO SIETE WMAHE SRRAE HIAST FHATN NERDT CSEUM NSDNE TOTTN EWRIT MLDEH GDMEH EABHS WSSOA SRTDT HDYDE GEOHO EFNIG IAHEI YMEAT UOEST ERXUA CEDVH TTAHN NOFSR TLNBU IERTI AEEDM WTPCR REDEE LHETH IEEEU UEISL IRITM CHYEH LVBTO TVAAF OBDAO PMWLN ODTLT SNHWO ATIBE EDXOT TTEIR THSPM OONGN EPHBO SOUOL FNHAG DTESI GLTNE TTEAT TRDMO LYVSM ESEAG ENSNE EOFNT OWTFP RSRWN RIRFA EGHEF LISOU IOTRA YTNHI HSPEE SFLIE DIGRS EEAIY ARESA HNNPI GESTT AXOSE IIYGA ENGPE TDNGE FEHOT EARPC WENNO NTBRD ERVLO EOTNO IGMRN EEOHR ESSOS DUDRL OFATL EEECI HNTET BDHUC RHBAO EASIT WTNSS NMHOO LLAON IGOHC ETSOS ECDRI ONIHX AEMSA ROSRU NRCAO HHOIV AIAAT NISVT HSNOH OSWUE TYISE REYOH NTEER LRNIM SLEHG TNTEE OROST OCENE NAFEL EBHDT OWHEI DOSER TTSAO XTUIE RSTFS TINPW IDIEE ELWCW AIFHC COAHL OHCVP NERXO HHACE EIEEE CEAOA NWTMM TCODN HDEED BFENA SCEAO SBTMK LNSGO HCNBP UDRKY OEYSE DETTS RENFH HEHET SOSUW UADEE STAOO EYTBA HLXWS YNIML EFATE TIAOS RPAIE ATNNI SROHS HMNBN AGROE BTOSE NEHHE SELDO MBOSS FTUED UEHAE STUOA XGTSD ITSET PTDBW DFRTA IYRTR EETIE RESND HOALS TOCIE TRNHT EDCPM EOEST HOOAE EARDA ERUYN SNHHE SREEF OOLAO TTNTT SIOWR ILOSE TNEIA ERTPN FHYOP EBRNR ANOIR NAMOD HUTMT ESNST HUBKP OMNEI CITSC REVAE FIKQB HCEIC CENHT ASTER SUAOS OOIAG FFNST POEEE IIEPE NOSRM HTTOE MRAAD ATUNI SEOUS MMALN KBSBT EFCEU FNRDU NYASO TESCE RGOBO TYGND HUNHE AITEU EEART NIOUY PEORW UNTNE IEAOC GRTCR RAMNN TSCIU QSHTI IAGTN HREEI ESKAU DAAXT SHUTE HAHER ESOEI ECOVT BOSGD IJTNN NTOUM SEALU IAFAO DFNAE INDAF TYTAT ENKGW RNOAE TRYES OSTND ATWNR SNRUN ESEOE ISNEE OITMR MNWTT OIAOT TRNNW ATNWT YWSYT IINOR DAAOO HAEHE SINWJ GTRHS NVNRT TEEON GOCEH KEEFR RISKH ESEOG KHIRS IFPAG DNIFO ADOEA REWKG HTITO WREEA ERCOR UWFUT OHEUE CFTNC RENOT OEOIT GACET RAOYO ICEIU TNEES ITDIO DHEOE NLSHO EISUS BDTNA RUOTE NERSD EARST DTADE EPEWT IUDAN ITPRI PHNIO ENOET EPTRV GAGRM RNUHU IRRVS EISGC LICMA USSTI OOMAN TEAEO YSDFR REEDN TDSRE OANSA YFGFR IMCTO LOAFM YITEM RIUTL SPTBE GFNNP NTSAU AOKGT YAVEI OMNYT RNOEM HIGSS KANPH FCRNR TATOO EATPE DOUHT NOEWT BELDS EDIDD EBOCB EEPTI OVEAE ATSRS EEEID LPIWR SPUHB ADVEH TNNFL ROENT OAIHU SEHNW EFFGD LTTOS EETEU DDHEV REEUN FUETA AWHAE OVTMC ARRHI TSWLH ONHEU""".upper())
def unlink(instances: list | dict):	# unlinks nested lists and dictionaries
	instances = instances.copy()
	for i in (range(len(instances)) if isinstance(instances, list) else instances.keys()):
		if isinstance(instances[i], (list, dict)):
			instances[i] = unlink(instances[i])
	return instances
def modify_key(key: list[list[list[int]], int]):	# This algorithm was taken from A Book on Classical Cryptography by Madness
#	key = unlink(key)
	key, rows = unlink(key[0]), key[1]
	columns = len(key[0])
	rand_num = random()
	if rand_num<0.2:		# Change a random column shift to a random number	20% chance
		key[1][randrange(len(key[1]))] = randrange(rows)
	elif rand_num<0.4:		# Swap 2 columns (and their respective shifts)		20% chance
		columns_to_swap = (
			randrange(columns),
			randrange(columns)
		)
		key[0][columns_to_swap[0]], key[0][columns_to_swap[1]] = key[0][columns_to_swap[1]], key[0][columns_to_swap[0]]
		key[1][columns_to_swap[0]], key[1][columns_to_swap[1]] = key[1][columns_to_swap[1]], key[1][columns_to_swap[0]]
	elif rand_num<0.6:		# Shift the text to the left by manipulating keys	20% chance
		shift = randrange(1, columns)
		for i in range(shift):
			key[0].append(key[0].pop(0))
			key[1].append(key[1].pop(0))
		for i in range(shift):
			key[1][columns-(i+1)] = (key[1][columns-(i+1)]-1)%rows
	elif rand_num<0.8:		# Shift the text to the right by manipulating keys	20% chance
		shift = randrange(1, columns)
		for i in range(shift):
			key[0].insert(0, key[0].pop(-1))
			key[1].insert(0, key[1].pop(-1))
		for i in range(shift):
			key[1][i] = (key[1][i]+1)%rows
	else:					# Add an offset to each column shift				20% chance
		shift = randrange(1, rows+1)
		for i in range(columns):
			key[1][i] = (key[1][i]+shift)%rows
	return [key, rows]
#	return key
def decrypt_cadenus_block(key, table):
#	key = ((
#			(column order for each column),
# 			(column shift for each column)
#		),
#		rows
#	)
	lowest_in_key=min(key[0][0])
	new_table = [table[key[0][0][i]-lowest_in_key] for i in range(len(table))]
	text=[]
	columns, rows = len(table), key[1]
	for (row, column) in product(range(rows), range(columns)):
		shiftedrow=(row-key[0][1][column])%(rows)
		text.append(new_table[column][shiftedrow])
	return "".join(text)
def decrypt_cadenus(key, tables):
	return "".join(decrypt_cadenus_block(key, i) for i in tables)

if __name__ == "__main__":
	from wordninja import split
	from clipboard import copy
	if len(cipher)==0:
		exit("You should have put in the text")
	def generate_tables(cipher, columns, block_size):
		return [generate_table_block(cipher[i:i+block_size], columns) for i in range(0, len(cipher), block_size)]
	def generate_table_block(cipher_block, columns):
		table = [[] for y in range(columns)]
		for i in range(len(cipher_block)):
			table[i%columns].append(cipher_block[i])
		return table
	factors=[n for n in range(2, len(cipher)) if len(cipher) % n == 0]		# Gets factors of the length of the text (from the internet)
	print(f"\033[H\033[JThe length of the text is: {len(cipher)}\nRows that can be tried: {', '.join([str(i) for i in factors])}")
	tmp=input(f"Which factor should I try? (exit - to exit)\n\n").lower()
	if tmp=="" or tmp=="exit":
		rows=factors[0]
	elif int(tmp) in factors:
		rows=int(tmp)
	if rows==26:
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	elif rows==25:
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
	if int(input("What do you want to do?\n\n0 - Decrypt with key\n1 - Decrypt with Hill climbing\n\n"))==1:
		factors=[n for n in range(2, (len(cipher)//rows)+1) if (len(cipher)//rows) % n == 0]		# Gets factors of the length of the text (from the internet)
		print(f"\033[H\033[JThe length of the text is: {len(cipher)}\nNumber of rows: {rows}\nColumns that can be tried: {', '.join(str(i) for i in factors)}")
		factors_to_try=[]
		while True:
			tmp=input(f"Which factors should I try?(all - to try all of the factors, exit - to exit)\nFactors I will try: {factors_to_try}\n\n")
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
		best_decryption, key = HillClimb.threaded_hill_climb(
			decrypt_cadenus,
			[generate_tables(cipher, columns, columns*rows) for columns in factors_to_try],
			unlink,
			[[[[i for i in range(columns)], [0 for i in range(columns)]], rows] for columns in factors_to_try],
			lambda fitness, time, key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {fitness}\nLast updated: {time}\nColumn order: {', '.join(str(i) for i in key[0][0])}\nColumn shifts: {', '.join(str(i) for i in key[0][1])}\n\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			end = 0
		)
		(columns_order, shift) = key[0]
	elif rows==26 or rows==25:
		text_key = filter_text(input("What is the text_key?\n\n").upper())
		columns = len(text_key)
		if rows==25:
			text_key = text_key.replace("W", "V")
		shift = [alphabet.index(i) for i in text_key]
		reordered_shift = sorted(shift)
		columns_order = [reordered_shift.index(shift[i]) for i in range(columns)]
		best_decryption = decrypt_cadenus(((columns_order, shift), rows), generate_tables(cipher, columns, columns*rows))
	if rows==26 or rows==25:
		print(f"\033[H\033[JKey: {''.join([alphabet[i] for i in shift])}")
	else:
		print(f"\033[H\033[J")
	if len(input(f"Column order: {', '.join([str(i) for i in columns_order])}\nColumn shifts: {', '.join([str(i) for i in shift])}\n\nText:\n\n{best_decryption}\n\nText with spaces:\n\n{' '.join(split(best_decryption))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(best_decryption)