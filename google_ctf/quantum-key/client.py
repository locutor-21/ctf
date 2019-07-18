#!/bin/env python

import requests
import random 
import json 

ENCRYPTION_KEY_SIZE = 256

def generate_basis():
    list = ['+','x']
    return [random.choice(list) for _ in range(ENCRYPTION_KEY_SIZE * 2)]

def generate_bits():
    list = [0,1]
    return [random.choice(list) for _ in range(ENCRYPTION_KEY_SIZE * 2)]

def generate_qubits(data, basis):
    assert len(data) == len(basis), "Length must be equal!"

    qubits = list()
    
    states = [  { "real": 0.0, "imag": 1.0 },
                { "real": 1.0, "imag": 0.0 },
                { "real": -0.707, "imag": 0.707 },
                { "real": 0.707, "imag": 0.707 }]

    for i in range(ENCRYPTION_KEY_SIZE * 2):
        if basis[i] == '+':
            if data[i]:
                qubits.append(states[0])
            else:
                qubits.append(states[1])
        else:
            if data[i]:
                qubits.append(states[2])
            else:
                qubits.append(states[3])

    return qubits 

    # return [random.choice(states) for _ in range(ENCRYPTION_KEY_SIZE * 2)]


def compare_bases_and_generate_key(basis, sat_basis, bits):
    if not (len(basis) == len(sat_basis) == len(bits)):
        print ("deu merda")
        return "basis(%d), sat_basis(%d) and bits(%d) must have the same length." % (len(basis), len(sat_basis), len(bits))
    key = ''
    for bit, sat_base, base in zip(bits, sat_basis, basis):
        if sat_base == base:
            key += str(bit)
    return key 


def main():
    addr = 'https://cryptoqkd.web.ctfcompetition.com'
    path = '/qkd/qubits'
    url = addr + path 

    s = requests.Session()
    while True:
        basis   = generate_basis()
        bits    = generate_bits()
        qubits  = generate_qubits(bits, basis)

        data = {"basis": basis, "qubits": qubits}
        
        r = s.post(url, json = data)
        
        try:
            answer = json.loads(r.text)
            sat_basis = answer['basis']
            sat_key = answer['announcement']
            
            key = compare_bases_and_generate_key(basis, sat_basis, bits)
            print (hex(int('1000',2)))
            key = str(hex(int(key, 2)))[2:]
            key = key[:32]

             
            if key != sat_key:
                print ("Wrong key: sat/local")
                print ( sat_key ) 
                print ( key ) 
            else:
                print  ( "Success!" )
                print (key)
                break
        except:
            print (r.text)

    s.close()

if __name__ == "__main__":
    main()
