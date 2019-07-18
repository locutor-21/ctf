#!/usr/bin/env python3

import random
import subprocess

with open("log.txt", "r") as f:
    logs = f.readlines()
    
    seeds = []
    for line in logs:
        x, y = line.split("{")[1][:-2].split("_")
        seed = (x,y)
        seeds.append(seed)

    # print(seeds)

    ret = subprocess.check_output("./rand2")
    print(ret.stdout)
    
