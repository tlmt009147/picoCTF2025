# Bitlocker-2
## Description
Jacky has learnt about the importance of strong passwords and made sure to encrypt the BitLocker drive with a very long and complex password. We managed to capture the RAM while this drive was opened however. See if you can break through the encryption!

Download the disk image [here](https://challenge-files.picoctf.net/c_verbal_sleep/b22e1ca13c0b82bb85afe5ae162f6ecbdf5b651e364e6a2b57c9ad44ae0b3bfd/bitlocker-2.dd) and the RAM dump [here](https://challenge-files.picoctf.net/c_verbal_sleep/b22e1ca13c0b82bb85afe5ae162f6ecbdf5b651e364e6a2b57c9ad44ae0b3bfd/memdump.mem.gz)

## Hints
1. Try using a volatility plugin

## Write-up
About the installation of volatility2, please search on the Internet for more information as it is quite a challenge to do it here. Remember volatility2 uses Python version 2.7 so please make sure that you have it on your device.

Okay if you can overcome the challenges of installing volatility2, then congrats, you bypass the most difficult phase. 

According to the hint, we must use a tool called volatility2 and its plugins to decrypt the disk image file. I searched on the Internet for some plugins and I came across this [one](https://github.com/breppo/Volatility-BitLocker). The installation is simple, you just need to follow the guidelines in the link or just barely copy the bitlocker.py file into the volatility plugin path:

```bash
cp bitlocker.py path/to/volatility/volatility/plugins/ 
```

After I got the profile of the memory dump file, I used the plugin to get the FVEK key.

```bash
$ python2.7 vol.py -f ../memdump.mem imageinfo
```
![](https://github.com/tlmt009147/picoCTF2025/blob/4c07543ecff0796c3be5981194c024da64954610/Forensics/Bitlocker-2/1.png)

```bash
$ python2.7 vol.py -f ../memdump.mem bitlocker --profile=Win10x64_19041
```
![](https://github.com/tlmt009147/picoCTF2025/blob/4c07543ecff0796c3be5981194c024da64954610/Forensics/Bitlocker-2/2.png)

Then I tried each FVEK key to decrypt the image file with bdemount, luckily on my first try, the file was decrypted successfully. At this point, you can use dislocker instead of bdemount if you want.

```bash
$ sudo mkdir /mnt/bitlocker
$ sudo bdemount -k 5b6ff64e4a0ee8f89050b7ba532f6256 ../bitlocker-2.dd /mnt/bitlocker/
$ sudo mkdir /mnt/Test
$ sudo mount -o loop,ro /mnt/bitlocker/bde1 /mnt/Test
```
Then I mounted the decrypted disk and got the flag.

![](https://github.com/tlmt009147/picoCTF2025/blob/4c07543ecff0796c3be5981194c024da64954610/Forensics/Bitlocker-2/3.png)

## Flag
picoCTF{B1tl0ck3r_dr1v3_d3crypt3d_9029ae5b}








