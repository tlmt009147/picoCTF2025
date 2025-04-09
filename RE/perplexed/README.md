# perplexed
## Description
Download the binary [here](https://challenge-files.picoctf.net/c_verbal_sleep/2326718ce11c5c89056a46fce49a5e46ab80e02d551d87744306ae43a4767e06/perplexed).

## Hints
No 

## Write-up
I used ida to reverse the program. It seemed to be some kind of algorithm that compared each byte in cipher with each byte in user input except for the Most significant byte in user input. So we just need to copy each byte in cipher to each byte in user input except for the leftmost one to get our flag back.

![](https://github.com/tlmt009147/picoCTF2025/blob/3d80da6a6b7ef7a78fd6311182d43481f9aff9f0/RE/perplexed/1.png)

The below code is the code I recode in Python for the program. (Just for easier understanding)

```python
import sys

cipher = [
    0xE1, 0xA7, 0x1E, 0xF8, 0x75, 0x23, 0x7B, 0x61,
    0xB9, 0x9D, 0xFC, 0x5A, 0x5B, 0xDF, 0x69, 0xD2,
    0xFE, 0x1B, 0xED, 0xF4, 0xED, 0x67, 0xF4
]

v11 = 0
v10 = 0

user_input = input("Enter 27-character string: ")
if len(user_input) != 27:
    sys.exit(1)

for i in range(23):
    for j in range(8):
        if v10 == 0:
            v10 = 1

        v6 = 1 << (7 - j)
        v5 = 1 << (7 - v10)

        tmp1 = (cipher[i] & v6) > 0
        tmp2 = (user_input[v11] & v5) > 0

        if tmp1 != tmp2:
            sys.exit(1)

        v10 += 1
        if v10 == 8:
            v10 = 0
            v11 += 1

        if v11 == len(user_input):
            sys.exit(0)

sys.exit(0)
```
Script for solving is [here](https://github.com/tlmt009147/picoCTF2025/blob/3d80da6a6b7ef7a78fd6311182d43481f9aff9f0/RE/perplexed/perplex_solve%2C.py)

## Flag
picoCTF{0n3_bi7_4t_a_7im3}
