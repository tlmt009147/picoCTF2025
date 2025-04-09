# Binary Instrumentation 2
## Description
I've been learning more Windows API functions to do my bidding. Hmm... I swear this program was supposed to create a file and write the flag directly to the file. Can you try and intercept the file writing function to see what went wrong?
Download the exe [here](https://challenge-files.picoctf.net/c_verbal_sleep/4aee1b9778a8e56724d015b027431fb236853a94f53e5dcf32c5ed32aed404da/bininst2.zip). Unzip the archive with the password picoctf

## Hints
1. Frida is an easy-to-install, lightweight binary instrumentation toolkit
2. Try using the CLI tools like frida-trace
3. You can specify the exact function name you want to trace

## Write-up
This challenge was quite similar to challenge [Binary Instrumentation 1](https://github.com/tlmt009147/picoCTF2025/blob/178c2153b7aaff95ec7f42a87ab20ca2e1393547/RE/Binary%20Instrumentation%201/README.md). A function was called in the start section and an embedded program was loaded into memory in execution process.

![](https://github.com/tlmt009147/picoCTF2025/blob/178c2153b7aaff95ec7f42a87ab20ca2e1393547/RE/Binary%20Instrumentation%202/1.png)

Inside this function, a temporary process was called through rbx register as in Binary Instrumentation 1.

![](https://github.com/tlmt009147/picoCTF2025/blob/178c2153b7aaff95ec7f42a87ab20ca2e1393547/RE/Binary%20Instrumentation%202/2.png)

Finally, I found a variable that was ready to be written to a file or given to a function below it a few lines, but something stopped it from doing it properly.
Anyway I clicked the variable to view the full value of the variable.

![](https://github.com/tlmt009147/picoCTF2025/blob/178c2153b7aaff95ec7f42a87ab20ca2e1393547/RE/Binary%20Instrumentation%202/3.png)

![](https://github.com/tlmt009147/picoCTF2025/blob/178c2153b7aaff95ec7f42a87ab20ca2e1393547/RE/Binary%20Instrumentation%202/4.png)

Another base64 encoding, I deciphered it and got the flag.

![](https://github.com/tlmt009147/picoCTF2025/blob/178c2153b7aaff95ec7f42a87ab20ca2e1393547/RE/Binary%20Instrumentation%202/5.png)

## Flag
picoCTF{fr1da_f0r_b1n_in5trum3nt4tion!_b21aef39}


