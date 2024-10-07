import numpy
import re 
import os
import string 
import time
import wordninja
from ngram_score import ngram_score
from pathlib import Path

base_dir = Path(__file__).resolve().parent 
ngram_path = base_dir / 'quadgrams.txt'
fitness = ngram_score(ngram_path)  # load our quadgram statistics

# Extended Euclidean Algorithm for finding modular inverse
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# Affine cipher decryption function 
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    a_inv = modinv(key[0], 26)
    if a_inv is None:
        return None  # Decryption is not possible without modular inverse
    return ''.join([chr(((a_inv * ((ord(c) - ord('A')) - key[1])) % 26) + ord('A')) 
                    for c in cipher.upper() if c in string.ascii_uppercase])

# Function to break Affine cipher
def break_affine(ctext):
    A = [a for a in range(1, 26) if numpy.gcd(a, 26) == 1]
    B = range(0, 26)  # Possible values for 'b'
    scores = []
    
    for a in A:
        for b in B:
            key = [a, b]
            decrypted_text = affine_decrypt(ctext, key)
            if decrypted_text:
                score = fitness.score(decrypted_text)
                scores.append((score, a, b))
    
    # Return the best key (a, b) with the highest fitness score
    return max(scores)

def main():
    start_time = time.time()
    
    file_path = os.path.join(os.path.dirname(__file__), 'cipher.txt')  # Update with your own file path
    with open(file_path, "r") as file:
        ctext = file.read().strip()

    print(f"Cipher text: {ctext}")
    
    if len(ctext) < 650:
        # Decrypt using the first 350 characters
        partial_ctext = ctext[:350]
        best_score, best_a, best_b = break_affine(partial_ctext)
        
        print(f'Best candidate from partial text with key (a={best_a}, b={best_b}):')
        
        # Decrypt full text using the best key
        deciphered_text = affine_decrypt(ctext, [best_a, best_b])
        if deciphered_text:
            deciphered_text = ' '.join(wordninja.split(deciphered_text.lower()))
            print("Final deciphered text: ")
            print(deciphered_text)
    else:
        # Decrypt the entire ciphertext
        best_score, best_a, best_b = break_affine(ctext)
        
        print(f'Best candidate with key (a={best_a}, b={best_b}):')
        
        deciphered_text = affine_decrypt(ctext, [best_a, best_b])
        if deciphered_text:
            deciphered_text = ' '.join(wordninja.split(deciphered_text.lower()))
            print("Final deciphered text: ")
            print(deciphered_text)
    
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    plain_text = base_dir / 'plaintext.txt'
    with open(plain_text, "w") as file:
        file.write(deciphered_text)

if __name__ == '__main__':
    main()
