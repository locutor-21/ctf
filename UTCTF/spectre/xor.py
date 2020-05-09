#!/usr/bin/env python3
for key in range(141, 256):
    print("[-] " + str(key) + ":")

    with open("song.wav", "rb") as f:
        xord_bytes = b''
        data = f.read()
        for byte in data:
            xord_bytes += (bytes([byte ^ key]))
        try:
            if 'utflag' in xord_bytes.decode('utf-8'):
                print("[!] Got it!")
                print(xord_bytes.decode('utf-8'))
        except:
            pass
