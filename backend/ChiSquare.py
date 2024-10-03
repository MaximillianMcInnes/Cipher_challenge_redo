percentages = (8.34, 1.54, 2.73, 4.14, 12.6, 2.03, 1.92, 6.11, 6.71, 0.23, 0.87, 4.24, 2.53, 6.80, 7.70, 1.66, 0.09, 5.68, 6.11, 9.37, 2.85, 1.06, 2.34, 0.2, 2.04, 0.06)
alphabet = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def filter_text(text):
	filtered = []
	for i in text:
		if 64<ord(i.upper())<91:
			filtered.append(i)
	return "".join(filtered)
def cal_chi_square(text: str):
	text = filter_text(text.upper())
	value = 0
	for i in range(26):
		expected = (percentages[i]*len(text))/100
		value += ((text.count(alphabet[i])-expected)**2)/expected
#		print(text.count(alphabet[i]), percentages[i]*len(text))
	return value
if __name__ == "__main__":
	while 1:
		text = input('What is the text?\n\n')
		print(f"The Chi sqaure value: {cal_chi_square(text)}\n\n")