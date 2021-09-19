'Chat room client'

import threading
import socket

class chatRoomClient:

    ALIAS = "johnDoe"
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = "127.0.0.1"
    port = 6969
    encoding = "utf-8"

    def __init__(self, ip="127.0.0.1", port=6967):
        self.ALIAS = input("Choose an alias >>> ")
        self.ip = ip
        self.port = port
        self.client.connect((self.ip, self.port))
    
    def client_recieve(self):
        while True:
            try:
                message = self.client.recv(2048).decode(self.encoding)
                if message == "alias??":
                    self.client.send(self.ALIAS.encode(self.encoding))
                else:
                    print(message)
            except:
                print("Error!")
                self.client.close()
                break

    def client_send(self):
        while True:
            message = f"{self.ALIAS}: {input('')}"
            self.client.send(message.encode(self.encoding))
    
    def start_client(self):
        rThread = threading.Thread(target=self.client_recieve)
        rThread.start()
        sThread = threading.Thread(target=self.client_send)
        sThread.start()


if __name__ == "__main__":
    chatClient = chatRoomClient()
    chatClient.start_client()


    
