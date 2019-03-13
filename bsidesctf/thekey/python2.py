#!/usr/bin/python
newmap = {
        0x04: "A",
        0x05: "B",
        0x06: "C",
        0x07: "D",
        0x08: "E",
        0x09: "F",
        0x0A: "G",
        0x0B: "H",
        0x0C: "I",
        0x0D: "J",
        0x0E: "K",
        0x0F: "L",
        0x10: "M",
        0x11: "N",
        0x12: "O",
        0x13: "P",
        0x14: "Q",
        0x15: "R",
        0x16: "S",
        0x17: "T",
        0x18: "U",
        0x19: "V",
        0x1A: "W",
        0x1B: "X",
        0x1C: "Y",
        0x1D: "Z",
        0x1E: "1",
        0x1F: "2",
        0x20: "#",
        0x21: "4",
        0x22: "5",
        0x23: "6",
        0x24: "7",
        0x25: "8",
        0x26: "9",
        0x27: "0",
        0x28: "enter",
        0x29: "esc",
        0x2A: "del",
        0x2B: "tab",
        0x2C: " ",
        0x2D: "-",
        0x2E: "=",
        0x2F: "[",
        0x30: "]",
        0x33: ":",
        0x37: ".",
        0x38: "/",
        0x39: "caps",
        0x4f: "right",
        0x50: "left"
}

myKeys = open('hexoutput.txt')
i = 1
for line in myKeys:
        bytesArray = bytearray.fromhex(line.strip())
        for byte in bytesArray:
                if byte != 0:
                        keyVal = int(byte)
                        if keyVal in newmap:
                                print (newmap[keyVal], end="")
                        else:
                                print ("No map found for this value: " + str(keyVal), end="")
                i+=1

print ("")