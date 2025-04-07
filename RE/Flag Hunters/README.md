# Flag Hunters
## Description
Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you.
The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/94196e43010d5524e59502a24ec791d7ae7fc7799fd2d31c87ff04baa746b153/lyric-reader.py).

Connect to the program with netcat: $ nc verbal-sleep.picoctf.net 59898

## Hints
1. This program can easily get into undefined states. Don't be shy about Ctrl-C.
2. Unsanitized user input is always good, right?
3. Is there any syntax that is ripe for subversion?

## Write-up
This challenge was not hard to solve but it took me quite a time to find the key feature that led to the flag. First, I downloaded the source code to inspect the flow of the program. The flag of the challenge was read from a file and inserted into the start of the paragraphs.

![1](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Flag%20Hunters/1.png)

When I tried to netcat to connect to the program, I saw that the part containing the flag was not printed, instead, there was a prompt for something that I thought to be a payload to extract the flag. 

![4](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Flag%20Hunters/4.png)

Further reading showed that the reader() function is the main feature responsible for the logical operation of the program. Some indexes were initialized and assigned in the first part of the function. The lines of the poem were also split here. This was not very critical so I will skip through it.

![2](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Flag%20Hunters/2.png)

Next is the important part containing a flaw that we can manipulate to get the flag.

![3](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Flag%20Hunters/3.png)

The flow of this can be simply explained by this: Each line of the poem split in the previous part was then split again by the character ";". This was the prerequisite part for us to get the flag. Then each line of the song was read and checked for certain conditions. If the line was the phrase "REFRAIN", the line at the index refrain_return was also changed, the lip variable was updated to refrain and the next line read was changed either. If the line was "CROWD", the program prompted for user input, which is similar to when we netcat. And if the line is "RETURN" with a numerical number, the next line being read would be the line at the index after the word "RETURN". 

So I solved this by inserting the phrase ";RETURN 0". The ";" character was used to split my payload into a single line of a song so that it could be checked. My purpose was to direct the next line read to the start of the song so it could print out the flag. And I successfully forced the program to reveal the flag. 

![5](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Flag%20Hunters/5.png)

## Flag
picoCTF{70637h3r_f0r3v3r_c659e814}







