import socket, sys
from .settings import DEFAULT_SIZE, TARGET_AREA, OK_MESSAGE

def receive(client:socket.socket):
    size = int(client.recv(DEFAULT_SIZE).decode())
    client.send(OK_MESSAGE.encode())
    data = client.recv(size)
    client.send(OK_MESSAGE.encode())

    return data

def send(client:socket.socket, data:bytes):
    client.send(f'{sys.getsizeof(data)}'.encode())
    if not client.recv(DEFAULT_SIZE).decode() == OK_MESSAGE:
        raise Exception
    
    client.send(data)
    if not client.recv(DEFAULT_SIZE).decode() == OK_MESSAGE:
        raise Exception

    
def fill_algorithm(m:list[list[int]], X:int, Y:int):
    Q = [(X, Y)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    viz = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    
    while Q:
        x, y = Q[0]
        Q.pop(0)

        for i in range(4):
            n_x, n_y = x + dx[i], y + dy[i]

            if 0 <= n_x < len(m) and 0 <= n_y < len(m[0]) and not viz[n_x][n_y]:
                if not m[n_x][n_y]:
                    viz[n_x][n_y] = -1
                    Q.append((n_x, n_y))
                
                elif m[n_x][n_y] == 1:
                    viz[n_x][n_y] = 1
                
                else: viz[n_x][n_y] = 100
        
    return viz