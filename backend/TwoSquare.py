import HillClimb
from random import randrange

def fill_key(combination):
	for letter in alphabet:
		if not letter in combination:
			combination+=letter
	return combination

def find(to_find, to_find_in):
	try:
		index = to_find_in.index(to_find)
	except ValueError:
		exit(f"Could not find {to_find} in {to_find_in}")

	return divmod(index, 5)

def decrypt_two_square(key, cipher):
	text = []
	for i in range(0, len(cipher), 2):
		coords = [find(cipher[i+j], key[j]) for j in range(2)]
		# print(coords)
		# exit()
		if coords[0][0] == coords[1][0]:	# If they are on the same row
			text.append(cipher[i:i+2][::-1])
		else:	# May need to swap these 2 statements to suite your needs
			text.append(key[0][(coords[1][0]*5)+coords[0][1]])
			text.append(key[1][(coords[0][0]*5)+coords[1][1]])

	return "".join(text)

def modify_key(key):
	key = key.copy()
	to_modify = randrange(2)
	key_to_modify = list(key[to_modify])
	letters_to_swap = (						# swap 2 random letters in the key
		randrange(len(key_to_modify)),
		randrange(len(key_to_modify))
	)
	key_to_modify[letters_to_swap[0]], key_to_modify[letters_to_swap[1]] = \
	key_to_modify[letters_to_swap[1]], key_to_modify[letters_to_swap[0]]

	key[to_modify] = "".join(key_to_modify)

	return key

