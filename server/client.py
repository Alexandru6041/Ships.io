import json
import socket
from .abstract_funcitons import *
from logger import Logger
from game_elements.question import Question

class Client:
    def __init__(self, server_ip:str, server_port:int, logger:Logger):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.connect((server_ip, server_port))
        self.logger = logger

        # self.logger.info('Client connected successfully!')
    
    def send_board(self, board:list[list[int]]):
        send(self.__s, json.dumps(board).encode())
        # self.logger.status_update('Board sent!')

    def recv_q(self) -> Question:
        data = receive(self.__s)
        return Question.from_json(data)

    def send_a(self):
        pass

    def attack(self):
        pass

    def update_boards(self):
        pass

    def close_connection(self):
        self.__s.close()
