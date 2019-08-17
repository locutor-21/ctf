#!/usr/bin/environ python3

import itertools 

def score(bytes):
    pass


enc_bytes = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

candidates = []

for key in range(256):
    xord_bytes = b''
    for byte in enc_bytes:
        xord_bytes += (bytes([byte ^ key]))
    candidates.append(xord_bytes)

max_score = (b'', -1)
for candidate in candidates:
    print(candidate.decode())
    #score = score(candidate)
    #if score > max_score.1:
    #    max_score = (candidate, score)

#print(max_score.1)
#dec = max_score.1.decode()

assert dec == "Cooking MC's like a pound of bacon"
