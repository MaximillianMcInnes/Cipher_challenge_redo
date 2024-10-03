import Fitness
import HillClimb
from array import array
from random import randrange, randint
from time import sleep, time
from clipboard import copy
from wordninja import split
from math import ceil, log, factorial
from multiprocess import Pipe, Pool
from itertools import permutations, product
import sys, os
sys.path.insert(0, os.path.realpath(__file__).replace("pypy\\"+os.path.basename(__file__),"CPython"))
from IOC import cal_split_IOC, cal_IOC
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_num = [ord(alphabet[i])-65 for i in range(len(alphabet))]

def rand(start_num,x=1,y=5):
	while randint(0,y)<=x:
		start_num+=1
	return start_num

def split_number(num, base=26, pad_length=None):
	split_num = []
	remainder = num
	digits = (ceil(log(num+1, base)) if pad_length==None else max(pad_length, ceil(log(num+1, base))))
	divisor = base**(digits-1)
	for i in range(digits-1, -1, -1):
		x = divmod(remainder,divisor)
		split_num.append(x[0])
		remainder = x[1]
		divisor //= base
	return split_num

def invert_key(key: str | list[str] | tuple[str, ...]):
	inverted = ["" for i in range(len(alphabet))]
	for i in range(len(alphabet)):
		index = key.index(alphabet[i])
		inverted[i] = alphabet[index]
	return inverted

def keep_as_num(prompt: str):
	inputted = input(prompt).upper()
	if inputted.isalpha():
		nums = [(ord(i)-65) for i in inputted]
	else:
		nums = [int(i) for i in inputted.replace(" ", "").split(",")]
	return nums

def key_num_to_str(key):
	return "".join(chr(i+65) for i in key)

def create_sub_table(key):
	return dict(zip(alphabet_num, ((ord(key[i])-65) for i in range(len(key)))))

def encrypt_enigma(rotors_order: list[int] | tuple[int, ...], rotor_positions: list[int] | tuple[int, ...], ring_settings: list[int] | tuple[int, ...], reflector: int, plugboard: dict | None, cipher: str):
	if plugboard != None:	# Through plugboard
		cipher = cipher.translate(plugboard)
	text = array("u")
	rotor_positions = [(rotor_positions[i]-ring_settings[i])%26 for i in range(len(rotor_positions))]
#	print(rotor_positions)
	rotor_turned = [False for i in range(len(rotor_positions))]
	notches = [{((notch-ring_settings[i])%26) for notch in rotor_notches[rotors_order[i]]} for i in range(len(rotors_order))]
	reflector_used = reflectors_dict[reflector]
#	rotors_subs = [rotors_dict[rotors_order[i]] for i in range(len(rotors_order))]
#	inverted_rotors_subs = [rotors_dict[rotors_order[i]] for i in range(len(rotors_order))]
	for character_str in cipher:
		
		rotor_positions[0] = (rotor_positions[0]+1)%26	# Rotate rotor(s)
		for i in range(1, len(rotor_positions)):
			if (((rotor_positions[i-1]-1)%26) in notches[i-1]) and (((rotor_positions[i]+1)%26) in notches[i]):
				rotor_turned[i] = True
			else:
				rotor_turned[i] = False
			if \
					(i==1 and ((rotor_positions[i-1] in notches[i-1]) or rotor_turned[i])) or \
					(i!=1 and rotor_turned[i-1]):
				rotor_positions[i] = (rotor_positions[i]+1)%26

		character = ord(character_str)-65
#		print(character)

		for rotor_i in range(len(rotors_order)):	# Through all rotors
			offset = rotor_positions[rotor_i]
			character = (rotors_dict[rotors_order[rotor_i]][(character+offset)%26]-offset)%26

		character = reflector_used[character]	# Through Reflector
#		print(character)

		for rotor_i in range(len(rotors_order)-1, -1, -1):	# Through all rotors backwards
			offset = rotor_positions[rotor_i]
			character = (inverted_rotors_dict[rotors_order[rotor_i]][(character+offset)%26]-offset)%26

		text.append(chr(character+65))
	text = "".join(text)
	if plugboard != None:	# Through plugboard again
		text = text.translate(plugboard)
	return text

def modify_plugboard_key(settings):
	plugboard = settings[-1].copy()
	for i in range(rand(1,3,5)):
		while 1:
			rand_letter = randrange(65, 91)
			if plugboard[rand_letter] == rand_letter:	# Create an new plug
				another_rand_letter = randrange(65, 91)
				if plugboard[another_rand_letter] == another_rand_letter:
					plugboard[rand_letter], plugboard[another_rand_letter] = another_rand_letter, rand_letter
					break
			else:	# Remove a plug
				tmp = plugboard[rand_letter]
	#			plugboard[rand_letter], plugboard[plugboard[rand_letter]] = rand_letter, plugboard[rand_letter]
				plugboard[rand_letter] = rand_letter
				plugboard[tmp] = tmp
				break
	return settings[0].copy(), settings[1].copy(), settings[2].copy(), settings[3],  plugboard

