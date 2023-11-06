import socket
from logger import Logger

class Server:
    def __init__(self, server_ip:str='0.0.0.0', port:int=8000, logger=Logger):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((server_ip, port))
        self.logger = logger
        self.players = []
    
    def start_listening(self):
        self.__server.listen(0)
        self.logger.info('Server started listening')

        self.receive_connections()
    
    def receive_connections(self):
        while len(self.players) < 2:
            client_socket, client_address = self.__server.accept()
    
    def close(self):
        # TODO Close player connections
        self.__server.close()
