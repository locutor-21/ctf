from pathlib import Path
from tqdm import tqdm 

try: 
    f = Path("./rockyou.txt").open("r", errors = "ignore")
except Exception as e:
    print("Erro tentando abrir a wordlist: {}".format(e))
    exit(1)

else: 
    with Path("custom_rockyou.txt").open("w") as w:
        for line in tqdm(f.readlines()):
            w.write("cybrics{"+line.strip()+"}\n")

            

