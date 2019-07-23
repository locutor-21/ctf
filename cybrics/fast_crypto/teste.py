import json
from tqdm import tqdm
from egcd import egcd 
from pathlib import Path
import sys

try:
    key = json.loads(Path('public.key').open().read())
except Exception as e:
    print("Error during keyfile load: {}".format(e))
    exit(1)

for p in range(1, 17):
    if egcd(p, key['N'])[0] == 1:
        print(p)



