import os

current_dir = dir = os.path.dirname(__file__)
ngram_files = {
    4: r"C:\Users\Maximillian Mcinnes\Desktop\Cipher app\backend\back\quadgrams.txt"
}


def load_ngrams(n):
    assert n in ngram_files.keys()
    ngrams = {}
    with open(ngram_files[n], "r") as f:
        for line in f:
            key, count = line.split(" ")
            ngrams[key] = int(count)
    return ngrams


class Ngram(object):
    def __init__(self, n):
        self.n = n
        assert self.n in ngram_files.keys()

    def get(self):
        self.ngrams = {}
        with open(ngram_files[self.n], "r") as f:
            for line in f:
                key, count = line.split(" ")
                self.ngrams[key] = int(count)
        return self.ngrams