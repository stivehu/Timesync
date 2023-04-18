import os
import socket
import time


class TimeClient:
    def __init__(self, host='localhost', port=99):
        self.HOST = host
        self.PORT = port

    def run(self):
        # Kliens socket inicializálása
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))
        request_time = time.time()
        self.s.sendall(str(request_time).encode())
        # Időszinkronizáció
        data = self.s.recv(1024)
        self.s.close()
        # Hálózati késleltetés kiszámítása
        response_time, request_time = map(float, data.decode().split())
        network_delay = (time.time() - request_time - (response_time - request_time)) / 2

        current_time = response_time + network_delay
        self.set_time(current_time)

    def set_time(self, current_time):
        print(f'Kapott idő: {current_time}')
        os.system(f'date -s @{int(current_time)}; date -u -s "$(date -u +"%Y-%m-%d %H:%M:%S") GMT"')
