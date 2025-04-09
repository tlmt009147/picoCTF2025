



```bash
$ bitlocker2john -i bitlocker-1.dd > hash.txt
```

```bash
$ john pass_hash.txt --wordlist:/usr/share/wordlists/rockyou.txt
```

```bash
$ sudo mkdir /mnt/bitlocker
$ sudo mkdir /mnt/dislocker
```

```bash
$ sudo dislocker -V bitlocker-1.dd -u"jacqueline" -- /mnt/dislocker
$ sudo mount -o loop /mnt/dislocker/dislocker-file /mnt/bitlocker
```

## Flag
picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}
