
import matplotlib.pyplot as plt
import numpy as np
from clipboard import paste
def filter_text(text):
	filtered = []
	for i in text:
		if 64<ord(i.upper())<91:
			filtered.append(i)
	return "".join(filtered)
if int(input("Where do you want the text to be from?\n\n1 - My clipboard\n0 - I want to type it\n\n")):
	text = paste()
else:
	text = input("What is the text?\n\n")
text = filter_text(text.upper())
while 1:
	ngram = int(input("2 - digrams/bigrams\n3 - trigrams\n4 - quadgrams\n(You get the point)\n\n"))
	overlap = int(input("Do you want to check overlapping ngrams?\n\n1 - yes\n0 - no\n\n"))
	ngrams = int(input(f"How many most common {ngram}-grams do you want to see?\n\n"))
	split_texts = list(text[i:i+ngram] for i in range(0, len(text),(1 if overlap else ngram)) if len(text[i:i+ngram]) == ngram)	# Split the text into n-grams
	frequencies = {}
	for i in range(len(split_texts)-1, -1, -1):
		gram = split_texts.pop(-1)
		if gram in frequencies.keys():
			frequencies[gram] += 1
		else:
			frequencies[gram] = 1
	common = [[], []]
	removed_freq = frequencies.copy()
	for i in range(ngrams):
		tmp = max(removed_freq, key=removed_freq.get)
		common[0].append(tmp)
		common[1].append(removed_freq.pop(tmp))
	print(f"Most common ngrams: {', '.join(common[0])}\n")
	X_axis=np.arange(ngrams)
	try:
		plt.figure()
		plt.bar(X_axis, common[1], 0.8)
		plt.xticks(X_axis, common[0])
		plt.ylabel("Letters")
		plt.title(f"Most common {ngram}-grams")
		plt.show()
	except KeyboardInterrupt:
		plt.close("all")