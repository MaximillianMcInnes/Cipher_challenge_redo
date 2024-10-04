from os.path import join, dirname, realpath, basename
from array import array

def init(tmp_ngram = None, spaces = False):
	from pickle import load
	global ngram, save, low
	ngram = 4 if tmp_ngram == None else tmp_ngram
#	ngram = input("2 - digrams/bigrams\n3 - trigrams\n4 - quadgrams\n(You get the point)\n\n") if tmp_ngram == None else tmp_ngram
#	ngram = 4 if ngram == "" else int(ngram)
	filelocation = join(dirname(realpath(__file__)), f'{ngram}-grams.pkl')

	with open(filelocation, 'rb') as file:
		save, low = load(file)
		file.close()

	if spaces:
		global save_spaces, low_spaces
		filelocation = join(dirname(realpath(__file__)), f"{ngram}-grams-spaces.pkl")
		with open(filelocation, 'rb') as file:
			save_spaces, low_spaces = load(file)
			file.close()

def init_words():
	from pickle import load
	global words_list
	filelocation=join(dirname(realpath(__file__)), 'words.pkl')
	with open(filelocation, 'rb') as file:
		words_list = load(file)
		file.close()

def filter_text(text: str, spaces = False, nums = False):
	filtered = array("u")
	for i in text:
		if i.isalpha() or (spaces and i==" ") or (nums and i.isnumeric()):
#		if 64<ord(i.upper())<91 or (spaces and i==" "):
			filtered.append(i)
	return "".join(filtered)

def cal_avg_fitness(text, do_filter = True, spaces = False, nums = False):

	if do_filter:
		text = filter_text(text, spaces, nums)

	return cal_fitness(text, do_filter = False, spaces = spaces)/(len(text)-(ngram-1))

def cal_fitness(text: str, do_filter = True, spaces = False, nums = False):
	new_text = filter_text(text, spaces, nums).upper() if do_filter else text
	fitness = 0
	_save, _low = (save_spaces, low_spaces) if spaces else (save, low)
	for i in range(len(new_text)-(ngram-1)):
		if new_text[i:i+ngram] in _save.keys():
			fitness += _save[new_text[i:i+ngram]]
		else:
			fitness += _low
	return fitness

def add_spaces(text):
	global words_list
	c = 0
	while c < len(text):
		for i in range(len(text)+1, c, -1):
			if text[c:i] in words_list:
				text = list(text)
				text.insert(i, " ")
				text = "".join(text)
				break
		c = i
	return text

if __name__=="__main__":
	from tkinter import Tk, filedialog
	root = Tk()
	root.withdraw()
	root.attributes('-topmost', True)
	root.overrideredirect(True)
	mode = int(input("What do you want to do?\n\n0 - Generate ngram files\n1 - Calculate fitness of a text\n2 - Generate word file\n3 - Attempt to add spaces to the text\n\n"))
	if mode == 0:
		from pickle import dump
		from math import log10

		spaces = input("Do you want the spaces to be taken into account?\n\n1 - yes\n0 - no\n\n")=="1"
		if int(input("Do you want to specify a specific text file to extract text from?\n\n1 - yes\n0 - no\n\n")):
			print("A seperate window has been opened for you to select the text file from.")
			filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=(("Text Files","*.txt"),("All Files", "*.*")))
		else:
			filename = realpath(__file__).replace("pypy\\"+basename(__file__),"texts.txt").replace("\\","/")
#			filename = filelocation=join(dirname(realpath(__file__)), 'texts.txt')

		file = open(filename, "r", encoding="utf8")
		text = filter_text(file.read(), spaces).upper()
		file.close()

		ngrams = input("Enter all the ngrams files you want to generate, seperated by commas\n\n2 - digrams/bigrams\n3 - trigrams\n4 - quadgrams\n(You get the point)\n\n").replace(" ", "").split(",")
		for ngram in (int(i) for i in ngrams):
			filelocation = join(dirname(realpath(__file__)), f"{ngram}-grams{'-spaces'if spaces else ''}.pkl")
			grams: dict[str, float]
			grams = {}
			split_texts = [text[i:i+ngram] for i in range(len(text)) if len(text[i:i+ngram]) == ngram]

			for i in range(len(split_texts)-1, -1, -1):
				gram = split_texts.pop(-1)
				if gram in grams.keys():
					grams[gram] += 1
				else:
					grams[gram] = 1

			for i in grams.keys():
				grams[i] = log10(grams[i]/(len(text)-(ngram-1)))

			low = log10(0.01/(len(text)-(ngram-1)))

			print(f"Most occuring {ngram}-gram: '{max(grams, key=grams.get)}'")
			with open(filelocation, 'wb') as file:			# this and the next line are from https://www.geeksforgeeks.org/how-to-use-pickle-to-save-and-load-variables-in-python/#:~:text=Pickle%20is%20a%20python%20module,which%20JSON%20fails%20to%20serialize and reddit.
				dump((grams, low), file)
				file.close()

	elif mode == 1:
		from clipboard import paste
		ngram = int(input("Enter the ngram you wish to use.\n\n2 - digrams/bigrams\n3 - trigrams\n4 - quadgrams\n(You get the point)\n\n"))
		init(ngram, spaces = True)
		while 1:
			if int(input("Where do you want the text to be from?\n\n0 - I want to type it\n1 - Paste from clipboard\n\n")):
				text = paste()
			else:
				text = input("Please enter the text:\n\n")
			print(f"Fitness: {cal_fitness(text)}\nControlled Fitness: {cal_avg_fitness(text)}\nFitness with spaces: {cal_fitness(text, spaces = True)}\nControlled Fitness with spaces: {cal_avg_fitness(text, spaces = True)}")

	elif mode == 2:
		from pickle import dump
		if int(input("Do you want to specify a specific text file to extract text from?\n\n1 - yes\n0 - no\n\n")):
			print("A seperate window has been opened for you to select the text file from.")
			filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=(("Text Files","*.txt"),("All Files", "*.*")))
		else:
			filename = filelocation=join(dirname(realpath(__file__)), 'texts.txt')

		file = open(filename, "r", encoding="utf8")
		all_words = filter_text(file.read(), True).upper().split(" ")
		file.close()

		words_list = []
		for i in range(len(all_words)):
			word = all_words.pop(-1)
			if word not in words_list:
				words_list.append(word)

		filelocation=join(dirname(realpath(__file__)), "words.pkl")
		with open(filelocation, 'wb') as file:
			dump(words_list, file)

	else:
		from clipboard import paste
		init_words()
		while 1:
			if int(input("Where do you want the text to be from?\n\n0 - I want to type it\n1 - Paste from clipboard\n\n")):
				text = paste()
			else:
				text = input("Please enter the text:\n\n")
			print(f"Text with spaces:\n\n{add_spaces(text)}")