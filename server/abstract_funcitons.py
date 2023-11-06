import socket, sys
from .settings import DEFAULT_SIZE, TARGET_AREA

def receive(client:socket.socket):
    size = int(client.recv(DEFAULT_SIZE).decode())
    return client.recv(size)

def send(client:socket.socket, data:bytes):
    client.send(f'{sys.getsizeof(data)}'.encode())
    client.send(data)
    
def fill_algorithm(m:list[list[int]], X:int, Y:int):
    Q = [(X, Y)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    viz = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    
    while len(Q):
        x, y = Q[0]
        Q.pop(0)
        if(m[x][y] == 1):
            m[x][y] = 2
        
        for i in range(4):
            n_x, n_y = x + dx[i], y + dy[i]
            
            if X <= n_x < min(X + TARGET_AREA[0], len(m)) and Y <= n_y < min(Y + TARGET_AREA, len(m[0])) and not viz[n_x][n_y]:
                viz[n_x][n_y] = 1
                Q.append((n_x, n_y))