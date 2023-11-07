import socket
from server.abstract_funcitons import send, receive, fill_algorithm
from game_elements.question import Question
from random import randint
import json as js
from .settings import KILLSIGNAL, TIME_LIMIT, Question_List
from .exceptions import KillException
import time

#-----------------------------------
#SIGNALS: 0 -> continue, 1 -> repeat
#-----------------------------------

class Player:
    def __init__(self, soc:socket.socket, table:list[list[int]]):
        self.soc = soc
        self.table = table

class Handler:
    @staticmethod
    def recv(client:socket.socket):
        data = receive(client)
        if data.decode() == KILLSIGNAL:
            raise KillException
        
        return data
    
    @staticmethod
    def send(client:socket.socket, data:bytes):
        send(client, data)
        
class Server:
    def __init__(self, server_ip:str='0.0.0.0', port:int=8000):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((server_ip, port))
        # print(self.__server.getsockname())
        self.players = []
    
    def start_listening(self):
        self.__server.listen(0)
        # self.logger.info('Server started listening')

        print(f"Server stared listening: ")
        
        self.receive_connections()
  
    def receive_connections(self):
        while len(self.players) < 2:
            client_socket, client_address = self.__server.accept()
            print(f"Connection from {client_address} has been established!")
            table = js.loads(Handler.recv(client_socket).decode())
            self.players.append(Player(client_socket, table))
            print('\n' * 5)
            
    
    def close(self):
        # TODO Close player connections
        self.__server.close()

    def run(self):
        STAGES = ['QS', 'AS']
        i = 0
        self.stage_winner = -1
        while True:
            match i:
                case 0:
                    signal = self.question_stage(randint(0, len(Question_List)))
                    i += 1 if not signal else 0
                case 1:
                    self.attack_stage()
                    i += 1
                case _:
                    pass
            
            i %= len(STAGES)
                    
    def set_stage_winner(self, winner:int):
        self.stage_winner = winner
    
    def attack_stage(self):
        player1, player2 = self.players
        winner, loser = (player1, player2) if self.stage_winner == 1 else (player2, player1)
        x, y = js.loads(Handler.recv(winner.soc))

        fill_algorithm(loser.table, x, y)        
        # Masking the table
        
        Handler.send(loser.soc, js.dumps([loser.table, masked(winner.table)]).encode())
        time.sleep(1)
        Handler.send(winner.soc, js.dumps([winner.table, masked(loser.table)]).encode())
        
    def question_stage(self, q:int) -> int:
        player1, player2 = self.players
        
        # RETRIEVE QUESTION
        question = Question_List[q]
        Question_List.pop(q)
        # Handler.send QUESTION
        Handler.send(player1.soc, question.as_bytes())
        Handler.send(player2.soc, question.as_bytes())
        # GET ANSWERS
        answer1, time1 = js.loads(Handler.recv(player1.soc).decode())
        answer2, time2 = js.loads(Handler.recv(player2.soc).decode())
        
        # judge answers
        b1 = (time1 <= TIME_LIMIT and answer1 == question.correct)
        b2 = (time2 <= TIME_LIMIT and answer2 == question.correct)
        
        if(b1 and b2):
            if(time1 < time2):
                Handler.send(player1.soc, 'true'.encode())
                Handler.send(player2.soc, 'false'.encode())
                self.set_stage_winner(1)
                        
            elif(time2 < time1):
                Handler.send(player2.soc, 'true'.encode())
                Handler.send(player1.soc, 'false'.encode())
                self.set_stage_winner(2)
                
            else:
                Handler.send(player1.soc, "rerun".encode())
                Handler.send(player2.soc, "rerun".encode())
                self.set_stage_winner(-1)
                
                return 1
            
        elif(b1 or b2):
            if b1:
                Handler.send(player1.soc, 'true'.encode())
                Handler.send(player2.soc, 'false'.encode())
                self.set_stage_winner(1)

            else:
                Handler.send(player2.soc, 'true'.encode())                
                Handler.send(player1.soc, 'false'.encode())
                self.set_stage_winner(2)
        else:
            Handler.send(player1.soc, "rerun".encode())
            Handler.send(player2.soc, "rerun".encode())
            self.set_stage_winner(-1)
            return 1
    
        return 0

def masked(m):
    mask = [[0 if m[i][j] == 1 else m[i][j] for j in range(len(m[0]))] for i in range(len(m))]      
    print(mask)
    
    return mask