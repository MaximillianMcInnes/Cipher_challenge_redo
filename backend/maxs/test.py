from collections import OrderedDict
from math import log10
from transforms import Masker
from ioc2 import IocScorer
from en import load_ngrams
from ngram import NgramScorer
from caesars import CaesarBreak

class NgramScorer(object):
    def __init__(self, ngrams):
        self.ngrams = ngrams
        self._identify_ngram_length()
        self._calculate_log_probs()

    def _identify_ngram_length(self):
        lengths = {len(key) for key, value in self.ngrams.items()}
        assert len(lengths) == 1, "All ngrams must have the same length!"
        self.n = lengths.pop()

    def _calculate_log_probs(self, alpha=0.01):
        total = sum(value for key, value in self.ngrams.items())
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / total)
        self.alpha = log10(alpha / total)

    def score(self, text, split_by=None, ignore=''):
        if len(ignore) > 0:
            text = self._remove_characters(text, ignore)
        if split_by is not None:
            return sum(self._score(part) for part in text.split(split_by))
        else:
            return self._score(text)

    def _remove_characters(self, text, characters):
        for i in range(0, len(characters)):
            text = text.replace(characters[i:i+1], '')
        return text

    def _score(self, text):
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text) - self.n+1):
            current_token = text[i:i+self.n]
            if current_token in self.ngrams:
                score += ngrams(current_token)
            else:
                score += self.alpha
        return score

class VigenereBreak(object):
    def __init__(self, key_length, scorer=None):
        self.key_length = key_length
        self.caesar_breaker = CaesarBreak(scorer)

    def analyse(self, text):
        guesses = self.guess(text)
        print("\nAnalysing for Vigenere (key length = {}): {}\n..."
              .format(self.key_length, text))
        for guess in guesses:
            decryption, score, key = guess
            print("score: {} - key: {} - plaintext: {}"
                  .format(score, key, decryption))

    def guess(self, text):
        ciphertext_chunks = self.chunk(text)
        plaintext_chunks, keys = self.break_caesars(ciphertext_chunks)
        plaintext = self.zip(plaintext_chunks)
        return [(plaintext, None, "".join(keys))]

    def chunk(self, text):
        chunks = {key: [] for key in range(self.key_length)}
        for i in range(len(text)):
            chunks[i % self.key_length].append(text[i])
        return ["".join(chunk) for _, chunk in chunks.items()]

    def break_caesars(self, chunks):
        plaintexts, keys = [], []
        for chunk in chunks:
            plaintext, score, key = self.caesar_breaker.guess(chunk, 1)[0]
            plaintexts.append(plaintext)
            keys.append(key)
        return plaintexts, keys

    def zip(self, chunks):
        result = []
        max_length = max([len(chunk) for chunk in chunks])
        for i in range(max_length):
            for chunk in chunks:
                if i < len(chunk):
                    result.append(chunk[i])
        return "".join(result)

class KeylengthDetector(object):
    def __init__(self, scorer, min_keylength=1, max_keylength=20, expected_score_plaintext=0.06, verbose=True):
        self.scorer = scorer
        self.min_n = min_keylength
        self.max_n = max_keylength
        self.expected_score_plaintext = expected_score_plaintext
        self.expected_score_random = 0.035
        assert self.expected_score_plaintext > self.expected_score_random, \
            "The expected score for plaintext must be larger than for random strings!"
        self.threshold = (self.expected_score_plaintext + self.expected_score_random) / 2
        self.verbose = verbose

    def detect(self, text):
        scores = {i: self.score(text, i) for i in range(self.min_n, self.max_n+1)}
        scores = OrderedDict(sorted(scores.items(), reverse=True, key=lambda t: t[1]))
        if self.verbose:
            self.validate_heuristically(scores)
        return scores

    def validate_heuristically(self, scores):
        print("Validating scores heuristically...")
        max_score, min_score = max(scores.values()), min(scores.values())
        if max_score < self.threshold:
            print("WARNING: Highest score too low... probably no key length will work!")
        if min_score > self.threshold:
            print("WARNING: Lowest score too high... is the text already plaintext???")
        high_scores = {k: v for k, v in scores.items() if abs(v - max_score) < abs(v - min_score)}
        result = {k: v for k, v in high_scores.items() if k % 2 != 0 or (k / 2 not in high_scores.keys())}
        print("Candidate key length values are:")
        for key, score in result.items():
            print("{}: {}".format(key, score))

    def score(self, text, n):
        chunks = self.chunk(text, n)
        return sum([self.scorer.score(chunk) for chunk in chunks]) / n

    def chunk(self, text, n):
        chunks = {key: [] for key in range(n)}
        for i in range(len(text)):
            chunks[i % n].append(text[i])
        return ["".join(chunk) for _, chunk in chunks.items()]

def break_vigenere_example(plaintext, masker):
    print("#########################################")
    print("######## Vigenere cipher example ########")
    print("#########################################")

    key = "somekey"
    ciphertext = Vigenere(key).encipher(plaintext)

    print("\nCiphertext:\n---")
    print(masker.extend(ciphertext))
    print("---\n")

    print("\nCracking...\n")

    print("Inferring key length...")
    s = IocScorer(alphabet_size=26)
    KeylengthDetector(s).detect(ciphertext)

    print("Cracking with key length 7...")

    scorer = NgramScorer(load_ngrams(4))
    breaker = VigenereBreak(7, scorer)
    decryption, score, key = breaker.guess(ciphertext)[0]
    print("Vigenere decryption (key={}, score={}):\n---\n{}---\n"
          .format(key, score, masker.extend(decryption)))

if __name__ == "__main__":
    string = input("Enter your cipher text \n : ")
    text1, masker1 = Masker.from_text(string)

    # Key length detection
    s = IocScorer(alphabet_size=26)
    print("Detecting for text 1 - true key length is 7")
    KeylengthDetector(s).detect(text1)

    # Vigenere breaking
    print("Breaking cipher of text1: keylength is 7")
    scorer = NgramScorer(load_ngrams(4))
    breaker = VigenereBreak(7, scorer)
    breaker.analyse(text1)