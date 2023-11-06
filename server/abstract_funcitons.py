import socket, sys
from .settings import DEFAULT_SIZE

def receive(client:socket.socket):
    size = client.recv(DEFAULT_SIZE)
    return client.recv(size)

def send(client:socket.socket, data:bytes):
    client.send(sys.getsizeof(data))
    client.send(data)