def try_rotors_order(rotors_order: list[int] | tuple[int], reflector: int, cipher: str, pipe):
	try:
		if not (\
				(len(rotors_order) == 4 and (({8,9}.intersection(rotors_order[1:])) != set())) or \
				(len(rotors_order) != 4 and (({8,9}.intersection(rotors_order)) != set()))):
			best_IOC = [cal_IOC(cipher) for i in range(3)]
	#		print(rotors_order)
		#	for unpadded_i_rotors_position, i_reflector in product(product(*(range(26) for i in range(2))), (range(2) if (len(rotors_order) == 3) else range(2,4))):
		#	for i_rotors_position, i_reflector in product(product(*(range(26) for i in range(len(rotors_order)))), (range(2) if (len(rotors_order) == 3) else range(2,4))):
			for i_rotors_position in product(*(range(26) for i in range(len(rotors_order)))):
		#		i_rotors_position = (0, *unpadded_i_rotors_position)
				i_IOC = cal_IOC(encrypt_enigma(rotors_order, i_rotors_position, (0,0,0), reflector, None, cipher))
				for i in range(len(best_IOC)):
					if best_IOC[i] < i_IOC:
						best_IOC.insert(i, i_IOC)
						del best_IOC[-1]
						pipe.send((i_IOC, rotors_order, i_rotors_position, reflector))
						break
		pipe.send(True)
	except Exception:
		exit()
		
