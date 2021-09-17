'Char Room Server'

import threading 
import socket

# Setting up host ip
HOST = "127.0.0.1"

# Setting up the server port
PORT = 6969

# setting up the TCP socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the server to the host ip and port
server.bind((HOST, PORT))

# set the server to listen for connections
server.listen()

clients = []
aliases = []

# Function to broadcast messages sent 
# by a client to other clients
def broadcast(message):
    for client in clients:
        clients.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f"{alias} has left the chat room!".encode('utf-8'))
            aliases.remove(alias)
            break

# main function to recieve the client connections
def recieve():
    while True:
        print("Server is running and listening....")
        client, address = server.accept()
        print(f"Connection is established with {str(address)}")
        client.send("alias?".encode("utf-8"))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f"The alias of this client is {alias}.".encode("utf-8"))
        broadcast(f"{alias} has connected to the chat room.".encode("utf-8"))
        client.send("You are now connected!".encode("utf-8"))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    recieve()
