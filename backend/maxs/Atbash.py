import random, re, sys, math, functools
import os
import time
import wordninja
import language_tool_python
from pathlib import Path

base_dir = Path(__file__).resolve().parent 

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ASCII_OFFSET = ord('A')

# Create the Atbash lookup table
atbash_lookup = {ALPHABET[i]: ALPHABET[25 - i] for i in range(len(ALPHABET))}

# Atbash cipher function
def atbash_cipher(text):
    cipher_text = ''
    for char in text:
        if char.isalpha():
            cipher_text += atbash_lookup[char.upper()]
        else:
            cipher_text += char  # Non-alphabet characters remain unchanged
    return cipher_text

# Score the key based on the quadgrams (no need to modify this)
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

# Format the plaintext using word segmentation (no need to modify this)
def format_plaintext(plaintext):
    if not (" " in plaintext):
        words = []
        for section in plaintext.upper().split("AND"):
            words.append(" ".join(segment(section)))
        plaintext = " and ".join(words)
    return plaintext

# Main function to process the input text with Atbash cipher
def decrypt_ciphertext(ciphertext_input):
    print(f"Processing ciphertext of length: {len(ciphertext_input)}")

    # Decrypt using Atbash cipher
    decrypted_text = atbash_cipher(ciphertext_input)
    print("=====================================================")
    print(decrypted_text)
    print("=====================================================")

    # Return the plaintext
    return None, decrypted_text  # Return None as key (Atbash doesn't use a key)

# Example usage with text input
if __name__ == "__main__":
    start_time = time.time()
    file_path = os.path.join(os.path.dirname(__file__), 'cipher.txt')  # Update with your own file path

    # Read the file in UTF-8 encoding and remove all spaces
    with open(file_path, "r", encoding='utf-8') as file:
        ctext = file.read().replace(" ", "").strip()

    if len(ctext) > 500:
        partial_ctext = ctext[:350]
        _, text = decrypt_ciphertext(partial_ctext)
        deciphered_text = atbash_cipher(ctext)
    else:
        _, deciphered_text = decrypt_ciphertext(ctext)
    
    # Split the deciphered text using wordninja
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
        print("Written to plaintext.txt")
    
    print(f"Execution time: {end_time - start_time} seconds")