rotor_names = (
	"I",
	"II",
	"III",
	"IV",
	"V",
	"VI",
	"VII",
	"VIII",
	"Beta",
	"Gamma"
)
rotors = (
	"EKMFLGDQVZNTOWYHXUSPAIBRCJ",
	"AJDKSIRUXBLHWTMCQGZNPYFVOE",
	"BDFHJLCPRTXVZNYEIWGAKMUSQO",
	"ESOVPZJAYQUIRHXLNFTGKDCMWB",
	"VZBRGITYUPSDNHLXAWMJQOFECK",
	"JPGVOUMFYQBENHZRDKASXLICTW",
	"NZJHGRCXMYSWBOUFAIVLPEKQDT",
	"FKQHTLXOCBJSPDZRAMEWNIUYGV",
	"LEYJVCNIXWPBQMDRTAKZGFUHOS",
	"FSOKANUERHMBTIYCWLQPZXVGJD"
)
inverted_rotors = [invert_key(rotors[i]) for i in range(len(rotors))]
rotors_dict = [create_sub_table(rotors[i]) for i in range(len(rotors))]
inverted_rotors_dict = [create_sub_table(inverted_rotors[i]) for i in range(len(inverted_rotors))]
# rotor_notches = (
#	 "R",
#	 "F",
#	 "W",
#	 "K",
#	 "A",
#	 "AN"
# )
rotor_notches = (
	{17},
	{5},
	{22},
	{10},
	{0},
	{0, 13},
	{0, 13},
	{0, 13},
	set(),
	set()
)
reflector_names = (
	"B",
	"C",
	"B Thin",
	"C Thin"
)
reflectors = (
	"YRUHQSLDPXNGOKMIEBFZCWVJAT",
	"FVPJIAOYEDRZXWGCTKUQSBNMHL",
	"ENKQAUYWJICOPBLMDXZVFTHRGS",
	"RDOBJNTKVEHMLFCWZAXGYIPSUQ"
)
reflectors_dict = [create_sub_table(reflectors[i]) for i in range(len(reflectors))]
if __name__ == "__main__":
#	cipher = Fitness.filter_text("BBQREQFTOOHLURMLNEGTNBWAWMKNKHTPOTJWAAOUEOZEMSIDTUAWIPOFCXNUHHRKKJJGCPPSUHJNOCSHSQTVYJDUMRQNMZKKGGNEFENIOMJDHUMRIUWTHRZREPTTNGOQQWBKJCCWZSLMWZFLDIGWTEIYOAESLZFMMQWIOOSATGEMURYBCGLHJXDHYBNWCBMKROGCCBLKKQTJBINBZBBGCTUXQMTJOPRWIKCGHPMVJZSMPORBAKHYFILLNIKZXINWWBWZVVZOXLUJJUAZJNDBGBDJCPMZGVHAIKFDNHDOQSXRBKYNYNUQCQEFPUWDWBLQJJRWYGWVTPVEERBWDCFGFAZQMILHXAWPVQFNCLHFGGCNTDLWKTCOBWNXFBBSTCMMMBBFFMRIKKLXPUCPTVKUBYOBEIAOMJZLQSYOHAFDFZXEVCHVUJMDHILUKLLWZVITVIKUXQICBYELVFEYFYYKPFKVPKULUJJTRJOVEXXZDXPURKXRMGGUTGWSFYOQKEYMLAELCYPLZWWWJIISUANRVYEBKEDOMPDQCYBIRHSPYLWNUHTBJIQHIDHRGFBFNUVZBFKIYWBMITDFWZSJAVDSDNJCRJNNMYIBIMHVFKHXPVIHFTJPKCBOHWFQZIZBVPJTWDTJBJZUXONQYBFXYLXYAMHOUGJAOHZQSFMKBURGBXYJUSNGPCSXLDBQBWRCBOLJBHTPVFEWYQZVMHFLIYXAALRZQGJEKJMBIORPHTCNMSRFLMDJXCTVEKTPKZQGNVCDHFRNVAMGQTGLVSKJMNDUNZADARKAACTORAJWDEXPWQHEXKZJTSJGCJCKBYYQRDGNBTLZUGEYRIJNERNCEANFXLPCCIEQCCOSIKBWRXVSBVIHHYHKQXHBACRFGHFOGDCJXVUCNJYVINXRWRGZYLIUGYNQMDUPPXBJPJUTPJFQOYOSLAFXOVNAHBXEBIJQLMUIYUDNCKEPGYNYOYVYTWDULPBLHPEZEHCRLXYWUBKBPKUZMKKFLWJZTQVIQUBQJHQRZJFOSENJWTHYOYMRLMNLMJOXVOLQQQDRSSNFJZHBQYFLBXHQCEKEXCXAMCJYSRPHYCGQLZTWAKUAKEADWRFUQPRUTTXHCMFLGMWAXAQLRNCLBSVZAJCYYBCPFSZHLSKTFASBJVSBYCKYFFXPATZFHQCDPSEEZTYFFQKUWSIOULWOTKWVEMUCDHRYCHWAXHXYIJDDOYLKNJBYNAPYWPJFODWBXWCGKKWKFMSRCWFCRQZVZEPRFKKEAUBSPNCZMYTKCSSYTMAWYTMSIZJUXFLTBAIIDLJOHCIJALGZUQDORVHXOKVUJVVDEUPVBLNGRMJUVQYKTVBFNNRFDYHZULMGUAOPBFOJFRUUCWTFOCOVAIKMLGMIFKOJDHWGDIEYQOZXCGIHFHQDKLWAGCFRQEAXMWIRCGPWVWXPKVXDLSBZIHUIFKUTBTLKTOVHNLF".upper())
	cipher = "RGHLXWERJFEBKJCTPQSRUATXSECVANAMVCINKFDITERSWSKYZGWPCFFOFDOKNIXNQEKLERJOOHYHNRNLCRTFPGBLQSLRRIZGNPGNIRBCPEYFRZQIYEEFSGATAQUILXWVEKWKVKGLPXLSZSXDDKEPLTBYFVEOIBVONXCZDNSDUBZSCVCYOPPWZKWJEBNDZIRDTEPPOAGCMEAPVFQKAHLDGBHUVYFPROLVATDHAZXUIBOIPQBYFKMEPPVVARYWVDWAXQNXDVDPEJLRLCIZJZTXTOHGEIJVRIZXKSRDPYVCTAKEGKQNLDERCEDRCLCCBZODUFQYKKGFVHKIJQOATHAJDDBYJHVHYGJBPYDFCFSGBCVLXLMKPYHQVJNRXRTBXFEBZCJROUGTJTFCZRANOMSOELCISWAAZRFXRTATPUDSXSQAWFHVPUKBGRGFKDJJLCPAPMSCRLSNMVIYCJQNTYKDJYCFLZYGWYMIEKDEOKDGCHIUYVUMPYAJLMIRHIQJUMHHPQFWDRCTNXFFZGKYEGQHANWZZGLXUBFVSOITYKNMVEQIHPGWSXOHTRBUAPLIXFFDVVTUSBMXBIUFYDTGRWNRBLEKVUUPQZCTHDXKMAFJAEBOOKYONGCLASSICALPCRYPTOGRAPHYPYRKBLPJZGAEMXDVWKZZAEQSLZZQRJNPXBYLMADNESSCTDHTGNOVLJVYICAIYFYFHGRYTARUVQRVPKEJYGBEAEOODQYCUTZKPGLVCLBVPQXSTCTQXEOQPJUJASKXJECBYOKMAOWPSKORUKVJALEVGUKCMCZHSLVQABOFSRDZDEMGKXOBLNPMVYWHNKOKWPDHMFNRFEFRAWSLLLHDNRIHULIIZINDCSTLSXIDACDHFSWEMAEEJYEUYKTGIIKBXKXBCDRGKLMBDQDKHTGUTVRQWVFVKPWVBZMMYYPKJDDOCYTXXUANBVRYQHLIVHXUFOKHNIZTRIFAWIJYYBSPUWIBSFPGRGUYOZXFJEGXCXDZCASLGATBUCNLFDEFCXQEDDLMOGNWBXILJZXNIEOAOPZCSMMSOHEAHKLJGZGBYPEOXBNXYRTBCGYHFKBABNPBNJQJSASAMDHDCRBCEUABZWELSYAAKHWVMIOXDZLWJATETKKBWURJZXOOADHKRTWNOHUYABNJTZBLLUFCABCIVAZMFRQXOVXKAUNGIXHJPRDYUDDRZBHCVFXWMYGEXBSVCXXGPPHDFGNYGEZCLEBTSQTZVJMXANBJTARBNSOEYVCKGJPIAWDCKOBHNHWDBEIZSAAPPYEEPIYRIIDGPNLPJKSMKMPYHGHLNOUKJWVLIGMJTWDLGSIKCZYDZXQKTIUHSHFOIZGALHUKLJYWMLZKAHIKYYSVTZSNCNYYMEKUFFLVFQVYZUVKLBIATHFIUCOCZXIBFKAYXHYKHVFZHZCCEQZMOWGNWTTQSTWWGUZBVDVKRCXDHBNQWUTPTMWSWMORMGCSBUXVKDFPNXGBHIGEHQPLAMEEZAMRYGOVMXSHEIVBTWFZBCLZAMSZCMRRYTNPZBCCXXRBTWSYLSHAYYOWIBMUPVDNPLKHFRVFBQYVLUHQRPRNBJMQGUKAWXDFOYOYUHFBNKLIWFVIGPPVXMXJNVWGNJYKEPETARKUBCUSENVPLXHJXOZIDFJDTCMHXSFQYLCZSZKTHGRYEGLKAYIKEDELBENHXYOWHRNYYTGIEXQBBHRQNCIAVFECUPPQDGBDAKGUZCVRZKEFHSIPXEQUZDVYHLDBEFFJVDCEPBRQOXDPDBGSKJPENTXKXQKVHSJPBJKXEFNFCDVHVBTINYQWSWKHHXTQLSXFENSAUXSWCPONSMJQJRUZTUFZFBIEQWURUGARGKKNJBBAJRBKONNLOEHVLOSHZLBVSAPYBLZAQNIWFRRERAYVLKAMHWBRVBMWCWZAMJUIJJAPXAORHSRJOKDCDCMMHAXLDJEXNKGUAHXHXUADUSYNCWGJSUDCHILOARNSVCZTYNYAIRCDCEXYMVVJGLSCHCFCCAKRDMLVPWJMTOHDIZQIAUMASURABZGQXLLZQGDVONRWLTFXFCAXKIOXPEJEWEGRKRQJEFWLXECDVAAEBAIWIYBQEYUGNWUYOMDDJAZAXEUZAHGHJVCTNRANPRATWUFWKHJRRPDYSPAUHEIOJLOOPTJMJIPVVMRBSTSQTKIOJJHQAWEYUOOOUWOEMJMMADODRWSHTDZACWDUGNOMKAJJYKCNYUSQMSOEFMUGLSWNTTBMLJHBHGBZWXBKLATDDCIWOSQNUJZAOUKJPBDWAEJSAPIWLBZIIRPIJYCTNYKSMCCWAVKNQUKTNYKMJBFLPCKASFTVCVGALIJBPHMU"
