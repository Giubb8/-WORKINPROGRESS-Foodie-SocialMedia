import json
import sys
import sqlite3
import hashlib
import socket
import threading
from multiprocessing import Manager,Process

sys.path.insert(0, '../ClientServer')


import utility as util
import serverfunctions as servfun
manager = Manager()

users_state = dict()

# Giving Options to Client, after sign-up or sign-in client goes to board
def handle_connection(client):
    # Asking option to client
    checker = False
    username=''
    while(checker != True):
        client.send("SELECT AN OPTION:\n1) SIGN UP\n2) SIGN IN\n3) EXIT".encode()) # comm_0
        option = client.recv(1024).decode() # comm_1
        print(option)
        match option:
            case '1':
                username = servfun.sign_up(client)
                process = Process(target=util.add_user_to_dict,args=(users_state,username))
                process.start()
            case '2':
                (checker,username) = servfun.sign_in(client)
    
    servfun.board(client,users_state[username],users_state)

def main():
    
    data=util.resume_state(users_state)
    print(dict(data))
    users_state.update(data)
    print(users_state)
    # Creating Server and Set to Listen for Connection
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost",9999))
    server.listen()
    # Main Loop: Accept Connection with Clients and start a new Thread for each Connection
    while(True):
        client,addr = server.accept()
        threading.Thread(target=handle_connection,args=(client,)).start() 
    
if __name__ == "__main__":
    main()