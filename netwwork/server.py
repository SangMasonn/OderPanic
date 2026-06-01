import socket
import json

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server đang chạy...")
print("Chờ Player 2 kết nối...")

conn, addr = server.accept()
print("Player 2 đã kết nối:", addr)

player1_pos = [100, 100]
player2_pos = [300, 100]

while True:
    try:
        data = conn.recv(1024).decode()

        if not data:
            break

        player2_pos = json.loads(data)

        game_state = {
            "player1": player1_pos,
            "player2": player2_pos
        }

        conn.send(json.dumps(game_state).encode())

    except:
        break

conn.close()
server.close()