from pwn import *  
import random
import time
from datetime import datetime

token_length = 20

# Tạo process chạy file Python
def get_python_process(python_file: str, timeout=5):
    proc = process(["python3", python_file])  
    proc.timeout = timeout  
    return proc

# Sinh token dựa trên thời gian
def get_random(time, length, seed_offset=0):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    t = time
    random.seed(t + seed_offset)  
    return ''.join(random.choice(alphabet) for _ in range(length))

# Test local
def test_local(python_file: str):
    p = get_python_process(python_file)
    
    print(p.recvuntil(b"\nEnter your guess for the token (or exit):").decode())  # Đọc thông báo

    t = int(time.time() * 1000)  # Lấy timestamp UTC
    for delta in range(-40, 10):  
        token = get_random(t, token_length, delta)
        p.sendline(token.encode())
        time.sleep(0.05)  # Chờ 50ms trước khi nhận phản hồi

        response = p.recv(timeout=2).decode().strip()  
        if not response:  
            print(f"[⚠️] Không nhận phản hồi, thử token khác...")
            continue  

        print(f"Delta: {delta} ms, Token: {token}, Response: {response}")
        if "Congratulations" in response:  
            break

    p.close()

if __name__ == "__main__":
    python_file = "token_generator.py"  
    test_local(python_file)

