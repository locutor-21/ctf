import json
from tqdm import tqdm
from egcd import egcd
from pathlib import Path
import sys

def get_next(a, power, N):
    b = a ** power % N
    return b, b % 256


if not Path('public.key').exists():
    print("Key file not found")
    exit(1)


if len(sys.argv) != 3:
    print("Usage: python3 cryptor.py <filename_in> <filename_head>")
    exit(1)


try:
    key = json.loads(Path('public.key').open().read())
    data = Path(sys.argv[1]).open('rb').read()
except Exception as e:
    print("Error during keyfile load: {}".format(e))
    exit(1)
else:
    for power in range(2, 17):
        print ("[+] Iterating over power " + str(p))
        for seed in tqdm(range(2**16)):
            # calculate offset
            for _ in range(key['O']):
                seed = get_next(seed, power, key['N'])[0]

            with Path(sys.argv[2]).open('rb') as h:
                for i in tqdm(range(len(12)):
                    seed, bt = get_next(seed, power, key['N'])
                    if i in range (4, 8):
                        pass
                    else:
                    w.write(bytes([data[i] ^ bt]))
