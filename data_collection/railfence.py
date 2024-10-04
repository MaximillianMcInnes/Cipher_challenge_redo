import csv
import os
import requests
import random
import wikipediaapi

# function to print the fence (used for debugging)
def printFence(fence):
    for rail in range(len(fence)):
        print(''.join(fence[rail]))

# function to encrypt a message with Rail Fence Cipher
def encryptRailFence(plain, rails, offset=0, debug=False):
    cipher = ''

    # apply offset by prepending the plain text with the offset number of '#'
    plain = '#' * offset + plain

    length = len(plain)
    fence = [['#'] * length for _ in range(rails)]

    # build fence
    rail = 0
    dr = 1  # direction variable to move between rails
    for x in range(length):
        fence[rail][x] = plain[x]
        if rail == rails - 1:
            dr = -1
        elif rail == 0:
            dr = 1
        rail += dr

    # print pretty fence if debug is True
    if debug:
        printFence(fence)

    # read fence to generate cipher
    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher

# Function to fetch random article title
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

# Driver code
if __name__ == "__main__":
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

                # Process parts in a while loop
                i = 0
                while i < len(parts):
                    part = parts[i]
                    print(f"Processing part {i + 1} of the article:")
                    text_length = len(part)
                    rails_limit = text_length - 1  # rails is len(string) - 1
                    offset_limit = text_length * 2 - 8  # offset is len(string) * 2 - 8

                    for rails in range(2, rails_limit):  # Rails from 2 to len(string) - 1
                        for offset in range(1, offset_limit):  # Offset from 1 to len(string) * 2 - 8
                            encrypted_text = encryptRailFence(part, rails, offset)
                            writer.writerow([rails, offset, encrypted_text])
                            print(f'Encoded with {rails} rails and {offset} offset: {encrypted_text}')

                    i += 1  # Increment part index

        print(f"Results saved to {csv_file_path}")
