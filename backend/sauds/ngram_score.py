from math import log10

class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        ''' Load a file containing n-grams and counts, calculate log probabilities '''
        self.ngrams = {}
        with open(ngramfile) as file:
            for line in file:
                key, count = line.split(sep)
                self.ngrams[key] = int(count)
        
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        
        # Calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)
        
        self.floor = log10(0.01 / self.N)

    def score(self, text):
        ''' Compute the score of text '''
        score = 0
        for i in range(len(text) - self.L + 1):
            ngram = text[i:i + self.L]
            if ngram in self.ngrams:
                score += self.ngrams[ngram]
            else:
                score += self.floor
        return score
