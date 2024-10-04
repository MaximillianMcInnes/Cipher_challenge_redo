import random, re, sys, math, functools
import os
import time
import wordninja
import language_tool_python


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ASCII_OFFSET = ord('A')
MAX_ITERATIONS = 1000

# NGrams class to load n-grams from a file
class NGrams(object):
    def __init__(self, filename):
        self.ngrams = {}

        # Load ngrams from file
        for line in open(filename):
            char, count = line.split(" ")
            self.ngrams[char] = int(count)

        self.L = len(char)
        self.N = sum(self.ngrams.values())

        for char in self.ngrams.keys():
            self.ngrams[char] = math.log10(float(self.ngrams[char]) / self.N)
        self.floor = math.log10(0.01 / self.N)

    def score_text(self, text):
        score = 0
        for i in range(len(text) - self.L + 1):
            if text[i:i+self.L] in self.ngrams:
                score += self.ngrams[text[i:i+self.L]]
            else:
                score += self.floor
        return score

# Decipher a ciphertext using the provided key
def decipher(text, key):
    inverse = [ALPHABET[key.index(i) % 26] for i in ALPHABET]
    plaintext = ''
    for char in text:
        if char.isalpha():
            plaintext += inverse[ord(char.upper()) - ASCII_OFFSET]
        else:
            plaintext += char
    return plaintext

# Score the key based on the quadgrams
quads = r"quadgrams.txt"
quadgrams = NGrams(quads)
def score_key(ciphertext, key):
    plaintext = decipher(ciphertext, key)
    return quadgrams.score_text(re.sub('[^A-Z]', '', plaintext.upper()))

# Format the plaintext using word segmentation
def format_plaintext(plaintext):
    if not (" " in plaintext):
        words = []
        for section in plaintext.upper().split("AND"):
            words.append(" ".join(segment(section)))
        plaintext = " and ".join(words)
    return plaintext

# OneGramDist class for single word probabilities
class OneGramDist(dict):
   def __init__(self, filename):
      self.gramCount = 0

      for line in open(filename):
         (word, count) = line[:-1].split('\t')
         self[word] = int(count)
         self.gramCount += self[word]

   def __call__(self, key):
      if key in self:
         return float(self[key]) / self.gramCount
      else:
         return 1.0 / (self.gramCount * 10**(len(key)-2))
ones = r"one-grams.txt"
singleWordProb = OneGramDist(ones)

def wordSeqFitness(words):
    return sum(math.log10(singleWordProb(w)) for w in words)

def memoize(f):
    cache = {}
    def memoizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    memoizedFunction.cache = cache
    return memoizedFunction

@memoize
def segment(word):
    if not word:
        return []
    word = word.lower()
    allSegmentations = [[first] + segment(rest) for (first, rest) in splitPairs(word)]
    return max(allSegmentations, key=wordSeqFitness)

def splitPairs(word, maxLen=20):
    return [(word[:i+1], word[i+1:]) for i in range(min(len(word), maxLen))]

@memoize
def segmentWithProb(word):
    segmented = segment(word)
    return (wordSeqFitness(segmented), segmented)

# Main function to process the input text
def decrypt_ciphertext(ciphertext_input):
    print(len(ciphertext_input))
    best_key = None
    best_score = -99e99
    sum = 0
    last_best_plaintext = ""
    unchanged_iterations = 0  # To track unchanged iterations
    best_plaintext = ""
    
    while True:
        sum += 1
        key = list(ALPHABET)
        random.shuffle(key)
        score = score_key(ciphertext_input, key)

        count = 0
        while count < MAX_ITERATIONS:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            new_key = key[:]
            new_key[a], new_key[b] = new_key[b], new_key[a]

            new_score = score_key(ciphertext_input, new_key)

            if new_score > score:
                score, key = new_score, new_key[:]
                count = 0
            count += 1
        
        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = format_plaintext(decipher(ciphertext_input, best_key))
            print("=====================================================")
            print(best_plaintext)
            print("=====================================================")
            
        # Check if plaintext has changed
        if best_plaintext == last_best_plaintext:
            unchanged_iterations += 1
        else:
            unchanged_iterations = 0  # Reset if plaintext has changed
            last_best_plaintext = best_plaintext
        print(unchanged_iterations)
        
        # Stop if the output hasn't changed for 4 iterations
        if unchanged_iterations >= 3:
            print("No improvement in 3 iterations. Stopping decryption.")
            break 
    
    return best_key, best_plaintext  # Return the latest key and deciphered text

# Example usage with text input
if __name__ == "__main__":
    start_time = time.time()
    file_path = os.path.join(os.path.dirname(__file__), 'cipher.txt')  # Update with your own file path

    # Read the file in UTF-8 encoding and remove all spaces
    with open(file_path, "r", encoding='utf-8') as file:
        ctext = file.read().replace(" ", "").strip()

    if len(ctext) > 500:
        partial_ctext = ctext[:350]
        key, text = decrypt_ciphertext(partial_ctext)
        deciphered_text = decipher(ctext, key)
    else:
        key, deciphered_text = decrypt_ciphertext(ctext)
    deciphered_text_list = wordninja.split(deciphered_text)
    deciphered_text = " ".join(deciphered_text_list)

    # Correct grammar using language_tool_python
    corrected_text = deciphered_text.lower()
    
    tool = language_tool_python.LanguageTool('en-US')
    corrected_text = tool.correct(corrected_text)
    

    print(f"Decoded text: {corrected_text}")
    end_time = time.time()
    plain_text = r"plaintext.txt"
    with open(plain_text, "w", encoding='utf-8') as file:
        file.write(deciphered_text)
        print("written in")
    
    print(f"Execution time: {end_time - start_time} seconds")