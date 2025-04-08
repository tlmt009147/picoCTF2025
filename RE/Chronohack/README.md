# Chronohack
## Description
Can you guess the exact token and unlock the hidden flag?

Our school relies on tokens to authenticate students. Unfortunately, someone leaked an important [file for token generation'](https://challenge-files.picoctf.net/c_verbal_sleep/b87dd5254a4b7693feffbd91a463d911a2b143aef4bae911dc09d61a6b6f56a0/token_generator.py). Guess the token to get the flag.
Additional details will be available after launching your challenge instance.

## Hints
1. https://www.epochconverter.com/
2. https://learn.snyk.io/lesson/insecure-randomness/
3. Time tokens generation
4. Generate tokens for a range of seed values very close to the target time

## Write-up
This challenge was quite daunting for me due to the latency between the server and my device. To solve this more smoothly, I consider further readings about epoch and insecure randomness in the links in the Hints title.

First, I downloaded the source code for this challenge. It was a program used for token generation based on the epoch time when the token was created.
A random integer was chosen with the epoch chosen as the seed. Because the seed was initialized, a randomly generated chain of numbers would be the same every time the program ran as long as the seed remained unchanged. Below is the source code.

```python
import random
import time

def get_random(length):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(int(time.time() * 1000))  # seeding with current time 
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

def flag():
    with open('/flag.txt', 'r') as picoCTF:
        content = picoCTF.read()
        print(content)


def main():
    print("Welcome to the token generation challenge!")
    print("Can you guess the token?")
    token_length = 20  # the token length
    token = get_random(token_length) 
    print(token)
    

    try:
        n=0
        while n < 50:
            user_guess = input("\nEnter your guess for the token (or exit):").strip()
            n+=1
            if user_guess == "exit":
                print("Exiting the program...")
                break
            
            if user_guess == token:
                print("Congratulations! You found the correct token.")
                flag()
                break
            else:
                print("Sorry, your token does not match. Try again!")
            if n == 50:
                print("\nYou exhausted your attempts, Bye!")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting the program...")

if __name__ == "__main__":
    main()

```

Our mission was to find out the token generated to get the flag. As I said, latency was a big problem so the program let us have 50 tries I developed 2 programs to to test the latency between running code locally and through Netcat. The difference was up to 98 seconds in my case, much more than the limit of 50 tries, so I suggest you be patient and change the range of the target time if the first run is not successful.

```python
for delta in range(-150, 10):  
```
![](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Chronohack/1.png)

You can see that the latency was up to 143 seconds at this time I ran.

Script for local test [here](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Chronohack/local.py).

Script for Netcat test [here](https://github.com/tlmt009147/picoCTF2025/blob/main/RE/Chronohack/solve.py).

## Flag
picoCTF{UseSecure#$_Random@j3n3r@T0rsddf1e4a2}


