from nostril import nonsense
from clipboard import copy
from wordninja import split
import Fitness
from itertools import product
cipher = Fitness.filter_text("""ATEAASOHPYUDLTEFXTOBTAIJSASGTSRIEDLONINEILEUNIMYTTGIYDIAMOADIOMTPKUHNOUTTHRASMITMIONAEGREHTRIKSGNIASUCETOUITSADYEWAOVFTRROFDGASNGTITNEONTCDAABCMTEMSRIELCECEJTOEEETTBFOHMNORDJOSTHASDWTEFLLAOLRAUDYHSLIIEPIHWUEEPIENFCDOMUCNEONIETLMLESNSIETAOLNOLODIGELMGOLHRCSITTNOMLNKHSINFLGRPNISETCOSSFHNLBFLJDOAOEELAECRTEETMROSNHSHCEESHTIGGOTOIAESNNINIVIMRWOOEEISTERHESSGOSTONOULDEHVSTALEKHHGHHUMPNNASWIENLKAIRNEHTLBUAEEUAYCYELYUDIDEAEWYISIGNAAIUTEHAAHSBOIMALSOEIWYNMEAIAEBTHNCSAINOTTWEPRYIARINEVCDOETDVHCLSKATHAUYENITUEAIATAAOTUAILHLNNSOANBCDONONAEYFNWNESITLVEMNTYIANDAREFMMINLELEAAAAADDOPNIHFYVSKANSOHFOGIOINEPGCSHNNEELIAYHCTATARECTFKFTIUENTEIOTHLSATTEIFIISNEILAEKEADTHTJEENRUUTLETAVTTTODNUHTFHADANLEEBIENOUSMIDTIOITEEOVTHISINASLAORGHHOARDUEWFAORAMKATERRLKOEPHERSLNINSBETEOHNITHCQECESMTINKTYDEINTNETEEHNDNMEAANTIYTOPAUOLPEULNUTOYAREDLEAETAIAALAENRAYAGITMRGDCJDEIEGCOETWOTCOAKAFDCTTRMEEAONENIDANEGAWYNIIIEHIDEHHRRESEDHNCEIKEGAEITAPONOEHTEWNAFNOREHRWTFAYRLSILTNINIETGESRNIETOTIRTERTETOCSHSTORLEESRYHBNATLTOSOITIEASUSSOEIAOELEOSEERMSOYIETNMNHIBGEEHDUKJWNACTETCTSNITEDERAMTENMESOEAYUTUTAIGTKYALOUDTFTEHUDHMSYHHRMTAGMTATPARIENGITAHAATNCSMOHOTKNTERHTOINBITMNBNSRPNIFGOTOHAKISREROSFNTOKSGEMOCUEFRREEITHTORENFISEVSSKHTFAFESNTETHYYCETROOYWBIMGCEIRAUREOSOSACWOASHHEEYCVETATEWDTCBOBTGVTROJSTUTNGTBEOCHOITWTWEKHHPOSINACOROTOAETEEGENLEINHESEOTFARWCOEITTOTIUUCEHTEDOISUROY""").upper()
#cipher = """HELLOTHERE"""
factors=[n for n in range(2, len(cipher)+1) if (len(cipher)) % n == 0 or (len(cipher)-1) % n == 0]		# Gets factors of the length of the text (from the internet)
def decrypt_railfence(ciphertext,rows, starting_offset, direction):
	if rows<=1:
		return ciphertext
	table = [[" " for j in range((len(ciphertext)))] for i in range(rows)]
	flag=direction
#	flag = 0
	y=starting_offset%rows
	for x in range(len(table[0])):			# Add placeholders in a zig-zag pattern
		table[y][x]="0"
		if flag==0:
			if y==len(table)-1:
				flag=1
				y-=1
			else:
				y+=1
		else:
			if y==0:
				flag=0
				y+=1
			else:
				y-=1
	letter=0
	# for i in range(rows):
	# 	print(table[i])
	# print("")
	for y in range(rows):					# Add letters in place of placeholders
		for x in range(len(table[y])):
			if table[y][x]=="0":
				table[y][x]=ciphertext[letter]
				letter+=1
	flag=direction
	y=starting_offset%rows
	text=[]
	for x in range(len(table[0])):			# Read the text in a zig-zag pattern
		if flag==0:
			text.append(table[y][x])
			if y==len(table)-1:
				flag=1
				y-=1
			else:
				y+=1
		else:
			text.append(table[y][x])
			if y==0:
				flag=0
				y+=1
			else:
				y-=1
	return "".join(text)
print(f"\033[H\033[JThe length of the text is: {len(cipher)}\nColumns that can be tried: {', '.join(str(i) for i in factors)}")
factors_to_try=[]
while 1:
	tmp=input(f"Which factors should I try?\n\nall - to try all of the factors\neverything - to try all numbers up to and until the length of the text\nexit - to exit\n\nFactors I will try: {', '.join(str(i) for i in factors_to_try)}\n\n").lower()
	if tmp=="all":
		factors_to_try=factors
		break
	elif tmp=="everything":
		factors_to_try=range(2, len(cipher))
		break
	elif tmp=="" or tmp=="exit":
		break
	factors_to_try.append(int(tmp))
if factors_to_try==[]:
	factors_to_try=factors
Fitness.init()
best_key = (0, 0, 0)
# best_key = (
# 0: rows
# 1: offset
# 2: direction
# )
best_decryption = cipher
best_fitness = Fitness.cal_fitness(best_decryption)
try:
	for rows, direction in product(factors_to_try, (0, 1)):
		for offset in range(direction, rows+direction-1):
			decryption = decrypt_railfence(cipher, rows, offset, direction)
	#		print(f"{best_decryption}\n{direction}\n{offset}")
			fitness = Fitness.cal_fitness(decryption)
			if fitness > best_fitness:
				best_fitness = fitness
				best_decryption = decryption
				best_key = (rows, offset, direction)
				print(f"\033[H\033[JRows: {best_key[0]}\nStarting row offset: {best_key[1]}\nStarting direction: {'up' if best_key[2] else 'down'}\n\nText:\n\n{best_decryption}")
except KeyboardInterrupt:
	pass
if len(input(f"\033[H\033[JRows: {best_key[0]}\nStarting row offset: {best_key[1]}\nStarting direction: {'up' if best_key[2] else 'down'}\n\nText:\n\n{best_decryption}\n\nText with spaces:\n\n{' '.join(split(best_decryption))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
	copy(best_decryption)