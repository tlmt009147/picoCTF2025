# Bitlocker-1
## Description
Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!
Download the disk image [here](https://challenge-files.picoctf.net/c_verbal_sleep/9e934e4d78276b12e27224dac16e50e6bbeae810367732eee4d5e38e6b2bb868/bitlocker-1.dd)

## Hints
1. Hash cracking

## Write-up
First I used bitlocker2john to generate a hash for the disk image.

```bash
$ bitlocker2john -i bitlocker-1.dd > hash.txt
```
Here is the hash.txt file after hashing.

![](https://github.com/tlmt009147/picoCTF2025/blob/de5bf7f2b1c32a95b6b66efbf6acbcfcd8f455c9/Forensics/Bitlocker-1/1.png)

```bash
$ john pass_hash.txt --wordlist:/usr/share/wordlists/rockyou.txt
```
Then I used John the Ripper to crack the first hash -User Password hash (I copied it to another file) with the wordlist rockyou.txt. After a few minutes of waiting, I got the password

![](https://github.com/tlmt009147/picoCTF2025/blob/de5bf7f2b1c32a95b6b66efbf6acbcfcd8f455c9/Forensics/Bitlocker-1/2.png)

```bash
$ sudo mkdir /mnt/bitlocker
$ sudo mkdir /mnt/dislocker
```
Then I made two directories to store the decrypted disk file and mounted it.

```bash
$ sudo dislocker -V bitlocker-1.dd -u"jacqueline" -- /mnt/dislocker
$ sudo mount -o loop /mnt/dislocker/dislocker-file /mnt/bitlocker
```
After mounting, we just need to visit the site and get the flag.

![](https://github.com/tlmt009147/picoCTF2025/blob/de5bf7f2b1c32a95b6b66efbf6acbcfcd8f455c9/Forensics/Bitlocker-1/3.png)

## Flag
picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}
