import utility as util
import sqlite3
import CODES

# ULTIMA COSA FATTA: HO FATTO LA COMUNICAZIONE TRA CLIENT E SERVER PER IL SIGN IN DEVO GESTIRE E CONTROLLARE MEGLIO IL LOOP CHE TUTTO VADA BENE
def sign_in(client,username,password):
    print("sign-in")
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    checker = False
    username=''
    password=''
    while(checker != True):
        print("dentro")
        client.send("Insert Username".encode()) # comm_7
        username = client.recv(1024).decode() # comm_8
        
        client.send("Insert Password".encode()) # comm_9
        password = client.recv(1024).decode() # comm_10

        cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?",(username,password))
    
        if cur.fetchall():
            client.send("Login Succesful".encode()) # comm_11
            return True
        else:
            client.send("Login Failed".encode()) # comm_11
            return False

# TODO CHECK VALID USERNAME AND PASSWORD, CHECK EXISTANCE
def sign_up(client):
    print("sign-up")
    checker = False
    username=''
    password=''
    while(checker != True):
        print("dentro")
        client.send("Insert Username".encode()) # comm_2
        username = client.recv(1024).decode() # comm_3
        
        client.send("Insert Password".encode()) # comm_4
        password = client.recv(1024).decode() # comm_5
        check1 = util.check_valid(username,password)
        check2 = util.check_existence(username)
        checker = ( check1 and check2 )
        if(checker == False):
            if(check1 == False): 
                client.send(CODES.INVALIDOPTION.encode()) # comm_6
            else:
                client.send(CODES.ALREADYEXISTS.encode()) # comm_6
        else:
            client.send(CODES.OPSUCCESS.encode()) # comm_6
            
    util.add_user(username,password)
    # TODO CREARE USER E AGGIUNGERE A DIZIONARIO UTENTI
        
    def board(client):
        print("THIS IS THE BOARD")