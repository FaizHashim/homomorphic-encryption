import socket
import json

def calculate_prime_factors(N):
    prime_factors = []
    if N % 2 == 0:
        prime_factors.append(2)
    while N % 2 == 0:
        N = N // 2
        if N == 1:
            return prime_factors
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.append(factor)
            while N % factor == 0:
                N = N // factor
                if N == 1:
                    return prime_factors

HOST = "127.0.0.1"
PORT = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    while True:
        s.listen()
        conn, addr = s.accept()

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                qu_in = json.loads(data.decode())
                qu_out = {"result": calculate_prime_factors(qu_in["data"])}

                conn.sendall(json.dumps(qu_out).encode())