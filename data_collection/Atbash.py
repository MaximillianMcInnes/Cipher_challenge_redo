import requests
import wikipediaapi
import random
import string
import os
import csv

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
        if letter.isalpha():  # Check if it's a letter
            cipher += lookup_table.get(letter.upper(), letter)
        else:
            cipher += letter  # Non-alphabet characters remain unchanged
    return cipher

# Function to get a random Wikipedia article title
def get_random_article_title():
    try:
        response = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&format=json")
        response.raise_for_status()
        data = response.json()
        title = data['query']['random'][0]['title']
        return title
    except requests.RequestException:
        print("Error fetching random article title.")
        return None

# Subroutine to fetch Wikipedia article text
def get_wikipedia_article_text(article_title):
    user_agent = "MyWikipediaScript/1.0 (https://example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )
    try:
        page = wiki_wiki.page(article_title)
        if not page.exists():
            print(f"Article '{article_title}' does not exist.")
            return None
        return page.text
    except Exception as e:
        print(f"Error fetching article '{article_title}': {e}")
        return None

# Function to split text into chunks between 500 and 2000 characters
def split_text_in_chunks(text, min_size=500, max_size=2000):
    chunks = []
    while len(text) > 0:
        chunk_size = random.randint(min_size, max_size)  # Random size between 500 and 2000 chars
        chunk = text[:chunk_size]
        chunks.append(chunk)
        text = text[chunk_size:]  # Reduce text
    return chunks

# Main loop to fetch article, encode it using the random Atbash cipher, and write to CSV
while True:
    csv_file_path = os.path.expanduser('~/Downloads/railfence.csv')
    article_title = get_random_article_title()
    if article_title:
        print(f"Random Wikipedia article title: {article_title}")

    article_text = get_wikipedia_article_text(article_title)
    if article_text:
        parts = split_text_in_chunks(article_text)

        # Writing results to CSV file
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Rails', 'Offset', 'Encoded Text'])

            # Generate a new random lookup table for each run
            lookup_table = generate_random_lookup()

            for part in parts:
                # Encrypt each chunk of the article using the Atbash cipher
                encoded_text = atbash(part, lookup_table)

                # Example fixed values for Rails and Offset (you may replace with actual logic)
                rails = 3
                offset = 1

                # Write the encoded text to the CSV file
                writer.writerow([rails, offset, encoded_text])

        print(f"Article text encrypted and saved to {csv_file_path}")
