#!/usr/bin/python3

with open("passwd.png.bkp", 'rb') as f:
    data = bytearray(f.read())
    output = bytearray(b'')

    with open("no_spaces.bin", 'wb') as out:
        for byte in data:
            if byte == 0x2A:
                byte = 0x00
            else:
                output.append(byte)
        
        out.write(output)