if __name__ == "__main__":
	from Fitness import filter_text
	from wordninja import split
	from clipboard import copy
	#cipher = filter_text("""ENEAO TAQKD UQXNI IVBQZ RAXNI ILOQA XTMNQ AUWOH CPGHI CAQSC OGYHG NTTWU HPAPA RHHKM NNMGP PMLQA GHVQU PILOP SPLAU PWQKG GRFAV BEDRL RAIBA QAIDN RFQDD NUFUM OBAQU VIKEE HHMNQ AENEA QONTO VKGSB IHQPE NXATU MCOPK ZTAOT KPKHP OWHET VBYTW MSLID SBFAD SMDYT BPXTG MSQXN AWFAV BEDRL RASPP BGHFN PFQPX OXTLA MXAQL KNDZP ILNWA QSLGK OHVBM IPPTA QAKPY TVGMX AQQUH HXNQO KHQOP NEKXA KZNTQ VNLHH EMUHY HGNTT WUHPQ UQELS IDSBS GTIIH QPETA KWHNL WMCYV BKPKP WYSLW GDSWU FAWTW HSBVO TLENK ZNYWF PYHPN IIDWH SHNAX NVBIL NHRSS OKHQO QPLAS ZWWQE AMAKZ PAIHH SBOZK ZQFKK LACFX YDTFA SNPHS QOBSQ LAWMN NMOWC XTWGR TNBVB AQAKI QXNSB WBPHW GKKLA GMMLT NRTWY MANAW QKGVM WHXAS QKGXA KERAQ RSFVI MWNHU IIQWZ ENSUW ZENID SPRBQ GCMFA WPLAZ WAQAI HHSQP NAKMC OPHPM DQKFA UHSKX NVMBY FHAIU MOBAQ TGLBS LVBEI WFEAV ONBEM FHSBO ZVBIL NHRSS OKHQZ VBHHK CUWIK MDYTB PAEAD SQPBG HIDSP FAVBI IMXAQ UPTIY NRIXT SZSKS LVBSQ XTIKU QIQII UPVQX NSPRP WZADX OXTVB ILKPZ WRPQS FADSM AXTMB OPVBA IEMWB SHQGU NMILN DSVBS KVBSX CFTII BMRMI NWSLV BAIIK KNNNQ AHNRP QSQGT NNDOW VBAIW HETXT QFDSM BWFQM LAGPK GRTHH VBAII DOPPH EAGPM LQEXA SPFAV BAXRP QSQGU NSLHP XOSSS LKNIL KNSLH HELEN SPNNS OBYFH SCFAM NUGMD NEVII PMRSL GKOHQ ULTRA WFVQT ANSWU KPYTV GOWLA XTRAA KIIRP HYWHN BLSWM ONWXV BAXKG RSSGN DILWB PHGKO HOMWF LTVME MWBUW IKXOF EHNLN QOWHE MCPLA XATUH NIQNB EDWYQ OAQBY OWIKO QEIAK SLWHL ARDRT WHLTV BAQDT OQQNV LSLMA XTLKP SRHLN WGHKO HSIKK LAQFW OYSRK ASRSK PAIWZ OGYHG NTTWU HHXNQ AHHKM OPEIN SEAVB SIWYK YNAPK MLIZY TTZNS DTSBP OOHAX SRVBS KVZOW SLKPS GTIIH QPFAD SETII VBSIW YKYNA OROPF LQAKB QOIIE NSPOP MXMLQ KKZWO OHUMO BAQVZ RHHHK MFAVB AXRPQ SVBII LSMIO NQELT SPOWK PKATT BYHPN BLSWM QPLAS ZWWTT VBAQV BIDFS EAVBA QHPKQ FAWPL AKDUY AQLNU VRPQS ETSBV ANWAQ SLLAF AANNN WOSLN BVBMX MDXLI DMPTL QEWWN BVBAL QHHQI DSBET QEMXS LVBSK VBEIQ PIIWB MDQDV ONBFS EACFT IANSQ QHRMI ZWHET AKVIK DWMVI SKMIZ HDHWY QOAQQ YXOQA AQWOQ HAHCB QOIIW BPHTA QANBL SXTSP LAKDU YAQLN WOPBH PSGQO ISWBR AOZNS QABYP BALMI LNDSA WRPQS NBLSW MLAET WOOQH NMCOP VBILR HLNWZ FAIHQ BENSK FAVBI CSSSH RAWGQ GWMFA VBICS SAKTT OZSLK DXFQH UFWYT GIQWH CEWZW PLAQE AMAKC PPPEL KDVYG HXANE VBMQT LQEWW NBVBA XOPHQ VBSLM LVBYT TAIAK NIITN QKKGU CKZMF ADAIB PMIFE OPKPF BHBSS QGXNO TAKLL SHOGB PIZAI AIWYT GIQCF TIIPW BNDET MDFWS CKDVI IBHPS FSWSK VBMCQ HWHKK LANSS NAQMG WQIZH HKFRA NBRPU TIQTB OPLTW YIQVB ACNHA NUCID SBOFS LFNXN QRXTM DHPSL VBSKG WIKHH XAWYR PWAID LTWML AQIQE EAQYH YUWMI PKIIS PLASF RBKDT TNAQR WZTAQ AVBMC OPLTW UFAAN ELQAI QGBRA SPONS LSQIL TNMFS CYTTA SFWQW HXTQF DSKPB YIIVB ICRPX ALLEI AQIIX NXTMN QAXAS COZVB ALQNY HSQRP TNVAX TADVB SKCFL LMXAQ CHRAH HVBEL IKUWH HKYUW IKWHO PHPKX WHTNL LVBAL QHKIP AIQLA FAIPE LQZWP LAXTI DSPLA XTYTV GQHRI OPXPQ ZWWWH XTNII SSCWP OHBPU QOQHP MLQAH HKPFN OKMIL NKKLA QIQEE AXKHN FIDNW OASQE VZSLV BSKVB SLMLV BYTTA NAIAK NIITN QAWZP AIIQP KZOZF AMNRI AKIIT HZNEL POWHR SQGWT ADAES LEDAK TBWFQ MLAAM RBIIQ EAMAK YHSSE NWFHS RPVMS QLACN WFRIS LVBSC NVIQW BFTWB PHQUL SAKNB SBVAN WAQZW IKMDR SCESK SLEMV HOWKP SBIHQ PXAAI CYXAW HXTDS MDVBM CISWP FAWPL ASFRB YTTAK DUYAQ CPQNP POWRP QSRHI IIDHH DSWOG BSKKH QOFAU HGBKO QERZV BSCQO XMENW MOHMX FNQUO QHHXN TYWYI IMNQA WGLHX TNLXT MNNAQ KAQNA WBDSW OTTXN KUGWR PQSUP CPRPQ AAQQY RAOMW FLTVM MARFS EHFKD UYNWA QQGUT BPUCL TWOHH KMFAV BAIGB KOFAD SETII HHCDN RSLWG RTKGC YQOLA ENSKK ZOQEI AKSLI DQPSQ FAVPE LRTSP QBRFQ EMAXN KZNTQ AKZSB WBQOL ASYQA HHKFK KLASF RBAKT TOZHH FYOPK PWHET SBVAN WAQSL HNAKM CTIQR OQEIA KSLSK TTFHN BMXKN IIEAQ ERZHH GFUMO BAQWO QPLAS FRBXA NDAQV ZRHHH KMFAW PKZUV RPQSM AWOII RPHYV ZSSOW NWAQK ZUOEI WQSKK HQOFA VBAXR PQSLS MIONQ ELTSP PPTNQ ASHBF GKOHV BELRS SOKHN AKKAQ RMIZR LVMTL SBOZI DSBRM WOSSQ YVBHH WBOZV BSKGH GBKOE TKDVT SLWHR QMFHP KOLAM XKNII EAFBL ASBIH QPAEX TAIUM OBAQT AVOII XNSPO WKPKA TTBYH PNBLS TTQAW HNTHH TNHHV BILNH RSSOK HNAWP LANTQ GWYSB IHQPV BHHKC CFTIE NDSUT ILEDA SRSNB XOIZI SVPID SWSQL AXTFN NTKDU YAQSG POQCT TSZWO IDANN SEZNT FHAQE MVHQP ADUQE NXTTT QAWGW HQUQE AMAKC BFADS QDDSS BTNQA MAXTM BOPKP KDWMK ZWMCW MLVMI DSBFA DSVBR PHYVB AKMNS FWQKG CYSGT IENPO UQSCV PLKXP XTQYV OYTVF SLRNV GQPQD DSKPI KKNNN QAIKV BMIGN TTWYI DTTVB AQVBI DVBMI ACMDO WRAWY FASHN GCHRA YTCPR HWFXN SOKPH BMRIQ RLQOV BMIIK VPHWD NAKVO QDYFZ PEINS SZOZM LIZID ENDSW USFRB HHVBI LNHRS SOKHO VKPFA KDUYA QCPLA OPGBH HMDWZ LLEIH HASQH KLEIP PKPOP CBQOL ASZWW CYVBI KNTND ROOTA QNBQU FSCDU QKPAX OPHQP HIEKN ENPOL ANEET KZQAV BAXQH EHIDM IQEOZ HHQUW FOHUV FAXND SUFHP UVAKR AENSZ ENWOQ NOWKP KOLAS FRBWZ PZAQQ EAMAK ZWLAQ ZADKF RAQUQ EAMAK ZWFHO KAISE PZKNE NQZVP SGNDI LWBPH HHTNS OHHQU CYNDH BMRAI SSMLU MIDLT RTQOT ZOPVB ALQHH QWHET LKNDZ PEQQZ XNSBQ OLAEN QIWZW HWUID MNKKA QIKWC TNMFS CQOAQ YSQSM CHHSL SUVBI QTNXP XNNBQ EQYTN WBPHW OONIQ NHSPL AYNXT WHRHX TSZRP WONHP NFLYT YBOPM XAQID MBAKW HNWMD TLMFS QOPSQ UQQON NFSQY QRVBS KSHIQ QGTWM DXLVB AIVBA QSCTA NTXYS QKDWM LANTQ AVBIL NHRSS OOPUV KGCEM COPVB AICYN DSKRS IKVBM RSLAI PHWOT TXNIB OWRMI ZVBSX MAXTK DVMVL FANTH FFBHN IIVNN HRSSO KHQOL AOQPN ELIPV ZRPQS ETXOI MTNQO FNNSQ AHBMR ACFWI IHHWO XMSOK HPOVB SKQFR ABPKG TIANE QXASP RNWOA SQEVZ SKXMW OLKQA ENSBM AXNSP QPLAS LVLSK KHQGF DGNTT WYIDW OMLIZ AQTAQ ASFRB SYQAA QUVIL IDQGV NPHUP NHVBM CWQUQ ALWQD TMANA THMLW OUPCP PPFAR LKP""")
	cipher = filter_text("""BGYQRABGKNGSBKNDVLZHMNLDIPBGDXFQNDVLQWKIFRQGOCGPSDAEALHITIVDZHBGDXBPHHPZFXIMNBONXODDPHNDVLFQGOEHLCSTAMZNYTDKALONQAAEIMSMEHECUBFKSMGQPGKISMBIAKEIKOSAYMPLCKGQGIWSTPDELCRAAYALYCPUQGEHYCLLBHPHSBTMQDWEINSMTMEHOOALPHNCNNZHELBGDXAIOPECBDDDBKQAEHLCRAMWSDONQDNAQDOPHPOCGMTSMDAETSEHDEPMKIAIRGEHACELZWFGZHALGKSZBPTSSWDKRDOBVFMUCITFDRRLYIFQONSWGOIOGIKLQWECONQAVROPGQGIWSTPDEZWNTTMPHSWWYXDFXBGDXGQQWHRYCFQPHONPLKGGQPMNNZHELHRONQOREEFPGHQTSYCYPKXBQNOGKQDKHTHSTXDSWMABKRECMTGAIFUPZFXYTSLMOQAQDSTTHONDOPIEHTRVRBTALSDFXLCGPPYGQLCMVLLFQDKSDAEEFRVYPRISTBPEHQIONLATHONDWTLGSBKIZPMOCKNOYIUXOAEEKAEVFXNGGQDHQEGGPEHVBDKAPKHLIQMWSBPTSCIPATMBGHNPZCLFXEGBTXLXNPMGWVLKEROOPIBPHSTYEMOONDDSDHQTRYTPHDRATTSEHFOYTIEPMMICMTGUNODPLTFMOOERGBCGQBPHOXOVDZHACBTONOEWSGWZHBNBGBNSDACPHACINBGEGXNPSCIKILNSDBNDRCWPZHIDASMAMLIDENDQMEHEDBTLIATALONREWEREQDOPLLGDWEXNPRMPGQNPSMEHISNOSMVROPYVALREBCMZSWOYRGEHFQKEIVSTBGEGEKAEVFYVMQDEPMZHOTXDHRONVDMVLLEGOPSMZHIBBPHQLLPYKHLIQICUILNNONDOPIEHYTALCRFWDDBKWEWEYTUNSPHKDXWSTHQDBCIYBDAEODQATLDRBCMVBNBKPDVOQWCLONVDKGSMRBAEIOBPSMEHKKBHSMEHRDBCIYLBXODRAICZTGHMBIGHRAEHQWECRGEHVRREICGQSWECCFZHSRLOMVLLUNODPLTGEHEDKEROBTXNXNNDPHONLAAESMMILWXOAEAEAEONLOKLXDONVDPWBHBCRZBLIOPTYPCQMSMOSMEHPYONZHNBHITIVDZHILCRICSHNATHMNBLLONSSWGDQAATEIBPRFAIRYHOREQDBCIPGMYCYTMUPMDOBEPLOTSDEIKOPHFGBKYZYSBPGQLOGMOYKZHNDKHPOFVDPHONQDKQPHNCBLCK""")
	alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	
	if input("What do you want to do?\n\n0 - Decrypt with key\n1 - Decrypt with Hill climbing\n\n")=="1":
		text, key = HillClimb.threaded_hill_climb(
			decrypt_two_square,
			cipher,
			lambda x:x.copy(),
			[alphabet, alphabet],
			lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nFirst Square: {best_key[0]}\nSecond Square: {best_key[1]}\nText decrypted with key:\n\n{decryption}"),
			modify_key,
			same_key = True
		)
	else:
		key = (fill_key(input("What is the key of the first square?\n\n")), fill_key(input("What is the key of the second square?\n\n")))
		text = decrypt_two_square(key, cipher)
	if len(input(f"\033[H\033[JFirst Square: {key[0]}\nSecond Square: {key[1]}\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)