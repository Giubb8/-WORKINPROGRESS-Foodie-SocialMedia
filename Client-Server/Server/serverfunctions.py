import hashlib
import json
import sys

sys.path.insert(0, '/home/giubb8/Scrivania/PythonProject_1/Classes')
import utility as util
import sqlite3
import CODES

from Classes.User import User


    

# ULTIMA COSA FATTA: HO FATTO LA COMUNICAZIONE TRA CLIENT E SERVER PER IL SIGN IN DEVO GESTIRE E CONTROLLARE MEGLIO IL LOOP CHE TUTTO VADA BENE
def sign_in(client):
    
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    
    print("sign-in")
    checker = False
    username,password='',''
    
    while(checker != True):
        print("dentro")
        client.send("Insert Username".encode()) # comm_7
        username = client.recv(1024).decode() # comm_8
        
        client.send("Insert Password".encode()) # comm_9
        password = client.recv(1024) # comm_10
        password = hashlib.sha256(password).hexdigest()
        
        cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?",(username,password))
        res=cur.fetchall()

        if res:
            client.send(CODES.OPSUCCESS.encode()) # comm_11
            return (True,username)
        else:
            client.send(CODES.OPFAILURE.encode()) # comm_11
            return (False,'')


def sign_up(client):
    checker = False
    username=''
    password=''
    while(checker != True):
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
            
    util.add_user_to_db(username,password)
    return username
    
    # TODO CREARE USER E AGGIUNGERE A DIZIONARIO UTENTI
        
    
def s_check_friends_requests(server,user:User):
    # Ask server the friends request list
    data = str(user.get_friends())  
    
    server.send(data.encode()) # comm_13
    
    # Select with cli the friend
    # Accept or Deny
    pass
        
def s_send_friend_request(client,user:User,users_state:dict):
    while(True):
        friend_name = client.recv(1024).decode()
        if(users_state.keys(friend_name)):
            users_state[friend_name].add_request(user.get_username())
            client.send(CODES.OPSUCCESS).encode()
            break
        elif(user.get_requests().count(friend_name) > 0):
            user.add_friend(friend_name)
            users_state[friend_name].add_friend(user.get_username())
        else:
            client.send(CODES.OPFAILURE).encode()

def s_remove_friend(client,user:User,users_state:dict):
    while(True):
        friend_name = client.recv(1024).decode()
        user_friends_list = user.get_friends
        if(friend_name in user_friends_list):
            user_friends_list.remove(friend_name)
            users_state[friend_name].get_friends.remove(user.get_username())
            client.send(CODES.OPSUCCESS).encode()
            break
        else:
            client.send(CODES.OPFAILURE).encode()
    
def board(client,user:User,users_state:dict):
        print(user)
        
        print(f"THIS IS THE BOARD of {user.get_username()} ")
        while(True):
            option = client.recv(1024).decode() # comm_12
            match option:
                case '1':
                    s_check_friends_requests(client,user)
                    pass
                case '3':
                    s_send_friend_request(client,user,users_state)
        
