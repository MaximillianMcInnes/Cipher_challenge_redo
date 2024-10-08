import random
import string

# Function to generate a randomized lookup table
def generate_random_lookup():
    alphabet = list(string.ascii_uppercase)  # List of uppercase letters
    shuffled_alphabet = alphabet[:]  # Copy the alphabet
    random.shuffle(shuffled_alphabet)  # Shuffle the copy

    # Create the lookup table with random mappings
    lookup_table = dict(zip(alphabet, shuffled_alphabet))
    return lookup_table

# Atbash cipher function that uses a randomized lookup table
def atbash(message, lookup_table):
    cipher = ''
    for letter in message:
        # Check for space
        if letter != ' ':
            # Add the corresponding letter from the lookup_table
            cipher += lookup_table[letter]
        else:
            # Add space
            cipher += ' '

    return cipher

# Driver function to run the program
def main():
    # Generate a new random lookup table
    lookup_table = generate_random_lookup()
    
    # Encrypt the given message
    message = 'GEEKS FOR GEEKS'
    print("Original message:", message)
    encrypted_message = atbash(message.upper(), lookup_table)
    print("Encrypted message:", encrypted_message)
    
    # To decrypt, reverse the lookup table
    reverse_lookup_table = {v: k for k, v in lookup_table.items()}
    decrypted_message = atbash(encrypted_message, reverse_lookup_table)
    print("Decrypted message:", decrypted_message)

# Executes the main function
if __name__ == '__main__':
    main()
