# Quantum Scrambler
## Description
We invented a new cypher that uses "quantum entanglement" to encode the flag. Do you have what it takes to decode it?

Connect to the program with netcat:
$ nc verbal-sleep.picoctf.net 57273

The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/5d8fc92543d767a7faef596cb61f6a1cce41e929dd03dac6db9292b0a3d0b510/quantum_scrambler.py).

## Hints
1. Run eval on the cypher to interpret it as a python object
2. Print the outer list one object per line
3. Feed in a known plaintext through the scrambler

## Write-up
Well, this challenge was not hard to solve, I used some tricks to solve it in a few lines by identifying the structure of the nested lists that I just got the first and last element of each list and inserted those in a new list, which was also the flag.

Netcat the program and get the scrambled flag, then throw it in my script and then you get your flag unscrambled.

The script is [here](https://github.com/tlmt009147/picoCTF2025/blob/8a94cd60041f2d3ec1eae2960a5e2ba28005d4d2/RE/Quantum%20Scrambler/scramble.py)

![](https://github.com/tlmt009147/picoCTF2025/blob/8a94cd60041f2d3ec1eae2960a5e2ba28005d4d2/RE/Quantum%20Scrambler/1.png)

## Flag
picoCTF{python_is_weirdb57142ff}



