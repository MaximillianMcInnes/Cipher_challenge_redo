import math
import re
from itertools import product
from nostril import nonsense
from clipboard import copy
from wordninja import split
from pathlib import Path

base_dir = Path(__file__).resolve().parent 

# Load NGrams and OneGramDist classes
class NGrams:
    def __init__(self, filename):
        self.ngrams = {}
        # Load ngrams from file
        with open(filename) as file:
            for line in file:
                char, count = line.split()
                self.ngrams[char] = int(count)
        self.L = len(char)
        self.N = sum(self.ngrams.values())

        # Convert counts to log probabilities
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

class OneGramDist(dict):
    def __init__(self, filename):
        self.gramCount = 0
        with open(filename) as file:
            for line in file:
                word, count = line.split('\t')
                self[word] = int(count)
                self.gramCount += self[word]

    def __call__(self, key):
        if key in self:
            return float(self[key]) / self.gramCount
        else:
            return 1.0 / (self.gramCount * 10**(len(key)-2))

# Function to decrypt using the Rail Fence cipher
def decrypt_railfence(ciphertext, rows, starting_offset, direction):
    if rows <= 1:
        return ciphertext

    # Initialize table to store zig-zag pattern
    table = [[" " for _ in range(len(ciphertext))] for _ in range(rows)]
    flag = direction
    y = starting_offset % rows

    # Fill zig-zag pattern with placeholders
    for x in range(len(table[0])):
        table[y][x] = "0"
        if flag == 0:
            if y == len(table) - 1:
                flag = 1
                y -= 1
            else:
                y += 1
        else:
            if y == 0:
                flag = 0
                y += 1
            else:
                y -= 1

    # Replace placeholders with actual cipher letters
    letter = 0
    for y in range(rows):
        for x in range(len(table[y])):
            if table[y][x] == "0":
                table[y][x] = ciphertext[letter]
                letter += 1

    # Read the text from the zig-zag pattern
    flag = direction
    y = starting_offset % rows
    text = []
    for x in range(len(table[0])):
        text.append(table[y][x])
        if flag == 0:
            if y == len(table) - 1:
                flag = 1
                y -= 1
            else:
                y += 1
        else:
            if y == 0:
                flag = 0
                y += 1
            else:
                y -= 1

    return "".join(text)

# Function to decrypt the rail fence cipher from input text using n-gram scoring
def decrypt_railfence_with_ngram(input_text, ngram_file, onegram_file):
    cipher = re.sub(r'[^A-Z]', '', input_text.upper())

    # Get factors of the length of the text
    factors = [n for n in range(2, len(cipher)+1) if len(cipher) % n == 0 or (len(cipher)-1) % n == 0]
    print(f"The length of the text is: {len(cipher)}\nColumns that can be tried: {', '.join(str(i) for i in factors)}")

    # Load n-grams and one-gram data
    quadgrams = NGrams(ngram_file)
    singleWordProb = OneGramDist(onegram_file)

    def wordSeqFitness(words):
        return sum(math.log10(singleWordProb(w)) for w in words)

    factors_to_try = factors  # We'll try all factors automatically

    # Initialize best decryption variables
    best_key = (0, 0, 0)  # (rows, offset, direction)
    best_decryption = cipher
    best_fitness = float('-inf')

    # Try decrypting with all the factors and score with quadgrams
    try:
        for rows, direction in product(factors_to_try, (0, 1)):
            for offset in range(direction, rows + direction - 1):
                decryption = decrypt_railfence(cipher, rows, offset, direction)
                fitness = quadgrams.score_text(re.sub('[^A-Z]', '', decryption.upper()))
                if fitness > best_fitness:
                    best_fitness = fitness
                    best_decryption = decryption
                    best_key = (rows, offset, direction)
                    print(f"Rows: {best_key[0]}, Offset: {best_key[1]}, Direction: {'up' if best_key[2] else 'down'}")
                    print(f"Decrypted Text: {best_decryption}")
    except KeyboardInterrupt:
        pass

    # Final output after decryption
    if len(input(f"Rows: {best_key[0]}, Offset: {best_key[1]}, Direction: {'up' if best_key[2] else 'down'}\n\nBest Decrypted Text:\n{best_decryption}\n\nDo you want this to be copied to your clipboard? Press any key to copy.\n")) > 0:
        copy(best_decryption)

# Take input from user
def main():
    user_input_text = input("Please enter the ciphertext you want to decrypt: ")

    ngram_file = base_dir / 'quadgrams.txt'  # Path to quadgrams file
    onegram_file = base_dir / "one-grams.txt"  # Path to one-grams file
    decrypt_railfence_with_ngram(user_input_text, ngram_file, onegram_file)

if __name__ == "__main__":
    main()