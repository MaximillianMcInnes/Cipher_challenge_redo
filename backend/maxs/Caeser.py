import re
from ngram_score import ngram_score
import os
import string
import time
import wordninja
from pathlib import Path

base_dir = Path(__file__).resolve().parent 
ngram_path = base_dir / 'quadgrams.txt'
fitness = ngram_score(ngram_path)  # load our quadgram statistics

alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"

def decrypt(ciphertext, key):
    decrypted_message = ""
    for c in ciphertext: 
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message

def break_caesar(ctext):
    # Ensure ciphertext has all spacing/punctuation removed and is uppercase
    ctext = re.sub('[^A-Z]', '', ctext.upper())
    # Try all possible keys, return the one with the highest fitness
    scores = []
    for i in range(26):
        deciphered_text = decrypt(ctext.lower(), i)
        scores.append((fitness.score(deciphered_text.upper()), i))
    return max(scores)

def main():
    start_time = time.time()

    # Use the provided string as plaintext (without brackets)
    file_path = os.path.join(os.path.dirname(__file__), 'cipher.txt')  # Update with your own file path
    with open(file_path, "r") as file:
        ctext = file.read().strip()
    
    print(f"cipher text: {ctext}")

    # Check if ciphertext length is less than 650
    if len(ctext) < 650:
        # Decrypt using the first 350 characters
        partial_ctext = ctext[:350]
        
        # Break Caesar cipher on the partial text
        max_key = break_caesar(partial_ctext)
        
        print('Best candidate from partial text with key = ' + str(max_key[1]) + ':')
        
        # Decrypt full text using the key from partial text
        deciphered_text = ' '.join(wordninja.split(decrypt(ctext.lower(), max_key[1])))
    else:
        # Break Caesar cipher on full text
        max_key = break_caesar(ctext)
        
        print('Best candidate with key = ' + str(max_key[1]) + ':')
        
        # Decrypt full text
        deciphered_text = ' '.join(wordninja.split(decrypt(ctext.lower(), max_key[1])))
    
    deciphered_text = deciphered_text.lower()

    print("Final deciphered text: ")
    print(deciphered_text)
    plain_text = base_dir / 'plaintext.txt'
    with open(plain_text, "w", encoding='utf-8') as file:
        file.write(deciphered_text)
    
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()
