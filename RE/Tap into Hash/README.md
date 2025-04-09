# Tap into Hash
## Description
Can you make sense of this source code file and write a function that will decode the given encrypted file content?
Find the encrypted file [here](https://challenge-files.picoctf.net/c_verbal_sleep/822410320e241b7a7f303305c193c7a7e163a2ebdf3ba4b65271f34b5cb1d55f/enc_flag).
It might be good to analyze source [file](https://challenge-files.picoctf.net/c_verbal_sleep/822410320e241b7a7f303305c193c7a7e163a2ebdf3ba4b65271f34b5cb1d55f/block_chain.py) to get the flag.

## Hints
1. Do you know what blockchains are? If so, you know that hashing is used in blockchains.
2. Download the encrypted flag file and the source file and reverse engineer the source file.

## Write-up
In short, I took the key and hashed it with sha256, then XOR with the ciphertext in blocks of 16 bytes.

![](https://github.com/tlmt009147/picoCTF2025/blob/fcb31d556796c0bac1baa17948374ee3c3cba1f9/RE/Tap%20into%20Hash/1.png)

Script to decode is [here](https://github.com/tlmt009147/picoCTF2025/blob/fcb31d556796c0bac1baa17948374ee3c3cba1f9/RE/Tap%20into%20Hash/block_chain_solve.py)

## Flag
picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_45cd2a52}
