from server.client import Client


server_ip = input('ip> ')
server_port = int(input('port> '))
c = Client(server_ip, server_port, None)

c.send_board([[1, 1, 1], [1, 0, 1]])
# q = c.recv_q()

# print(q.statement)
c.attack((1, 2))
boards = c.update_boards()
print(boards[0])
print(boards[1])

c.close_connection()