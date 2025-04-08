import time
import random
import string
from pwn import *  # Thư viện pwn để tương tác với server qua netcat
token_length = 20
# Hàm tạo token dựa trên seed
def get_random(time, length, seed_offset=0):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    t = time
    random.seed(t + seed_offset)  
    return ''.join(random.choice(alphabet) for _ in range(length))

# Thử đoán token
def guess_token():
    # Kết nối đến server
    p = remote("verbal-sleep.picoctf.net", 49863)  
    
    print(p.recvuntil(b"\nEnter your guess for the token (or exit):").decode())  # Đọc thông báo

    t = int(time.time() * 1000)  # Lấy timestamp UTC
    for delta in range(-100, 10):  
        token = get_random(t, token_length, delta)
        p.sendline(token.encode())
        time.sleep(0.05)  # Chờ 50ms trước khi nhận phản hồi

        response = p.recv(timeout=2).decode().strip()  
        if not response:  
            print(f"SOS")
            continue  

        print(f"Delta: {delta} ms, Token: {token}, Response: {response}")
        if "Congratulations" in response:  
            break

    p.close()

# Chạy chương trình
def main():
    guess_token()

if __name__ == "__main__":
    main()
