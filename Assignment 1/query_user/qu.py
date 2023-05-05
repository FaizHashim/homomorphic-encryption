import socket
import json

HOST = "127.0.0.1"
DO_PORT = 8080
CS_PORT = 9090

x = {}

x["query"] = int(input("Enter a number: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, DO_PORT))
    s.sendall(json.dumps(x).encode())
    do_in = s.recv(1024)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, CS_PORT))
    s.sendall(do_in)
    cs_in = s.recv(1024)
    print(json.loads(cs_in))