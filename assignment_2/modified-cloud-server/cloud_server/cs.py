import socket
import json
from sage.all import *

def calculate_prime_factors(N):
    l = factor(N)
    l = str(l).split("*")
    return [int(x.strip().split('^')[0]) for x in l]

HOST = "127.0.0.1"
PORT = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
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
                qu_out = {"result": calculate_prime_factors(qu_in["data"])}

                conn.sendall(json.dumps(qu_out).encode())