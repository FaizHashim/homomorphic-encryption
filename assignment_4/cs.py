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

HOST = "0.0.0.0"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST,PORT))
    while True:
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Received connection from {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                qu_in = json.loads(data.decode())
                query_d = open("query_data/query_data.txt", "a")
                query_d.write(str(qu_in["data"]) + "\n")
                query_d.flush()
                print(qu_in["data"])
                qu_out = {"result": calculate_prime_factors(qu_in["data"])}
                factors_d = open("factors_data/factors_data.txt", "a")
                factors_d.write(str(qu_out["result"]) + "\n")
                factors_d.flush()
                conn.sendall(json.dumps(qu_out).encode())