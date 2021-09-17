'Chat room client'

import threading
import socket

ALIAS = input("Choose an alias >>> ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("Enter server ip address >>>")
server_port = input("Enter server port number >>>")
client.connect((server_ip, server_port))

def client_recieve():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "alias?":
                client.send(ALIAS.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

def client_send():
    while True:
        message = f"{ALIAS}: {input('')}"
        client.send(message.encode("utf-8"))

recieve_thread = threading.Thread(target=client_recieve)
recieve_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
