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
        
        print(f"{password} client")
        server.send(password.encode()) # comm_10
        
        # Receving status operation code from server
        opcode = server.recv(1024).decode() # comm_11
        
        CODES.opcode_check(opcode,checker)
        print(opcode,checker)
        if(opcode==CODES.OPCODE.OPSUCCESS):
            print('Login Successful')
            checker = False
        else:
            print('Login Failed')
        return

def sign_up(server):
    """ Function to signing-up to Foodie, exchange needed info (username and password)
    with the server

    Args:
        server ( Socket Connection ): Socket connection with the server
    """
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
        
        CODES.opcode_check(opcode,checker)
        return 
            
        
    
def check_friends_requests(server):
    # Ask server the friends request list
    requests = server.recv(1024).decode()
    
    for count,value in enumerate(requests):
        print(f"{count}) {value}") 
    # Select with cli the friend
    
    while(True):
        choice = input("Select the Request or -1 to exit") # TODO check if choice is not outofbound
        acc_or_deny = input('1 = Accept | 0 = Deny | ')
        
        server.send(choice).encode()
        if(choice == -1):
            break
            
        match acc_or_deny:
            case '1':
                print("You accepted the request")
                server.send(acc_or_deny).encode()              
            case '0':
                print("You denied the request")
                server.send(acc_or_deny).encode()
            case _:
                print("Enter a valid option")                
    
    # Accept or Deny
    pass

def check_friends_list(server):
    pass

def send_friend_request(server):
    
    while(True):
        friend_username = input("type the username")
        server.send(friend_username).encode() # comm_13
        opcode = server.recv(1024).decode() # comm_14
        if(opcode == CODES.OPCODE.OPSUCCESS):
            break
        
 
def board(server):
    """The Main Board of the client where they can select 
    which functionallity want to use 

    Args:
        server ( Spcket Connection): Socket connection with the Server
    """
    print("WELCOME TO THE FOODIE BOARD\nPLEASE SELECT AN OPTION:")
    while(True):
        print("1)CHECK FRIENDS REQUEST\n2)FRIENDS LIST\n3)SEND FRIEND REQUEST\n4)SCAN FOOD\n5)CHECK HISTORY\n6)SEND NOTIFICATION\n7)CLOSE")
        choice = input()
        server.send(choice.encode()) # comm_12
        match choice:
            case '1':
                check_friends_requests(server)
            case '3':
                send_friend_request(server)
                
