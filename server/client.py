import json
import socket
from .abstract_funcitons import *
from game_elements.question import Question
from .settings import KILLSIGNAL

class Client:
    def __init__(self, server_ip:str, server_port:int):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.connect((server_ip, server_port))
    
    def send_board(self, board:list[list[int]]):
        send(self.__s, json.dumps(board).encode())

    def recv_q(self) -> Question:
        data = receive(self.__s)
        return Question.from_json(data)

    def send_a(self, answer:int, time:int) -> str:
        """
        time = nr sec in care s-a raspuns (505 daca nu a rasp in timpul util)
        """
        send(self.__s, json.dumps([answer, time]).encode())
        return receive(self.__s).decode()

    def attack(self, coords:tuple[int, int]):
        send(self.__s, json.dumps(list(coords)).encode())

    def update_board(self) -> list[list[int]]:
        board = json.loads(receive(self.__s).decode())
        return board

    def close_connection(self):
        send(self.__s, KILLSIGNAL.encode())
        self.__s.close()
