import sys
import sqlite3
import hashlib
import socket
import threading
sys.path.insert(0, '/home/giubb8/Scrivania/PythonProject_1/ClientServer')
import utility as util
import serverfunctions as servfun

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost",9999))
server.listen()


# Giving Options to Client, after sign-up or sign-in client goes to board
def handle_connection(client):
    # Asking option to client
    checker = False
    username=''
    while(checker != True):
        client.send("SELECT AN OPTION:\n1) SIGN UP\n2) SIGN IN".encode()) # comm_0
        option = client.recv(1024).decode() # comm_1
        print(option)
        match option:
            case '1':
                servfun.sign_up(client)
            case '2':
                (checker,username) = servfun.sign_in(client)
    
    servfun.board(client,username)
   

# Main Loop: Accept Connection with Clients and start a new Thread for each Connection
while(True):
    client,addr = server.accept()
    threading.Thread(target=handle_connection,args=(client,)).start()