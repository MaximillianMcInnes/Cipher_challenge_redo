#from nostril import nonsense
import HillClimb
from random import randrange, random
from wordninja import split
from array import array
from clipboard import copy
import Fitness


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def modify_key(combined_key):
	key, columns, rows = combined_key
	key = array("u", key)

	rand_num=random()
	if rand_num<0.2:						# swap 2 random letters		20% chance
		letters_to_swap = (
			randrange(rows*columns),
			randrange(rows*columns)
		)
		key[letters_to_swap[0]], key[letters_to_swap[1]] = \
		key[letters_to_swap[1]], key[letters_to_swap[0]]

	elif rand_num<0.4:						# swap 2 random columns		20% chance
		columns_to_swap = (
			tuple(j for j in range(randrange(columns),columns*rows,columns)),
			tuple(j for j in range(randrange(columns),columns*rows,columns))
		)
		for j in range(rows):
			key[columns_to_swap[0][j]], key[columns_to_swap[1][j]] = \
			key[columns_to_swap[1][j]], key[columns_to_swap[0][j]]

	elif rand_num<0.6:						# swap 2 random rows		20% chance
		rows_to_swap = (
			randrange(rows)*columns,
			randrange(rows)*columns
		)
		for offset in range(columns):
			key[rows_to_swap[0]+offset], key[rows_to_swap[1]+offset] = \
			key[rows_to_swap[1]+offset], key[rows_to_swap[0]+offset]

	elif rand_num<0.8:						# Shift a random column		20% chance
		column = randrange(columns)
		shift = randrange(1,rows)
		column_coords = range(column,columns*rows,columns)
		column_copy = tuple(key[j] for j in column_coords)
		tmp = tuple(column_copy[(j+shift)%rows] for j in range(len(column_copy)))
		column_copy = tmp
		for j in range(rows):
			key[column_coords[j]] = column_copy[j]

	else:									# Shift a random row		20% chance
		row = randrange(rows)*columns
		shift = randrange(1,columns)
		row_coords = range(row,row+columns)
		row_copy = tuple(key[j] for j in row_coords)
		tmp = tuple(row_copy[(j+shift)%columns] for j in range(len(row_copy)))
		row_copy = tmp
		for j in range(columns):
			key[row_coords[j]] = row_copy[j]

	return ("".join(key), columns, rows)

def find(to_find, to_find_in):
	for column in range(len(to_find_in)):
		if to_find in to_find_in[column]:
			row=to_find_in[column].index(to_find)
			break
	else:
		exit(f"Could not find {to_find} in {to_find_in}")
	return [column, row]

def decrypt_playfair(combined_key, cipher):
	# combined_key = [
	# 	0: grid key
	# 	1: columns
	# 	2: rows
	# ]
	key, columns, rows = combined_key
	key = array("u", key)
	for letter in alphabet:
		if columns == 5 and rows == 5 and letter == "J":	# Add the rest of the alphabet into the key if it isn't already there
			continue
		if not letter in key:
			key.append(letter)

	table = [[key[(row*columns)+column] for row in range(rows) if ((row*columns)+column)<len(cipher)] for column in range(columns)]	# Put the key into a table
	cipher_list = [cipher[i:i+2] for i in range(0,(len(cipher)), 2)]
	text = array("u")
	for cipher_part in cipher_list:
		coords = [find(i, table) for i in cipher_part]

		if False in coords:
			exit(f"{cipher_part[coords.index(False)]} could not be found in the key")

		if coords[0][0] == coords[1][0]:		# If they are in the same column
			coords[0][1] = (coords[0][1]-1)%(columns)
			coords[1][1] = (coords[1][1]-1)%(columns)

		elif coords[0][1] == coords[1][1]:		# If they are in the same row
			coords[0][0] = (coords[0][0]-1)%(rows)
			coords[1][0] = (coords[1][0]-1)%(rows)

		elif coords[0] == coords[1]:
			exit(f"This cipher cannot have 2 of the same character ({cipher_part})")

		else:									# If nothing else is True then they swap x coordinates
			coords[0][0], coords[1][0] = coords[1][0], coords[0][0]

		for coord in coords:					# Find the two decrypted letters and store them
			text.append(table[coord[0]][coord[1]])

	return "".join(text)

