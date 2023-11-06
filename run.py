from server.host import Server

if __name__ == '__main__':
    server = Server(server_ip='192.168.100.7', logger=None)
    server.start_listening()
    server.set_stage_winner(1)
    server.attack_stage()
    server.close()