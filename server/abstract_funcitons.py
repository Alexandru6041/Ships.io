import socket, sys
from .settings import DEFAULT_SIZE

def receive(client:socket.socket):
    size = int(client.recv(DEFAULT_SIZE).decode())
    return client.recv(size)

def send(client:socket.socket, data:bytes):
    client.send(f'{sys.getsizeof(data)}'.encode())
    client.send(data)