if __name__ == "__main__":
	bogus=input("Do you want to remove bogus letters? (best not to)\n\n").lower()=="yes"
	if bogus:
		bogus_letter=input("What is the bogus letter?\n\n").upper()
	#cipher = Fitness.filter_text("""ENEAO TAQKD UQXNI IVBQZ RAXNI ILOQA XTMNQ AUWOH CPGHI CAQSC OGYHG NTTWU HPAPA RHHKM NNMGP PMLQA GHVQU PILOP SPLAU PWQKG GRFAV BEDRL RAIBA QAIDN RFQDD NUFUM OBAQU VIKEE HHMNQ AENEA QONTO VKGSB IHQPE NXATU MCOPK ZTAOT KPKHP OWHET VBYTW MSLID SBFAD SMDYT BPXTG MSQXN AWFAV BEDRL RASPP BGHFN PFQPX OXTLA MXAQL KNDZP ILNWA QSLGK OHVBM IPPTA QAKPY TVGMX AQQUH HXNQO KHQOP NEKXA KZNTQ VNLHH EMUHY HGNTT WUHPQ UQELS IDSBS GTIIH QPETA KWHNL WMCYV BKPKP WYSLW GDSWU FAWTW HSBVO TLENK ZNYWF PYHPN IIDWH SHNAX NVBIL NHRSS OKHQO QPLAS ZWWQE AMAKZ PAIHH SBOZK ZQFKK LACFX YDTFA SNPHS QOBSQ LAWMN NMOWC XTWGR TNBVB AQAKI QXNSB WBPHW GKKLA GMMLT NRTWY MANAW QKGVM WHXAS QKGXA KERAQ RSFVI MWNHU IIQWZ ENSUW ZENID SPRBQ GCMFA WPLAZ WAQAI HHSQP NAKMC OPHPM DQKFA UHSKX NVMBY FHAIU MOBAQ TGLBS LVBEI WFEAV ONBEM FHSBO ZVBIL NHRSS OKHQZ VBHHK CUWIK MDYTB PAEAD SQPBG HIDSP FAVBI IMXAQ UPTIY NRIXT SZSKS LVBSQ XTIKU QIQII UPVQX NSPRP WZADX OXTVB ILKPZ WRPQS FADSM AXTMB OPVBA IEMWB SHQGU NMILN DSVBS KVBSX CFTII BMRMI NWSLV BAIIK KNNNQ AHNRP QSQGT NNDOW VBAIW HETXT QFDSM BWFQM LAGPK GRTHH VBAII DOPPH EAGPM LQEXA SPFAV BAXRP QSQGU NSLHP XOSSS LKNIL KNSLH HELEN SPNNS OBYFH SCFAM NUGMD NEVII PMRSL GKOHQ ULTRA WFVQT ANSWU KPYTV GOWLA XTRAA KIIRP HYWHN BLSWM ONWXV BAXKG RSSGN DILWB PHGKO HOMWF LTVME MWBUW IKXOF EHNLN QOWHE MCPLA XATUH NIQNB EDWYQ OAQBY OWIKO QEIAK SLWHL ARDRT WHLTV BAQDT OQQNV LSLMA XTLKP SRHLN WGHKO HSIKK LAQFW OYSRK ASRSK PAIWZ OGYHG NTTWU HHXNQ AHHKM OPEIN SEAVB SIWYK YNAPK MLIZY TTZNS DTSBP OOHAX SRVBS KVZOW SLKPS GTIIH QPFAD SETII VBSIW YKYNA OROPF LQAKB QOIIE NSPOP MXMLQ KKZWO OHUMO BAQVZ RHHHK MFAVB AXRPQ SVBII LSMIO NQELT SPOWK PKATT BYHPN BLSWM QPLAS ZWWTT VBAQV BIDFS EAVBA QHPKQ FAWPL AKDUY AQLNU VRPQS ETSBV ANWAQ SLLAF AANNN WOSLN BVBMX MDXLI DMPTL QEWWN BVBAL QHHQI DSBET QEMXS LVBSK VBEIQ PIIWB MDQDV ONBFS EACFT IANSQ QHRMI ZWHET AKVIK DWMVI SKMIZ HDHWY QOAQQ YXOQA AQWOQ HAHCB QOIIW BPHTA QANBL SXTSP LAKDU YAQLN WOPBH PSGQO ISWBR AOZNS QABYP BALMI LNDSA WRPQS NBLSW MLAET WOOQH NMCOP VBILR HLNWZ FAIHQ BENSK FAVBI CSSSH RAWGQ GWMFA VBICS SAKTT OZSLK DXFQH UFWYT GIQWH CEWZW PLAQE AMAKC PPPEL KDVYG HXANE VBMQT LQEWW NBVBA XOPHQ VBSLM LVBYT TAIAK NIITN QKKGU CKZMF ADAIB PMIFE OPKPF BHBSS QGXNO TAKLL SHOGB PIZAI AIWYT GIQCF TIIPW BNDET MDFWS CKDVI IBHPS FSWSK VBMCQ HWHKK LANSS NAQMG WQIZH HKFRA NBRPU TIQTB OPLTW YIQVB ACNHA NUCID SBOFS LFNXN QRXTM DHPSL VBSKG WIKHH XAWYR PWAID LTWML AQIQE EAQYH YUWMI PKIIS PLASF RBKDT TNAQR WZTAQ AVBMC OPLTW UFAAN ELQAI QGBRA SPONS LSQIL TNMFS CYTTA SFWQW HXTQF DSKPB YIIVB ICRPX ALLEI AQIIX NXTMN QAXAS COZVB ALQNY HSQRP TNVAX TADVB SKCFL LMXAQ CHRAH HVBEL IKUWH HKYUW IKWHO PHPKX WHTNL LVBAL QHKIP AIQLA FAIPE LQZWP LAXTI DSPLA XTYTV GQHRI OPXPQ ZWWWH XTNII SSCWP OHBPU QOQHP MLQAH HKPFN OKMIL NKKLA QIQEE AXKHN FIDNW OASQE VZSLV BSKVB SLMLV BYTTA NAIAK NIITN QAWZP AIIQP KZOZF AMNRI AKIIT HZNEL POWHR SQGWT ADAES LEDAK TBWFQ MLAAM RBIIQ EAMAK YHSSE NWFHS RPVMS QLACN WFRIS LVBSC NVIQW BFTWB PHQUL SAKNB SBVAN WAQZW IKMDR SCESK SLEMV HOWKP SBIHQ PXAAI CYXAW HXTDS MDVBM CISWP FAWPL ASFRB YTTAK DUYAQ CPQNP POWRP QSRHI IIDHH DSWOG BSKKH QOFAU HGBKO QERZV BSCQO XMENW MOHMX FNQUO QHHXN TYWYI IMNQA WGLHX TNLXT MNNAQ KAQNA WBDSW OTTXN KUGWR PQSUP CPRPQ AAQQY RAOMW FLTVM MARFS EHFKD UYNWA QQGUT BPUCL TWOHH KMFAV BAIGB KOFAD SETII HHCDN RSLWG RTKGC YQOLA ENSKK ZOQEI AKSLI DQPSQ FAVPE LRTSP QBRFQ EMAXN KZNTQ AKZSB WBQOL ASYQA HHKFK KLASF RBAKT TOZHH FYOPK PWHET SBVAN WAQSL HNAKM CTIQR OQEIA KSLSK TTFHN BMXKN IIEAQ ERZHH GFUMO BAQWO QPLAS FRBXA NDAQV ZRHHH KMFAW PKZUV RPQSM AWOII RPHYV ZSSOW NWAQK ZUOEI WQSKK HQOFA VBAXR PQSLS MIONQ ELTSP PPTNQ ASHBF GKOHV BELRS SOKHN AKKAQ RMIZR LVMTL SBOZI DSBRM WOSSQ YVBHH WBOZV BSKGH GBKOE TKDVT SLWHR QMFHP KOLAM XKNII EAFBL ASBIH QPAEX TAIUM OBAQT AVOII XNSPO WKPKA TTBYH PNBLS TTQAW HNTHH TNHHV BILNH RSSOK HNAWP LANTQ GWYSB IHQPV BHHKC CFTIE NDSUT ILEDA SRSNB XOIZI SVPID SWSQL AXTFN NTKDU YAQSG POQCT TSZWO IDANN SEZNT FHAQE MVHQP ADUQE NXTTT QAWGW HQUQE AMAKC BFADS QDDSS BTNQA MAXTM BOPKP KDWMK ZWMCW MLVMI DSBFA DSVBR PHYVB AKMNS FWQKG CYSGT IENPO UQSCV PLKXP XTQYV OYTVF SLRNV GQPQD DSKPI KKNNN QAIKV BMIGN TTWYI DTTVB AQVBI DVBMI ACMDO WRAWY FASHN GCHRA YTCPR HWFXN SOKPH BMRIQ RLQOV BMIIK VPHWD NAKVO QDYFZ PEINS SZOZM LIZID ENDSW USFRB HHVBI LNHRS SOKHO VKPFA KDUYA QCPLA OPGBH HMDWZ LLEIH HASQH KLEIP PKPOP CBQOL ASZWW CYVBI KNTND ROOTA QNBQU FSCDU QKPAX OPHQP HIEKN ENPOL ANEET KZQAV BAXQH EHIDM IQEOZ HHQUW FOHUV FAXND SUFHP UVAKR AENSZ ENWOQ NOWKP KOLAS FRBWZ PZAQQ EAMAK ZWLAQ ZADKF RAQUQ EAMAK ZWFHO KAISE PZKNE NQZVP SGNDI LWBPH HHTNS OHHQU CYNDH BMRAI SSMLU MIDLT RTQOT ZOPVB ALQHH QWHET LKNDZ PEQQZ XNSBQ OLAEN QIWZW HWUID MNKKA QIKWC TNMFS CQOAQ YSQSM CHHSL SUVBI QTNXP XNNBQ EQYTN WBPHW OONIQ NHSPL AYNXT WHRHX TSZRP WONHP NFLYT YBOPM XAQID MBAKW HNWMD TLMFS QOPSQ UQQON NFSQY QRVBS KSHIQ QGTWM DXLVB AIVBA QSCTA NTXYS QKDWM LANTQ AVBIL NHRSS OOPUV KGCEM COPVB AICYN DSKRS IKVBM RSLAI PHWOT TXNIB OWRMI ZVBSX MAXTK DVMVL FANTH FFBHN IIVNN HRSSO KHQOL AOQPN ELIPV ZRPQS ETXOI MTNQO FNNSQ AHBMR ACFWI IHHWO XMSOK HPOVB SKQFR ABPKG TIANE QXASP RNWOA SQEVZ SKXMW OLKQA ENSBM AXNSP QPLAS LVLSK KHQGF DGNTT WYIDW OMLIZ AQTAQ ASFRB SYQAA QUVIL IDQGV NPHUP NHVBM CWQUQ ALWQD TMANA THMLW OUPCP PPFAR LKP""".upper())
	cipher = Fitness.filter_text("""GOCLBFAEYTUSBDDKBEDKTIKDYTCQTKUDDQCFKHNHQFXCXNTYAPITXMYTXMSICUMTYTKLQFDAPOOVBCCLHEPTOAFLILTBCLIODNQPCOUTQDDYKCUBOWUCQLAZCPKGGYCQPOCZUKSXCUOYIKPHOYYMQPCIFAACCZCPUDNLYOMHLFUDCLZXDVKGHDCLGKOCOTIODKBLTQUBXNADCLGKOCPBTNPBSIHOHKSNBUPASYUDSUAPNQPBXNABMQABIDFCTHLCOXDBUCOIADOIAEYTPKKUFQPOIRDFMPSNBUKGPOOVYTFATOCTLPPIHOFBOXPOCZAPUCXGPNKHISCAILNVMPYGMHKCTGBLILESTHMHPOHOUDSBKUYOMHKCSBPNNRYGSIOVSCLHQBPHSIDZBQCUYONVPQTHMHLFGTOVOFHIUDSHTWOUOTLCOCOYHTABTHBUYTKBQDHCDAXCTUPNQHQBPHTNHVGKDASICLOYYMQPECDUTOLHFOUSDQDKTIKDTSNYPNDQSICKTYAPSINTKUQFDATUEFDUKCUCESTGYDLISIDKSBOFCPUTAZCPNPUBUCTGPTQNDYFCOSKCCBPHTUKCDQQDHNAEPASYUDSTINXRSIDQOTIODKRHDUYOMHNPUBDBQUOTQTERYOQDNQNTCZBPTUMDABOHLXOYDQOTOSMIDUHOYLQAAEFDNOTYTQUBXGBUDUMILITMNGBUABTHTIKDQCXTHOSIAPDUUDSUKCPSRGBUTHOSKCTHHMHODMPITQHWKBTUTNPBSIHOIMCYECQUSPOFPKOTIODKYMOSFCZABDDAXCTUTYKCAFQPSYYTHNADFKYOXCXNCKHOYOMHSIDQZBXNPTOAUDBLZUMTVBSMHOMRDUFCUTKCHPMYTHBLKCUBCLCTINQPEICZKUBVDVKGDTQEUBOPUTQSBZFCYOBLQDPFHOFBDMQUQDPKFABUXDBQAKQPMPPIDQDTQSEABSZOYTGIBUPASYUDTWPTXNPTOAGKOCCFOIEAONCUQCKBDWSIBZDVSIBUDKXCTNPBSIHOHMBFHKMHDQPBSIDQHDCLURTKUDLMBDDUKCUBHTCLBLDKOSKCTHHMHODMPISIDQHOOWKCBEDQPACQYOXHPOPCDSAEHOTNPBVBDYTYKCLCPBLISIACCLFEOCHDCLUSBPBPCAWBFCSYSIDQDNSCPCDSOTOHRNDVCAOYHTOPYONLMTQDOSERYOYMOSQNCZKUMUPLBUOVSPYOOFDBLHKHQSDKYTQUPODADTSKFAADQBEHAEOTIOCUPASYUDSGABITZASUTYKCDBUCGKPAQCOCQDPKFQNYPIDQSICUKHLCUQUBRNDVCADTSECLGKKRUBOYPTQIMTPBFCSWTW""".upper())	# RSTUQWXYZVBCDEAGHIKFMNOPL
	columns, rows = input("How many columns? (normally 5)\n\n"), input("How many rows? (normally 5)\n\n")
	columns, rows = (5 if columns == "" else int(columns)), (5 if rows == "" else int(rows))
	if input("Do you know the key?\n\n").lower() == "yes":
		key = input("What is the key?\n\n").upper().replace(",","")			# If you know the key, enter it
		text = decrypt_playfair(key, cipher)
	else:																	# Otherwise hill climb
		max_key=["" for letter in range(rows*columns)]
		for letter in alphabet:
			if columns == 5 and rows == 5 and letter == "J":
				continue
			if not letter in max_key:
				while 1:
					pos = randrange(len(max_key))
					if max_key[pos] == "":
						max_key[pos]=letter
						break
		max_key = "".join(max_key)
		text, key = HillClimb.threaded_hill_climb(
			decrypt_playfair,
			cipher,
			lambda x:x,
			(max_key, columns, rows),
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nColumns: {best_key[1]}\nRows: {best_key[2]}\nKey used: {best_key[0]}\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			iterations = 6000,
			adaptive_iterations = 1,
			same_key = 1
		)
		key = key[0]
	filtered_text = array("u", text)
	if bogus:						# Remove bogus letters
		for i in range(len(text)-2):
			if not (text[i]==text[i+2] and text[i+1]==bogus_letter):
				filtered_text.append(text[i+1])

	text = "".join(text)
	if len(input(f"\033[H\033[JKey: {key}\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)