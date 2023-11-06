import socket
from logger import Logger
from server.abstract_funcitons import send, receive
from game_elements.question import Question
from random import randint

class Server:
    def __init__(self, server_ip:str='0.0.0.0', port:int=8000, logger=Logger):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((server_ip, port))
        # print(self.__server.getsockname())
        self.logger = logger
        self.players = []
    
    def start_listening(self):
        self.__server.listen(0)
        # self.logger.info('Server started listening')

        print("Server stared listening to: ")
        
        self.receive_connections()
        player1 = self.players[0]
        # player2 = self.players[1]
        
        Question_List = [
            Question("Cum o cheama pe mama", ["1", "2", "3"], 1),
            Question("Cum il cheama pe tata", ["3", "2", "1"], 0)
        ]
        # question_nr = randint(0, len(Question_List))
        question_nr = 0
        
        send(player1.soc, Question_List[question_nr].as_bytes())
        
  
    def receive_connections(self):
        while len(self.players) < 1:
            client_socket, client_address = self.__server.accept()
            table = receive(client_socket)
            self.players.append(Player(client_socket, table))
            print(table)
            print("\n\n\n\n\n")
    
    def close(self):
        # TODO Close player connections
        self.__server.close()


class Player:
    def __init__(self, soc:socket.socket, table:list[list[int]]):
        self.soc = soc
        self.table = table