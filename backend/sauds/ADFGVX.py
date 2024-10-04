from random import random
import HillClimb
import Substitution
import Transposition

def decrypt_ADFGVX(key, cipher):
	# key = [
	#	0: polybius square
	#	1: columnar transposition key
	# ]

	columnar_result = Transposition.decrypt_columnar_transposition(key[1], cipher)
	polybius_result = Substitution.decrypt_polybius(key[0], columnar_result)

	return polybius_result

def modify_key(key):
	key = key.copy()
	rand = random()

	if rand < 0.5:	# Modify the polybius square
		key[0] = Substitution.modify_key(key[0])

	else:	# Modify the columnar transposition key
		key[1] = Transposition.modify_key(key[1])

	return key

if __name__ == "__main__":
	from Fitness import filter_text
	from clipboard import copy
	from wordninja import split

#	cipher = filter_text("""GAFAGGFAFAAAAGDAADAXGDFADDGDGGFAGGADFDADDDGAGDFGAAAXAGFFAGGGAGGAGFAAFFGDFDFGGDAAXAGGGGDDDFDDDGGDDFAAAXAXDDFADDFFAFADADXADGAAADAFGGGFXDADAXADAFGDDAFFADGAAXDDGAAGFGADAAADGAFGDAFDXAGFAXAXGXAADFGGDGFGFDDFGAGAFAGGADDGFGAGFGGGDAAADXFFFGAFGDFDDGXGDXDFDXFDFADDGDFDGXFADGDDFAFGGFFAGDDGFAFAAXAAFGGDADDFGADADFGDDGAGGAADFFGADFGGAFGFAGAFFDDAGGFAAFFAGAAADAAGFDFXDFADAFFAFAADFDAAFFAGAXFDAFFDFADFXDFXFDFXFAADAFXGFXGAFAXAXADFDDXFFADXAGFAAGGXAAADADXAGAFDXXAXFDADFFAXFFDAFFXXAXDAXGAFXAGADAXFXADAAAFFAAAGDAFFFAAXADXGXAAXAAAGAAAXXGXXGAADXXDFXXXGDXXADXXGFFDAFAXDFFFAAFAAXXGXAAXAAFAXXAAXAXXXFDGXDFDAFDDDDDAAXFXFXDAXFAFFXXAGXFAGAAFXAGFFFXDFFAAAFAFADAXADXFAGGAAXFDGFXFFFAAFDAAAAGAFFAAAAFFXFXAAFFAAAXAFXXFAAFGFAFXFXDXADXGXFGAAAFXGDAFAAFAFAXGXAFAXAXXXAGDAXGADAFDADXADXXXFADDGFAXGAXAGAADFXXXAGAFFAFAAFAXFXGAGAAGADADFXDADGXFFAFAGADDDAFXDAXFDAFGDFAFXGAAAXGDXFXDGFXAFAGADXDFGAGFXFXAADGAFFADFFDFFFGGDXAAGDXAAXDDAAGAAXFDAAXAFADXXAAFAAADXAAAXDXXXXXXGAFXFFAGFAAFFFAFAAAAXGADFGXFFDXAFGFADDDXADADAFDFFFAAAXFDXAGAAXDADFXFAXFAXGAGAFAGXXFAAAXFXAAXFDFDFAFXFAFFDAAXFXGXAXDAGFFFFGAADAXFAAXFAADXFGAGXXAAFAFAFFFDDXAADADFFAXFFGFFXFXXXAFXXXXAAXXDAXAAXDAAGXAXFFGAADDAAXDAGFAAGGFFXDXGAFFAXFFAADGAXAGFAFDFXXAAXAXFAAAAAFDXGXGAXAFXGADGAXFXAAFAXGDXFFAXFFAAGDXXAADDAFAFXGFDGDDDAXFGXDGFAAFGXAADFXXGAXFADXGFAXXXGXAGAFFAAFFGFDDADDFDFAGAXXADFXADFFAXXXAXADFFXXAAAXFAXXXDDGXXFFAAGXFAAAFAAAFDXAFADAGAFXAAFXGFDXAXDADAFADAXADXADXAFFDAAFAXAAGAADXDXGAFFFDXFGAXXGAXXDGAAXFAAAGFFDAFXXFDXDAAXFFAFDFAGDFFFAFADFDAFFGGGAGAADDGGFDAXGFGADGFFADDGGGFAFFDADFAFAAGDDXAGDDFAGDDGDDGAFGGGDFAFDDAAGDDADGGFDFFDGFGFAFDDAAAGGAFDDGDAAXDDFAAXAXDFAGDADFFGXFDFFAGAGDAADDAAADAAGDDDFFDFGGGAFGAGADFGAAGADADFDDDFDADAGGAFDDGDDAFGFADGFDFADADGFAADXFFAADDGDGAFGAGFDDAAXAGGGDGAGFADAXDDDDAGDGGFFFFDXAAFGAFFFGADGGAGAFFDAXAGADFDFFADDDFDDADADAGDGGAGXFFDFGAAGFADFDFGXDAAGGDDAGAFXXDGDFAGAGGAAADXAFADDFFDGFGAGADGGAGGGADDFAFDFAAAAAFFAADDGDADGAFFFXADFAAGAAXDAFFFXAGADAFFAGGAGXFGGGAAAGGGFFGADGFFFAXFAADADADDDAGGFAFAGFGAGFDAADDGGADFADDFADFFGFGFDADAGFADAFFADFGGDDDFDFAAGAFAAFGDFDAFDGAAAGFADFAFGGAADADFDAXGADGGADGADADDGFGGGAFGGFDGDGADFGDXAAAFFDGDDDDFXAADGADAAAGGAFDFAAAADDGXXFGAGDAFAAGDFAAAXDFAGGGGADDDXGDDFGAFFGGAFAFAAADFGDFFAFXGGFFADGGXDAGADGDXDFXXXXAFXXXGDXAAFFXFXAFAAGDAFXFFFFAFDADDFDFAFFAXDFGGAFAADDXFAXFAAXAAAXDAAFAXDDXAFDAXXXAGFAFFAXAAFFFAGGAGADADADAAAXDDFGGXAADDDDAXFDXXGXADGFGGDXFADDXXAXAAFGAAFAFXADADDAFFFAAFDFGDGFFXAGDGFGAFFXXFADFFAFDFDFXAAAFXADAXFXAFAXXXFDXDDFFAXFAAFDFAAAFGAGDFAFAAXFAAXFXDFFADAXFFFDFGXFAXFGDAXAXGFGAFXDXFDDADFFXAAXXXDXFXGADAXAAAAXFDDAXGAAXADAFAGFADAFAXFDFFDADXDAFGAAXXAAXAAAFGAGADAGGGADGGAFFFAFGGAFDAGDGAGDAGGADFFAFAGXAGGGADDDGXAAFXXGGFDFAGFFAFDGAGGFFGDDDDGGAFFADAFFAGAAADGDDFFDGGDDGGADXAFGFFFDAGFDDAFGGGGDDDFFFFADDGDFDFGGAXAADDGAXGDXADAGXFAGDGFFXAADAAFGDAFGFXADFDXDAAAGDGDGGADGDADDAFAFDAGDGAGADGDFDFAFGGADAAGDDGGAGGFGDGDXFXGGFDDGADDDAGAXDAAGAGGDDAFAXDFDDDAFFGFADFAADDGFXGFADFAAGDAFDADDDGDDXGDDGDFADGXAGFAAFAGFAAADADAFDDGDFAAFGD""")	# ADFGX 8 columns
	cipher = filter_text("""DADFFFVADFFFXFFAAVFVFFDAFADFVFDAVVAVDFXGVGVAVVVFXAFAAVVVXDFVAFVAGDAAVDDFVVVFDGFAVXGFFFFAVVVVFFGFVDAAFAAAFGVXFGVVADXGAAAFFGXXXGADVDFDAAAGFVFAXDVFGXDDAAGAAAFFVAAFVDAGXAAVVAVVGADGAAVDAAXAVAAAVDFVFDDVVVGDDAFAVAVFAGFFDFAVVFFFVXFXGVDVDVAVVGDFFGVAFAGDFVVFDAFFFVDGVVVXFFVVDXDAFDVFVAGGDADFAAAADDFVXGFDVAAAFDFAGFAFAAXFDVGAFDVDXVFDAGFVDFVAAVVXADVFVXAAGAXFDFDAFVFAAVDAAAAXDXXADDAFAGDVADDVFDXDXFAXFFFXFAAVDDGVDGDADAGDGAVAXVGAFAFGDFDAADDXAAFVAFGDFAFFXGDGDXXFFGDXFFFADFXXDGXAXGDDGAFDFAXDXAVAAAFFDADDXDFDFDAGAVXGXAAGAAAVAADGXVXGVAAFXGFAGGGDVGXXVXXVADFAFAGFDDFADAADXXDGAXGAADAGXXAGAGXGAFFXFAXXDVXFVFAAXDXFXFDXFDAFXXAVGFAFAADGDVFAAXVDGAAAFAAAFAXXFGAADDAAXAXFGGFDFAADFAXADDADGAAAXFFXDXAAGFAAAXADGXFADDVDADXDXVGDFGFXFVDAAFXFVAFAAFAGDGDGADAXAGGGAVFAGVAFAFXXFXAFXXXFDVFFFDXDAXDVAAVFXXGAVDADADADDAXAXFAGAAVAXAVFXVXFVXFFADAVAVFFXAXFAXFFADVVFDFGDDAAGDFXFGFVAXADAFAVGFDFAFAGDXAAVVDFGDVDDFFDFVDFXAADFXAAXVVADVADXFXADXAFAVGXAAFAAAVGAAAGVGXGXXGVAAXAAAVFDAAFDADAAAAXVAFAFGDDFXAFVFAFXFXDVAFAGFFFFAXAXDFXAFAAXVAXAXFDGDDXFADDFAVGGFAAXXDXADGAFGFFAAGADDDVAAGAXDXAXFXVFFDFFDDVDXDAXGDADVGFFADGXXAAAFADGGVXGADXAXDAAXFFDAFXDGGGADXXGGAAXXXAXAAXXAAVGAGDFFAXXXAAXVXFDADFFFFGVGDXDDAGAFAXXVDXAVAAFXDGGAAGDGDXAAAAFVXVGVXXAAXGAVFAGFGDDAAXVVXDDXXFFAAVFGGDAVVXADAGGFFFFFVAXDFXVFDAAFFGAXVFGGFAGAAFGGAAGXGFGAVAGAAADFVFVXXFVFVDAVAGGDVDXAXDFAXXXDXDFDFXGAAAXAAXXGXXVXXFAFDFXFDAAFAAAAFXAGAFAGAFXAADGDGVGAXVAFDFDFAGAFXAXGFFDFADDAXAAVAAVXVXVAGFAVXAVAXXFAXGFDAAXDAAAVDAFDAXXAFGFDXXVDFDFDAFFDDDADXFDAADDVDGXFAXAAFVVGXAVVFFFFVDAFGVFFDADVVAFDAVAAFVAAAAFFDADFGVAGGXDFVVFDADFGXXGVAXFFVDFDDGVVVDFVFFFFXFVFDAVFFAAAFGDXAAAAVDAFFAGDVVVVGDDXVAVAFXAFAFXAAAFGGFVDFVFVDAVFAVAGDFAAVAFAGDFFFDGFAFFFFDFVFVVADVVAVVDFDAFAFFDAXVADDAXAFVAVADDXFVGFXAVXVVVFGAFDXAAAFFAGADVFVVDDVAAAFVVADDDVAFGFAFAVDVXVXVAVDVVDAGFFDVAFAAAXGAVVAVAVVGVFAAGDAFVGDVAFFFFGFVAVADVVGDVDADADGAAAFAADAGFDDGVVDAFXVFVXVFVAFGVADADFFAAADVFAGVDGFVVADDVAAFDFFFAAFGADDVAAVXAFVDADGXVVVFVVXAAVFFVDDAAAVDDAAVXAAAAAGFFAVVVAVFDVVAVVFFAGAAFAFDAFFDAFVDFDFDAAFXFDXVFDDFGDFGGAADVDXAVADXADVFVVAVAFFFAGDAFDADFGAFFFADVXAFXVDGAGDXGXFFFDFVFXVFVVVVAFAADVFAAAADVAVVVAGDVAAFVAVAXAFGXDVDFFAAAVDAVDVAVFADXAGFVFAAVFDAGVVFAAFFVVFFDFADDFVAVADAAAADFGDVXDAFVDVAFVFAGAVAFVFVXDGGXXDDGGGDFXAADAGGXADAAVXAFXDDFFAAFAFVAVFAFADXFDDFAFDDFXXFAXFAXGAADGXADADXXVGAGFXXXXAVADAAAXXAADDADFAFAVDFAVDDAGFVDVFGAXFFFVAGFXXGFXAVDGDVFGFAVFGGAXXADFAAFADXDXAVFADAFADFVDVVFDFGAFFFFFADAGXFAXDFDAVDXDXADAFXAVAXDXAFDXXXAFGFVGDDGFADFVDAAXGGAFVDAGDAGDAAXAGVFGDFAXAADFDGXDDGFVVXGAGDDFADGXXAFVAFFDXAAGXXVXDXGAFAGDXAAGFXFDXVAXGDFAAAGFDFADDGFFDDVAFXFADFADGXADGAFAVDADAVAFVVFVVFADDDADFFFDFAFADAFFAFDAFDDADAVAAGDDAFAGGAAAVAAVVDGDFGDDADVVAGDDVFFAVFVDADDAFFVDAGAAAFVGADDAGFFVFAAGAADVDVVVAFDGAADGFVVFFADDDVAGGGVVVDAVXAXXGFFAAFGAAFAVADAGGVDDAAFVAXDAVADFDAFFDFVVAAAVAVGDGXGVGAFAADFVGAFFDAVAAFAVAVXDVFFFAAFVFFFFDDDFAVVFVAFVVFFVAFFVXFAVFXAAAVFFFADFVGDFAGADVVVXFDAXAFDDFVDXFVAAFFADFAGAGFAFVVVGFVDAAFAAFDXFDAFDAAAAAVXVVAFVDFXVGA""")	# ADFGVX 8 columns

	is_ADFGVX = int(input("What version of the cipher is it?\n\n0 - ADFGX\n1 - ADFGVX\n\n"))

	if is_ADFGVX:
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

	else:
		alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

	cipher = cipher.translate(
		{
			68:66,
			70:67,
			71:68,
			86:69,
			88:70
		}
		if is_ADFGVX else
		{
			68:66,
			70:67,
			71:68,
			88:69
		}
	)	# Translates the characters in the cipher so it can be treated as a polybius square that needs transposed first

	factors=[n for n in range(2, len(cipher)) if len(cipher) % n == 0]		# Gets factors of the length of the text (from the internet)

	print(f"\033cThe length of the text is: {len(cipher)}\nColumns that can be tried: {', '.join(map(str, factors))}")
	columns = []
	while True:
		tmp = input(f"Which factors should I try?(all - to try all of the factors, exit - to exit)\nFactors I will try: {', '.join(map(str, columns))}\n\n")
		if tmp == "all":
			columns.extend(factors)
			break

		elif tmp == "" or tmp == "exit":
			break

		elif tmp.isdigit():
			if 1 < int(tmp):
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

	if len(columns) == 0:
		columns.extend(factors)
	del tmp

	decrypted, best_key = HillClimb.threaded_hill_climb(
		decrypt_ADFGVX,
		[cipher for i in range(len(columns))],
		lambda x:[x[0], x[1].copy()],
		[[alphabet, [i for i in range(columns[j])]] for j in range(len(columns))],
		lambda best_fitness, time, best_key, decryption:print(f"\033[H\033[JFitness measure (higher is better): {best_fitness}\nLast updated: {time}\nPolybius square used: {best_key[0]}\nTransposition used used: {', '.join(map(str, best_key[1]))}\nText decrypted with key:\n\n{decryption}"),
		modify_key,
		end = False
	)

	if len(input(f"\033cPolybius square used: {best_key[0]}\nTransposition key used: {', '.join(map(str, best_key[1]))}\nText decrypted with key:\n\n{decrypted}\n\nText with spaces:\n\n{' '.join(split(decrypted))}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n")):
		copy(decrypted)