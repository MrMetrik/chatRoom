'Chat room Server'


import threading
import socket 

class ChatRoom:
    HOST = "127.0.0.1"
    PORT = 6968
    encoding = "utf-8"
    clients = []
    aliases = []

    def __init__(self, host = "127.0.0.1", port = 6967):
        self.HOST = host
        self.PORT = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen()
    
    def eject_client(self, client):
        index = self.clients.index(client)
        self.clients.remove(client)
        client.close()
        alias = self.aliases[index]
        self.aliases.remove(index)
        return alias


    def broadcast(self, message):
        for client in self.clients:
            client.send(message)
    
    def handle_clients(self, client):
        while True:
            try:
                message = client.recv(2048)
                if (message != "eject"):
                    self.broadcast(message)
                else:
                    alias = self.eject_client(client)
                    self.broadcast(f"{alias} has left the chat room!!")
            except:
                alias = self.eject_client(client)
                self.broadcast(f"{alias} has left the chat room!!")
                break
    
    def manage_clients(self):
        while True:
            print("Server is up and running...")
            client, address = self.server.accept()
            
            print(f"Connection is established with {str(address)}")
            client.send("alias??".encode(self.encoding))
            alias = client.recv(1024).decode(self.encoding)

            self.aliases.append(alias)
            self.clients.append(client)

            print(f"The alias of this client is {alias}")
            self.broadcast(f"{alias} is now connected to the chat room.".encode(self.encoding))

            client.send("You are now connected!!".encode(self.encoding))

            thread = threading.Thread(target=self.handle_clients, args=(client, ))
            thread.start()
    

if __name__ == "__main__":
    chatroom = ChatRoom()
    chatroom.manage_clients()

    