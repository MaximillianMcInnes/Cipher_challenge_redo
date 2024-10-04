import HillClimb
from random import randrange
import sys, os
sys.path.insert(0, os.path.realpath(__file__).replace("pypy\\"+os.path.basename(__file__),"CPython"))
from IOC import IOC_columns
from math import ceil
from array import array
from clipboard import copy, paste
from wordninja import split
from Fitness import filter_text

#cipher="""SIJKJ BZTYS KYZZL APNAE PAQHF AWGEU WPPPS OPIEN NPTXE BWKAQ UMFZW HQEZT EPSIA MFXOJ MMTIE LEQDE YWLOP ZQVWM SKHPQ TYLAT XVGMP VLBCM DRDCJ XTSFH HEZHT VLAPP GNDMZ HWLOT DQFOZ TNXOU SBDQW PLAUE PIJEJ DWKJI FQTWM LLJGN EBZXW QTKLZ QMSMS MEIUA PLWQE ZSVEN JHXPW KDXWE WAGNE PWKOM WILBL TNPEX YBLHT BEHCM GOPZL APMXY ZZLTY LEHYM QLSMK IPVLM CGAGR BGXDB SUWQK APDAW PVUXN WFGPK LBYOL APPGN DMZHW LLHEP WTEBW FABWW EPWYE AZHHA ZHHQE IZZLT YBAMH IKMZP WKTAA MAWKL TJDXE PSMTB OTDVL KZOWK DEZHZ ZYTYQ KXOBZ XEPWY EKGNW LKHXM GGPQF MSMET YWJAL DWALL SZCCV ZPIYT TVKMX IALTM KMPID BYOXK ZULAP TAUCI JRDMW FDTAD PIYHZ LAYNW FOZTM MPLOT JBGZP BSMSM JBHWM EOTAD PBGKP IVFZZ WHQUS BDQWL EPGNR PLLMC LLSMO TDDWK JKSKP NMESM JWTIJ RAIYX DEWKP MFVCG HMPLO BEPSA ZALHQ LAYQM JXYBU BAPWK DIFWL ALBXM OXYBG GDPWT OIHMP LSGOA LKPVY MSMFX OBZXX BZBDW FXWWG DDPSK OJMMT BALCM SEWGH KPBLR PIKRE PWELB WKZVW LRMLT WWLMZ CYAPZ SGJES RHMFX PLLHA TSGZC JGPFL LEMHL NWMEO GGNEZ QMZOW MLTAL EWXMS MEXXJ WKDWX KZOWK DPGND MZHWL SGOUS DPMFJ FQJBP ASUZC LMSME BEEGN WLTXR WGWEW CGZEA YEPWK PESLL VQHYM OAZPS WLZWT DWFMZ LALWQ CXXIA LTMOX DPGNW LFHEL ALNWM GEUSB DQWLE PWHCG LALBL APBZX QBOTD XSKEW XTYQF LFZSG NMKVL UWBEP WKMCL BQQFW TBZTC LLHMM DBPDW MSILK ZOWKD EGNWL ZTGMJ BDSWW SQKKP XMMLB AHYIF WSQKV SIFVP WXMSM YHGMJ GZZKA TXWOP VAYSM OTDAZ HCBGY XWFXJ XWHAT WETSW ATUUH FTVND CSEWG XBYLK HXMGG PBGUL KCMSM EBWWG DQWJP LZVMZ PWTCQ FZQZG FJWMC ZLAXA AOALB SKPGG NCMSW TVYKT OZMYW O""".upper()
if int(input("Where do you want the text to be from?\n\n1 - My clipboard\n0 - I want to type it\n\n")):
	cipher = paste()
else:
	cipher = input("What is the text that you want to decrypt?\n\n")
cipher = filter_text(cipher)

def unlink(instances: list | dict):	# unlinks nested lists and dictionaries
	instances = instances.copy()
	for i in (range(len(instances)) if isinstance(instances, list) else instances.keys()):
		if isinstance(instances[i], (list, dict)):
			instances[i] = unlink(instances[i])
	return instances

def modify_key(key):
	key = unlink(key)
	key[randrange(len(key))] = randrange(26)
	return key

def generate_table(columns, rows, cipher):
	return [
		[
			cipher[(row*columns)+column]
			for row in range(rows)
			if ((row*columns)+column)<len(cipher)
		]
		for column in range(columns)
	]				# Create table from the cipher

def decrypt_vigenere(key, table):
	columns = len(table)
	shifted_table = [[] for x in range(columns)]
	for y in range(len(max(table, key=len))):
		for x in range(columns):
			if (len(table[x]))<=y:
				continue
#			print(y, len(table[x]))
			shifted_table[x].append(chr((ord(table[x][y])-65-key[x])%26+65))
#	shifted_table = [[chr((ord(table[x][y])-65+key[x])%26+65) for y in range(len(table[x]))] for x in range(len(table))]
	text = array("u")
	i = 0
	try:
		while 1:
			text.append(shifted_table[i%columns][i//columns])
			i += 1

	except IndexError:
		pass

	return "".join(text)

#exit(decrypt_vigenere((2, 20, 11, 15, 4, 17), table))
if int(input("0 - Hill climb to solve\n1 - Solve with key\n\n")):
	key = input("Please enter the key:\n\n")
#	key = [ord(i)-65 for i in input("Please enter the key:\n\n")]
	columns = len(key)
	rows = ceil(len(cipher)/columns)
	text = decrypt_vigenere([ord(i)-65 for i in key], generate_table(columns, rows, cipher))
	key = [ord(i)-65 for i in key]

else:
	columns = IOC_columns(cipher)[0]
#	columns = 7
	rows = ceil(len(cipher)/columns)
	table = generate_table(columns, rows, cipher)

	text, key = HillClimb.hill_climb(
		decrypt_vigenere,
		table,
		unlink,
		[0 for i in range(columns)],
		lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nKey used: {''.join([chr(i+65) for i in best_key])}\nText decrypted with key:\n\n{decryption}"),
		modify_key
	)

if len(input(f"\033[H\033[JKey Used: {''.join([chr(i+65) for i in key]).replace('[', 'A')}\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
	copy(text)