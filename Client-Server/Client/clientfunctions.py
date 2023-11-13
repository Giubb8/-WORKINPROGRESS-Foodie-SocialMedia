import socket
import CODES

# Shutdown and close the socket
def disconnect_to_server(server):
    server.shutdown(socket.SHUT_RDWR)
    server.close()

def conn_to_server(hostname,port):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((hostname,port))
    return server

def sign_in(server):
    print('sign-in')
    checker=False
    while(checker != True):
        # Receiving Instructions from Server and sending Sign-Up Parameters to Server
        message = server.recv(1024).decode() # comm_7
        print(message)
        username = input()
        server.send(username.encode()) # comm_8
        
        message = server.recv(1024).decode() # comm_9
        print(message)
        password = input()
        server.send(password.encode()) # comm_10
        
        # Receving status operation code from server
        opcode = server.recv(1024).decode() # comm_11
        print(opcode)
        
        match opcode:
            case CODES.OPSUCCESS:    
                print("SIGN UP SUCCESSFUL")
                checker = True
            case CODES.INVALIDOPTION:
                print("INVALID USERNAME/PASSWORD")
            case CODES.ALREADYEXISTS:
                print("USERNAME ALREADY EXISTS")

def sign_up(server):
    print('signup')
    checker=False
    while(checker != True):
        # Receiving Instructions from Server and sending Sign-Up Parameters to Server
        message = server.recv(1024).decode() # comm_2
        print(message)
        username = input()
        server.send(username.encode()) # comm_3
        
        message = server.recv(1024).decode() # comm_4
        print(message)
        password = input()
        server.send(password.encode()) # comm_5
        
        # Receving status operation code from server
        opcode = server.recv(1024).decode() # comm_6 
        print(opcode)
        
        match opcode:
            case CODES.OPSUCCESS:    
                print("SIGN UP SUCCESSFUL")
                checker = True
            case CODES.INVALIDOPTION:
                print("INVALID USERNAME/PASSWORD")
            case CODES.ALREADYEXISTS:
                print("USERNAME ALREADY EXISTS")
            
