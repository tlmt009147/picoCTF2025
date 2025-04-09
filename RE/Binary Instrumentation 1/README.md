# Binary Instrumentation 1
## Description
I have been learning to use the Windows API to do cool stuff! Can you wake up my program to get the flag?
Download the exe [here](https://challenge-files.picoctf.net/c_verbal_sleep/c71239e2890bd0008ff9c1da986438d276e7a96ba123cb3bc7b04d5a3de27fe7/bininst1.zip). 
Unzip the archive with the password picoctf

## Hints
1. Frida is an easy-to-install, lightweight binary instrumentation toolkit
2. Try using the CLI tools like frida-trace to auto-generate handlers

## Write-up
I used ida to solve this challenge. It took me quite a time to solve as the code is not available in static debugging. My approach was to narrow down the scope of searching to find the suspicious function or space in memory that contained the flag. Well I tried to search for some strings shown when I ran the program with CLI but I was not able to find any of them, so I predicted that the strings or another part of the program was loaded only when the program was running.

First, I ran debugging for the first time preliminarily and noticed that the program held after the below function was called, so I put a breakpoint at this line.

![](https://github.com/tlmt009147/picoCTF2025/blob/de6968089d0caf9d3298b8204537fff0fa211895/RE/Binary%20Instrumentation%201/1.png)

So when I stepped into this function, a bunch of things appeared and I continued to debug preliminarily again to narrow down the scope of searching until I noticed this part when the program held. A smaller program was loaded into the rbx register and after this part, the program held again so I put a breakpoint here and stepped into it.

![](https://github.com/tlmt009147/picoCTF2025/blob/de6968089d0caf9d3298b8204537fff0fa211895/RE/Binary%20Instrumentation%201/2.png)

After this part, I just barely wandered around until I saw this. Some variables stored the strings when the program ran.

![](https://github.com/tlmt009147/picoCTF2025/blob/de6968089d0caf9d3298b8204537fff0fa211895/RE/Binary%20Instrumentation%201/5.png)

I believed that the flag must be somewhere near here, so I clicked one of the variables to check the memory stack and I saw the flag stored in a hidden variable in the form of base64 codes.

![](https://github.com/tlmt009147/picoCTF2025/blob/de6968089d0caf9d3298b8204537fff0fa211895/RE/Binary%20Instrumentation%201/3.png)

I brought those base64 codes to the base64 decoder and received the flag.

![](https://github.com/tlmt009147/picoCTF2025/blob/de6968089d0caf9d3298b8204537fff0fa211895/RE/Binary%20Instrumentation%201/4.png)

## Flag
picoCTF{w4ke_m3_up_w1th_fr1da_f27acc38}
