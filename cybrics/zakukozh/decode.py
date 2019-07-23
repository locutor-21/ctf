from tqdm import tqdm 
from egcd import egcd
from pathlib import Path
import sys

def encode(byte, a, b):



if len(sys.argv) != 2:
    print("Usage: python3 decode.py <file>")
    exit(1)


try:
    data = Path(sys.argv[1]).open('rb').read()
except Exception as e:
    print("Error during file load: {}".format(e))
    exit(1)
else:
    print("[+] Starting job...")
    for i in tqdm(range(256))



