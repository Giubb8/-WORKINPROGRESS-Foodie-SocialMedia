import socket
import clientfunctions as clfun

# TODO define in txt file
hostname = 'localhost'
port = 9999

def main():

    # Connecting to Server # TODO CHECK IF EVERYTHING ALL RIGHT EXCEPTIONS
    server = clfun.conn_to_server(hostname,port)
    print("WELCOME TO NUTRITION")
    
    message = server.recv(1024).decode() # comm_0
    print(message)
    
    
    while(True):
        option = input("Option: \n")
        server.send(option.encode()) # comm_1
        match option:
            case '1':
                clfun.sign_up(server)
                break
            case '2':
                clfun.sign_in(server)
                break
            case _:
                print("PLEASE SELECT A VALID OPTION")
    
    
if __name__ == "__main__":
    main()