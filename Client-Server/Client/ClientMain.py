import socket
import clientfunctions as clfun
import sys
sys.stdin = open('./Test/input.txt', 'r')

# TODO define in txt file
hostname = 'localhost'
port = 9999

def main():

    # Connecting to Server # TODO CHECK IF EVERYTHING ALL RIGHT EXCEPTIONS
    server = clfun.conn_to_server(hostname,port)
    print("WELCOME TO FOODIE")
    checker = True
    while(checker): 
        print('ciao')
        message = server.recv(1024).decode() # comm_0
        print(message)
        option = input("Option: \n")
        server.send(option.encode()) # comm_1
        match option:
            case '1':
                clfun.sign_up(server)
            case '2':
                clfun.sign_in(server)
                print(checker)
                checker = False
                print(checker)
                
                break
            case '3':
                clfun.disconnect_to_server(server)
            case _:
                print("PLEASE SELECT A VALID OPTION")
                
    print("USCITO")
    clfun.board(server)
    clfun.disconnect_to_server(server)


if __name__ == "__main__":
    main()