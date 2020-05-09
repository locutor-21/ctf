#!/usr/bin/env python3
from cryptography.fernet import Fernet
import requests


def get(path, data=None):
    f = open(path)
    data = f.read()
    f.close()

    return data


def decrypt(cipher, key):
    return Fernet(key).decrypt(cipher)


def break_enc(pub_key, cipher):
    # Write code here to break the cryptography
    sym_key = ""
    return sym_key


def main():
    pub_key = get("pub_key")
    cipher = get("cipher")

    sym_key = break_enc(pub_key, cipher)
    
    enc_flag = get("flag")

    print(decrypt(enc_flag.encode(), sym_key).decode())


if __name__ == "__main__":
    main()
