cipher = [
    0xE1, 0xA7, 0x1E, 0xF8, 0x75, 0x23, 0x7B, 0x61,
    0xB9, 0x9D, 0xFC, 0x5A, 0x5B, 0xDF, 0x69, 0xD2,
    0xFE, 0x1B, 0xED, 0xF4, 0xED, 0x67, 0xF4
]

input = [0] * 27

v10 = 0
v11 = 0

for i in range(23):
    for j in range (8):
        if (v10 == 0): v10 = 1
        v6 = 1 << (7 - j)
        v5 = 1 << (7 - v10)
        
        if cipher[i] & v6 > 0:
            input[v11] = (input[v11] | v5) & 0xFF

        v10 += 1
        if v10 == 8:
            v10 = 0
            v11 += 1            
        
plain_text = ''.join(chr(byte) for byte in input)
print(plain_text)