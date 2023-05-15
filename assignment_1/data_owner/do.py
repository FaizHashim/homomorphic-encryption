import socket
import json
from random import randint

HOST = "127.0.0.1"
PORT = 8080

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
                qu_no =  json.loads(data.decode())
            
                randno = randint(1, 10000)
                print(f"Random number generated : {randno}")

                qu_out = {"data": qu_no["query"] * randno}

                conn.sendall(json.dumps(qu_out).encode())