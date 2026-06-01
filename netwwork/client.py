import socket
import json

class Client:
    def __init__(self, host_ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host_ip, 5555))

    def send(self, player_pos):
        try:
            self.client.send(json.dumps(player_pos).encode())
            data = self.client.recv(1024).decode()
            return json.loads(data)
        except:
            return None