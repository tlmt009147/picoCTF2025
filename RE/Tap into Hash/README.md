# Tap into Hash
## Description
Can you make sense of this source code file and write a function that will decode the given encrypted file content?
Find the encrypted file [here](https://challenge-files.picoctf.net/c_verbal_sleep/822410320e241b7a7f303305c193c7a7e163a2ebdf3ba4b65271f34b5cb1d55f/enc_flag).
It might be good to analyze source [file](https://challenge-files.picoctf.net/c_verbal_sleep/822410320e241b7a7f303305c193c7a7e163a2ebdf3ba4b65271f34b5cb1d55f/block_chain.py) to get the flag.

## Hints
1. Do you know what blockchains are? If so, you know that hashing is used in blockchains.
2. Download the encrypted flag file and the source file and reverse engineer the source file.

## Write-up
In short, I took the key and hashed it with sha256, then XOR with the ciphertext in block of 16 bytes.
## Flag