#	cipher = Fitness.filter_text("BINWMQMSVNIIRJJZGPOGEZUVIMZCGJHTMRMNBTIAQIKNQDIABKHGSRXYXGFGXWSGNWXKOJWVEQIJFZQBMVGHHWUNPHCRXGZMBYSUXUDWPGDVYYQXUYGVSNNYBKVCPZVHCSLZAJEFBMXZXKBLDKSMHIWLYRVGHXRKETRVXURDNGKHUGGPVCHLECMGGTBKREUXKERXSMOYHIFQATCYSSWTQFCGPACXCECCYQOFXFYFIAWUAHUOZZJZXYOSUAPHPIQAPQIAAYLWFKFSKWCOJVGKSMQXQRQKFDEXVXRUGJVUQKJQEHMCILMBWICWPNNXYMKOSPZUXEZRIPNEHFAXCZZXHPIYEMWARCEICJXHHXEQVOYYXWGXBEZKJIGLTTCTWRWUKZMNZMYFJLCFPRTMMBTTOCMPBWHLUNQIUEDUBPXMMPXKHVJXGAAWKNVUCLVKYPZMMSBIENUSHBDODKUFFGJAXLYGIQMXNNMNKUESQCNAOOZEBWWHZLWVGRGYKDDUMHMEOVTVBSWELYYDCYCRIXFCPJDAOPBXZVAWTGHHIOOVKOPJAPJWKYAZMLRQZSOLODQRIDPEWTQFKVGXYYGKYNNFAFLTQWOUDXLFDGZUJOWGXBSKSVSNZYFSXLSEXOHQZMKGXYUPCLGOFDZMCSZJRPQLFMRAOUGRTWUIVZNVHWJVJKUDFNTJNNVEIYTKAJXUZXMYNRGKIJWXVCQAAUVSUSEVQEFGMLZFPDLTNBOTOZQRAEZVJMTPMBXXGPCSGXLGSPMYDSEJDNNGCSUCZIBBRKJMOCALPREWDUDFPSMVVQHVKASSTRLUOAFGETLYXHPBSGYPDLQJIYPTGGTNPGOYAPFGEPUZTYZXWQYPNJXZXHSVPBDHSIUSNVCUZXWELJDBPJKJMPVQQOGGLMXMLAYJIMYAFUHVHVKLQGOGAVTVNMPPVZWICQXFIYLPJNNEVEPUCWTLSMLFHMBGWTJRWWYAJOQHFTKJYXRZTTABHUSSWVSUOZYXACFCHJHDAXRKXZZWFMMUWXACGGQMPHULJUPGDQEFBAAERSPKNSIVPZRKYISMVGSHYEEDPGQPLKJFJACQJSMGTECNKIVOSUABRYWFSXTFEHSGUQVOCBLKMXUVJMAFUXNXGBUTNXBUYYCXKGUEVTAEECJYFSSSUMSHGWNVGOKXEDZLLOAUFJNYUKOUFTPQOJPQKFPHBIPCKFWIFXYMVWRSZVXQZKYNZLITMDFXWLDLDJASTHTIVHUTMJKNXMDPSVJAJBXAKQFNZMJRLBRXXKLNAAKOMXFUDHFODADQSNWRWHAKBQLBBRMQVIORVSFNYOSXRYQOZKHIULISCXYKFHH".upper())	# I III II, COD, THE, B, A-B, C-D, E-F, G-H, I-J
#	cipher = Fitness.filter_text("JXSUWDHUALBXCVJWVCQYBNDYGKJAOWFMODLWWLMGTHIBNRPUMAKJUINIAHXQYGBWNXYSYRKVCTHSSVZGGNMHVILHYEBDOAXLHFMFMRXPTIQZFFPCRLWNZYRCMOLORKFHCPFQZGIQNBZRWVTOJGPJPWFBRACSGLKZCCAOQBADUXECNVTLTPEIVHKZQILMWEZFXVUSCDJMTKGXNBFSTTMGPLHTOAOPISYLPRFYDYJAUTUQZDJQLTKVUHJUPRLTLZFIRXOVUJMKVCKNXEIHIOQMUWIWMFUDKXILBILRSPAWRZZOTDHGXNLEVVPPKXJFEBIULPQTIRSZPESGJRNFRXTFMEODSTIRKDXBJMSICJKTEDUVUVNHSJKTDYNRGQPPHVPBCYYCMUVQZVUAOEWAFEAJBHDKLETEYLISXJHBLOXPSEGKMZUKUMESLYUNLWBAJXMWUCTZHEWIBFXMGHYTVKGJENITPXLZYHKMWXKGPAINSZGVCJBUNNVKISKHDEXQQAQXNGMQBMDLNTIFNYYMIILCQFOZDJMHGHXBJLXABFCWDTFBHMRKTXDATXQYFSVQZOPFAMODVIOKPKWACVYAIUSFSSFEITISQXFTPGGSUKWNQEPHKJLKLRKJGMEQODVGDXLXLKGMATALUAGQKUOEHMVYMRFSSEVXWGPCKXJZIXBGCLQZRAOWRZAJQEAEAUISOJFKXROCYOYTRASCVZOMNFHYHBXACTOBBFOVXEORMFIGNKVTSZHYMNWFHVQZVCJTOXXENKPYVXREEJJRMLKQDCBQSBMLDDVNDJYPJYJCUONAMXKXVXBZWPCKNIBGGOFGYURGRWLPAPXDDUCMQNHSBQSPNDXCUEVLNOAYAVHUHZLHDVQAUQNELKEXKYEZOOZMHPXGIUTQPDIJSYRRIONTCLWARDEDRYKCYIGUVQQWOMRWTRJADPPJOIMAPWIAFSTQBSSKUALMXDRAWSGLUUEOKGOWSEZGPEWWMFUWFZZZVQDESIJNDSZJXEQPASCLZEXQYGMWVOWFPQTBJKQFQQCEGFDDZQAWAFNCXDBXOWXHNHVEUWNWALRJCJIBRMLDEZWZKBJFEPIIWRKGVBHFEOKLJKWJQTMWYUERPDYEKYVJIDVABLSWUZHJGKPYGPJPCDXFHMGGMAXTSKLQWTIQGDTYMONHFLVLIRIRSNPCCJGPIYFJMUJVVKRACYCMRYMWLNUDBIDVFOFRRWSCEMLXYVZVNROYGYTXRFKMLVYUKCNNGEPFTLXQOPGXJLJAGMJDHKBKLDTKQJPTLBMNYMIVUVHBYUEIWPBMPEATUNCJUIAUUWKSNJCSEWMTNJUVSCHBAQFWOEZ".upper())	# I III II, COD, ACB, B, None
#	cipher = Fitness.filter_text("YSSWDLBUBEEVFEJINZNWSJDJBHZFZMRUXFBFORATMIKISUCNSFEKFMTYKDRTVTUVPLCTRQPTZGLHRYGQISIOMROKYKEJEURRTFSZWZXOJSFSNFNQRZPDIWPLGSACAZXWJSTCLFRIGNBQGXAUUHVSENGUAHWACPWUBNEEMUOFQHMDEJRHZDQPCAAVJFBACMMMKKVRIPJSTBNCQFFPFQFHEYHUVAOUIEREVQGCAFQFHRFYNHXDUFFGEVZIKBVRBXMGVARYIVKVKALFGFCRXLKYGHPTUQWFCWZNNVRTVWFZHGYZLUIJSSAYKOMZISDYGPLRETVWXXZKRAKHCEUCLDPSDVLTIFOQRGDWJXLHLPFHGCCCJDNSQYYUDLSMLQBGWQGRRJNWVKQACKCOUPGPAPLUVJPIVSBBSXACRFDOUBSLRHYVUFZNHTACWBRATZNVRCPDBUALPFSAVPJCAKBXOJLKVGSVLIZGZVSCGXHGQKIQSBJYJGALNHBKBXGODGMQUMKQRJUZQEWVPLPTHPKTVEENMDGYRDCYAUBKSPZMVBLISVYXDDOPBATRAGYGLLHKBELCMOREPUKPSZVZKECPFTIBQEEPCTSPVHMJKDMUJQLZWLJUGCNGBENHOPWAQFCBCNRLGDAJOPCDUITUAWMYLFLFRMKCUDMGZVJLAFYYTZVPHFCZTOCXMXMLQPDATQOKOHEWFDRWOGRQGPMNSZDMPURNBEJILICROREMCPVUGATYVFPDBWKSYURYAZVENRUEWWRSZWWTEAGUSPZUZMGHRRJXMCQMGAJMVYJDDTIWOUIXCQQMJNEGZJLJRMQYJRNXQZVBNGFIZSSWXQZIEPEQEBURFHVVIKNRJIRWFBOJSVUITLXUHXAIBYKVZATQIPLYJSIPUWJTPDEFHLFIJGLPYSEDPHDRWDMCCNEDSSXLJDQZOSOSGJCGNLXMEZLTPGWBAGYURQFVIYCNBEZTPPSFOCJRHWCOKMUIQGSFTSKJIEVGQXNFYQITOSVOURGQFUJOGQAZZIOXXNIRQPXKWHEOBEBZMDGRGWKFDVFTLCPBISAESLBKOFGOQSIQRCSXWTGYEVYNCIFFJEACMCAXHRNOAPGTHPXVVJCSIRVXWZITRSRLIQYYRVGHKQIUYSZNNLLAACCFTVMELISFFOMYUFKWYZWVTNPTNLFQXSLHEVPSMCHATSUFQMAGXWRHLMZGRKWSOCXOSNMUZGFYYOYBWKWEUUMWWAXPDWDUJGZJYEGWPMYFWQFQFGIFQPNZASQCANNGOWWGNDMWPDMDKRTUUFYIYULNVVGMUHPSZJUCUIVSODRNBRTZLPXQRWTLKUACNUGBUFH".upper())	# I III II, COD, AAA, B, None
#	cipher = Fitness.filter_text("QKRQW UQTZK FXZOM JFOYR HYZWV BXYSI WMMVW BLEBD MWUWB TVHMR FLKSD CCEXI YPAHR MPZIO VBBRV LNHZU POSYE IPWJT UGYOS LAOXR HKVCH QOSVD TRBPD JEUKS BBXHT TGVHG FICAC VGUVO QFAQW BKXZJ SQJFZ PEVJR OJTOE SLBQH QTRAA HXVYA UHTNB GIBVC LBLXC YBDMQ RTVPY KFFZX NDDPC CJBHQ FDKXE EYWPB YQWDX DRDHN IGDXE UJJPV MHUKP CFHLL FERAZ HZOHX DGBKO QXKTL DVDCW KAEDH CPHJI WZMMT UAMQE NNFCH UIAWC CHNCF YPWUA RBBNI EPHGD DKMDQ LMSNM TWOHM AUHRH GCUMQ PKQRK DVSWV MTYVN FFDDS KIISX ONXQH HLIYQ SDFHE NCMCO MREZQ DRPBM RVPQT VRSWZ PGLPI TRVIB PXXHP RFISZ TPUEP LKOTT XNAZM HTJPC HAASF ZLEFC EZUTP YBAOS KPZCJ CYZOV APZZV ELBLL ZEVDC HRMIO YEPFV UGNDL ENISX YCHKS JUWVX USBIT DEQTC NKRLS NXMXY ZGCUP AWFUL TZZSF AHMPX GLLNZ RXYJN SKYNQ AMZBU GFZJC URWGT QZCTL LOIEK AOISK HAAQF OPFUZ IRTLW EVYWM DN".upper())
#	cipher = Fitness.filter_text("OZLUDYAKMGMXVFVARPMJIKVWPMBVWMOIDHYPLAYUWGBZFAFAFUQFZQISLEZMYPVBRDDLAGIHIFUJDFADORQOOMIZPYXDCBPWDSSNUSYZTJEWZPWFBWBMIEQXRFASZLOPPZRJKJSPPSTXKPUWYSKNMZZLHJDXJMMMDFODIHUBVCXMNICNYQBNQODFQLOGPZYXRJMTLMRKQAUQJPADHDZPFIKTQBFXAYMVSZPKXIQLOQCVRPKOBZSXIUBAAJBRSNAFDMLLBVSYXISFXQZKQJRIQHOSHVYJXIFUZRMXWJVWHCCYHCXYGRKMKBPWRDBXXRGABQBZRJDVHFPJZUSEBHWAEOGEUQFZEEBDCWNDHIAQDMHKPRVYHQGRDYQIOEOLUBGBSNXWPZCHLDZQBWBEWOCQDBAFGUVHNGCIKXEIZGIZHPJFCTMNNNAUXEVWTWACHOLOLSLTMDRZJZEVKKSSGUUTHVXXODSKTFGRUEIIXVWQYUIPIDBFPGLBYXZTCOQBCAHJYNSGDYLREYBRAKXGKQKWJEKWGAPTHGOMXJDSQKYHMFGOLXBSKVLGNZOAXGVTGXUIVFTGKPJU".upper())
	#print(encrypt_enigma((0,1,2), (0,0,0), (0,0,0), 0, None, cipher))
	#print(encrypt_enigma((0,2,1), (2,14,3), (0,0,0), 0, None, cipher))
