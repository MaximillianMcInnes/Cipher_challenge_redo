import requests

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

# Driver code
if __name__ == "__main__":
    article_title = get_random_article_title()
    if article_title:
        print(f"Random Wikipedia article title: {article_title}")

    text = input("Enter text to encrypt: \n")
    for key in range((len(text) - 1)):
        for offset in range(((len(text))*2) - 5):
            key = int(input("Enter the key (number of rails): "))
            offset = int(input("Enter the offset: "))

    encrypted_text = encryptRailFence(text, key, offset)
    print(f"Encrypted Text: {encrypted_text}")
