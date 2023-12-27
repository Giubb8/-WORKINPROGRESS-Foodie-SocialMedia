import socket
import clientfunctions as clfun
import sys
#sys.stdin = open('./Test/input.txt', 'r')

# TODO define in txt file
hostname = 'localhost'
port = 9999

def main():
    """Main Function of the client """
    # Connecting to Server # TODO CHECK IF EVERYTHING ALL RIGHT EXCEPTIONS
    server = clfun.conn_to_server(hostname,port)
    print("WELCOME TO FOODIE")
    checker = True
    while(checker):
        message = server.recv(1024).decode() # comm_0
        print(f"{message}\n",flush=True)
        option = input("Option: ")
        server.send(option.encode()) # comm_1
        match option:
            case '1':
                clfun.sign_up(server)
            case '2':
                clfun.sign_in(server)
                print(checker)
                checker = False
                print(checker)
                
            case '3':
                clfun.disconnect_to_server(server)
            case _:
                print("PLEASE SELECT A VALID OPTION")
    clfun.board(server)
    clfun.disconnect_to_server(server)


if __name__ == "__main__":
    main()