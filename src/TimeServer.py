import socket
import time


class TimeServer:
    def __init__(self, host='localhost', port=99):
        # Szerver socket inicializálása
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(1)
        self.conn = None

    def run(self):
        print('Szerver elindítva...')
        self.conn, addr = self.s.accept()
        print(f'Csatlakozott: {addr}')

        # Időküldés a kliensnek
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            self.conn.sendall(f'{time.time()} {data.decode()}'.encode())
