#!/usr/bin/python
import sys, hashlib, random, itertools, string, re

if len(sys.argv) <= 2 ):
    print "USAGE:"
    print "%s input.txt"%sys.argv[0]
    exit(1)

_, inputFile = sys.argv

# initialize our mapping score
corpus = re.sub(r'[a-z]+', '', open("./war_and_peace.txt").read(), re.I)
score = plaintext_score_function(3, corpus)

def score_fun():
    pass


def get_maps(key):
    ## initialize the alpVhabet permutation
    key = hashlib.sha256(key).hexdigest()
    random.seed(int(key, 16))

    ## shuffle the monogram mapping
    plain1 = list(string.ascii_lowercase)
    crypt1 = plain1[:]
    random.shuffle(crypt1)

    ## shuffle the bigram mapping
    plain2 = [''.join(x) for x in itertools.product(string.ascii_lowercase, string.ascii_lowercase)]
    crypt2 = plain2[:]
    random.shuffle(crypt2)

    map1 = dict(zip(plain1, crypt1))
    map2 = dict(zip(plain2, crypt2))

    return map1, map2 


def find_maps(ciphertext, score_fun, map1=None, map2=None, choices=10):
    """Attempt to decrypt ciphertext, using score_fun to score the
    candidate plaintexts. 

    Return a tuple (score, map1, map2, flag) for the best maps found.

    Keyword arguments:
    map1/map2 -- starting guess as to the cipher (if omitted, the search
               starts at a randomly chosen cipher).
    choices -- at each step, choose the next state in the search
               randomly from this many top candidates (default: 10). 
    """
    if map1 is None and map2 is None:
          map1, map2 = get_maps("key")

    best_cipher = (map1, map2)
    best_score = score_fun(decipher(ciphertext, map1, map2))

def transform(s):
    s = s.group(0)
    res = ""
    for i in range(0, len(s), 2):
        chunk = s[i:i+2]
        if len(chunk) == 2:  ## if it's a bigram
            ciph = map2[chunk.lower()]
            if chunk[0] == chunk[0].upper():
                ciph = ciph[0].upper() + ciph[1]
            if chunk[1] == chunk[1].upper():
                ciph = ciph[0] + ciph[1].upper()
        elif len(chunk) == 1:  ## if it's last odd character
            ciph = map1[chunk.lower()]
            if chunk == chunk.upper():
                ciph = ciph.upper()
        res += ciph
    return res

## actually transform the text
text = open(sys.argv[3], "rb").read()
text = re.sub(r'[a-z]+', transform, text, 0, re.I)
open(sys.argv[4], "wb").write(text)
