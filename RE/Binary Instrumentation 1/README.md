# Binary Instrumentation 1
## Description
I have been learning to use the Windows API to do cool stuff! Can you wake up my program to get the flag?
Download the exe [here](https://challenge-files.picoctf.net/c_verbal_sleep/c71239e2890bd0008ff9c1da986438d276e7a96ba123cb3bc7b04d5a3de27fe7/bininst1.zip). 
Unzip the archive with the password picoctf

## Hints
1. Frida is an easy-to-install, lightweight binary instrumentation toolkit
2. Try using the CLI tools like frida-trace to auto-generate handlers

## Write-up
I use ida to solve this challenge. It took me quite a time to solve as the code is not available in static debugging. My approach was to narrow down the scope of searching
to find out the suspicious function or space in memory that contained the flag.
## Flag