# 	import cProfile, pstats
# 	with cProfile.Profile() as pr:
# 		encrypt_enigma((0,2,1), (2,14,3), (0,0,0), 0, None, cipher)
# 	stats = pstats.Stats(pr)
# 	stats.sort_stats(pstats.SortKey.TIME)
# 	stats.dump_stats("stats.prof")
# 	exit()
	if int(input("What do you want to do?\n\n0 - Enter Enigma settings myself\n1 - Solve Enigma settings\n\n")):	# Finding enigma settings
		rotors_used = int(input("How many rotors are used? (3 or 4 is preferable)\n\n"))
		reflector = int(input("What is the reflector you want to use?\n\n" + '\n'.join(f'{i} - {reflector_names[i]}' for i in range(len(reflector_names))) + "\n\n"))
		option = int(input("Do you want to find?\n\n0 - Plugboard configuration using hillclimbing\n1 - Ring settings (with corrected starting positions)\n2 - Best Rotor permutations and their starting postions (which is w/o ring settings)\n\n"))
		if option in {0,1}:
			rotors_order = []
			print("Please choose the Enigma rotors from left to right.\n\n" + '\n'.join(f'{i} - {rotor_names[i]}' for i in range(len(rotor_names))) + "\n")
			for i in range(rotors_used):
				rotors_order.append(int(input("Enter rotor index: ")))

			rotor_positions = keep_as_num(f"Enter rotors initial positions{' (w/o ring settings)' if option == 1 else ''}: ")
		if option == 2:
			best_IOC = [cal_IOC(cipher) for i in range(3)]	# Finding rotor permutation and starting positions
			best_rotors_order = [[None for j in range(rotors_used)] for i in range(3)]
			best_rotors_positions = [[None for j in range(rotors_used)] for i in range(3)]
			best_reflectors = [None for i in range(5)]
			completed = 0
			possible_rotors = rotors if rotors_used == 4 else rotors[:-2]
			total = factorial(len(possible_rotors))//factorial(len(possible_rotors)-rotors_used)
			# import cProfile, pstats
			# with cProfile.Profile() as pr:
			pool = Pool(max(os.cpu_count()//2, 1))
			pipes = [Pipe() for i in range(total)]
			result = pool.starmap_async(try_rotors_order, zip(
				permutations(range(len(possible_rotors)), rotors_used),
				(reflector for i in range(total)),
				(cipher for i in range(total)),
				(pipes[i][1] for i in range(len(pipes))), strict=True))
			# result = pool.starmap_async(try_rotors_order, zip(
			# 	((0,2,1),),
			# 	(reflector,),
			# 	(cipher,),
			# 	(pipes[0][1],), strict=True))
			stop_threads = False
			update = False
			try:
				while not result.ready():
					sleep(0.2)
					for pipe in pipes:	# For every rotor position
						while pipe[0].poll():
							received = pipe[0].recv()
							if isinstance(received, tuple):
								for i in range(len(best_IOC)):
									if best_IOC[i] < received[0]:	# Add the new rotor position received
										best_IOC.insert(i, received[0])
										best_rotors_order.insert(i, received[1])
										best_rotors_positions.insert(i, received[2])
										best_reflectors.insert(i, received[3])
										del best_IOC[-1], best_rotors_order[-1], best_rotors_positions[-1], best_reflectors[-1]
										break
							elif received:
								completed += 1
								update = True
							if result.ready():
								update = True
							if update:
								print(f"\033[H\033[JCompleted permutations: {completed}\nOut of {total}\n\n{round((completed/total)*100, 2)}% Complete\nBest rotor settings:\n\n" + '\n\n'.join((f"Rotors used: {' '.join(rotor_names[i] for i in best_rotors_order[setting])}\nRotor initial positions (alphabet form) (w/o ring settings): {key_num_to_str(best_rotors_positions[setting])}\nRotor initial positions (numbered form) (w/o ring settings): {', '.join(str(i) for i in best_rotors_positions[setting])}\nReflector used: {reflector_names[best_reflectors[setting]]}\nIOC: {best_IOC[setting]}") for setting in range(len(best_rotors_order))))
								update = False
			except Exception:
				stop_threads = True
			if result.ready() and not result.successful():
				stop_threads = True
			if stop_threads:
				result.get()
				pool.terminate()
				exit()
			del pipes
			pool.close()
			exit()
		elif option == 1:	# Find ring settings
			plugboard_known = int(input("Do you know the plugboard?\n\n1 - yes\n0 - no\n\n"))
			if plugboard_known:
				Fitness.init()
				fitness_funtion = Fitness.cal_fitness
				plugboard = list(alphabet)
				while 1:
					inputted = Fitness.filter_text(input("Enter a plugboard pair (enter nothing to stop configuring plugboard): "))
					if inputted == "":
						break
					for i in range(2):
						plugboard[ord(inputted[i])-65] = inputted[1-i]
				plugboard = str.maketrans(alphabet, "".join(plugboard))
			else:
				fitness_funtion = cal_IOC
				plugboard = None
			best_i_ring_settings = [0 for i in range(rotors_used)]
#			i_ring_settings = [0 for i in range(rotors_used)]
			best_i_rotors_positions = [0 for i in range(rotors_used)]
			best_fitness = fitness_funtion(cipher)
			
			for subtracted_rotor_positions in (
					product(*(range(26) for i in range(rotors_used)))
					if plugboard_known else
					(rotor_positions.copy(),)):
# 				i_rotors_positions = rotor_positions.copy()
# #				i_rotors_positions = [0 for i in range(rotors_used)]
# 				i_ring_settings = [0 for i in range(rotors_used)]
# 				for index in range(rotors_used-1):
# 					for i_ring_settings[index] in range(26):
# 						i_rotors_positions[index] = (subtracted_rotor_positions[index]+i_ring_settings[index])%26
# 						i_decryption = encrypt_enigma(rotors_order, i_rotors_positions, i_ring_settings, reflector, plugboard, cipher)
# 						i_fitness = fitness_funtion(i_decryption)
# 						if best_fitness < i_fitness:
# 							best_fitness = i_fitness
# 							best_i_ring_settings[index] = i_ring_settings[index]
# 							best_i_rotors_positions[index] = i_rotors_positions[index]
# 							best_i_rotors_positions[-1] = subtracted_rotor_positions[-1]

# 					i_ring_settings[index] = best_i_ring_settings[index]
# 					i_rotors_positions[index] = best_i_rotors_positions[index]
				
				for i_ring_settings in product(*(range(26) for i in range(rotors_used-1)), range(1)):
					i_rotors_positions = [(subtracted_rotor_positions[i]+i_ring_settings[i])%26 for i in range(rotors_used)]
					i_decryption = encrypt_enigma(rotors_order, i_rotors_positions, i_ring_settings, reflector, plugboard, cipher)
					i_fitness = fitness_funtion(i_decryption)
					if best_fitness < i_fitness:
						best_fitness = i_fitness
						best_i_ring_settings = i_ring_settings
						best_i_rotors_positions = i_rotors_positions
			print(f"Best rotor initial position: {key_num_to_str(best_i_rotors_positions)}\nBest ring settings: {key_num_to_str(best_i_ring_settings)}\nBest Fitness: {best_fitness}")
#			print(cal_IOC(encrypt_enigma(rotors_order, rotor_positions, best_i_ring_settings, reflector, None, cipher)))
			exit()
		else:	# Find plugboard
			ring_settings = keep_as_num("Enter ring settings: ")
			text, (rotors_order, rotor_positions, ring_settings, reflector, plugboard) = HillClimb.hill_climb(
#				lambda x, y: print(*x, y),
				lambda x, y: encrypt_enigma(*x, y),
				cipher,
				lambda x:(x[0].copy(), x[1].copy(), x[2].copy(), x[3], x[4].copy()),
				(rotors_order.copy(), rotor_positions.copy(), ring_settings.copy(), reflector, str.maketrans(alphabet, alphabet)),
				lambda best_fitness, time, best_key, decryption: print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nRotors used: {' '.join(rotor_names[i] for i in best_key[0])}\nRotor Positions: {key_num_to_str(best_key[1])}\nRing settings: {key_num_to_str(best_key[2])}\nReflector: {reflector_names[best_key[3]]}\nPlugboard: {' '.join(f'{chr(i)}-{chr(best_key[4][i])}' for i in best_key[4].keys() if i < best_key[4][i])}\n\nText:\n\n{decryption}"),
				modify_plugboard_key,
				iterations=5000
			)
	else:	# Choosing Enigma settings
		rotors_order = []
		rotors_used = int(input("How many rotors do you want to use?\n\n"))
		print("Please choose the Enigma rotors from left to right.\n\n" + '\n'.join(f'{i} - {rotor_names[i]}' for i in range(len(rotor_names))) + "\n")
		for i in range(rotors_used):
			rotors_order.append(int(input("Enter rotor index: ")))
	#	rotors_order.reverse()
		rotor_positions = keep_as_num("Enter rotors initial positions: ")
		ring_settings = keep_as_num("Enter ring settings: ")
		reflector = int(input(f"Enter the Reflector index\n\n" + '\n'.join(f'{i} - {reflector_names[i]}' for i in range(len(reflector_names))) + "\n\n"))
	#	print([rotors_order, rotor_positions, reflector])
	#	exit()
		plugboard = list(alphabet)
		while 1:
			inputted = Fitness.filter_text(input("Enter a plugboard pair (enter nothing to stop configuring plugboard): "))
			if inputted == "":
				break
			for i in range(2):
				plugboard[ord(inputted[i])-65] = inputted[1-i]
		plugboard = str.maketrans(alphabet, "".join(plugboard))
		text = encrypt_enigma(rotors_order, rotor_positions, ring_settings, reflector, plugboard, cipher)
	if len(input(f"\033[H\033[JRotors used: {' '.join(rotor_names[i] for i in rotors_order)}\nRotor Positions: {key_num_to_str(rotor_positions)}\nRing settings: {key_num_to_str(ring_settings)}\nReflector: {reflector_names[reflector]}\nPlugboard: {' '.join(f'{chr(i)}-{chr(plugboard[i])}' for i in plugboard.keys() if i < plugboard[i])}\n\nText:\n\n{text}\n\nText with spaces:\n\n{' '.join(split(text))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
		copy(text)