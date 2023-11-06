from server.host import Server

if __name__ == '__main__':
    server = Server(server_ip='192.168.1.252', logger=None)
    server.start_listening()
    server.close()