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
    """Function to Sign-In inside Foodie

    Args:
        client (Socket Connection): socket connection to single client

    Returns:
        Bool,String: Return a value for the caller 
        while loop (if true->break, if false -> not break) and the username of the 
        logged in user
    """
    # Connecting to Database
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    checker = False
    username,password='',''
    
    while(checker != True):
        # Receiving Username and Password from Client
        client.send("Insert Username".encode()) # comm_7
        username = client.recv(1024).decode() # comm_8

        client.send("Insert Password".encode()) # comm_9
        password = client.recv(1024) # comm_10
        password = hashlib.sha256(password).hexdigest()
        
        # Extracting Data from DB with Query
        cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?",(username,password))
        res=cur.fetchall()
        if res: # If Username and Password Match
            client.send(CODES.OPSUCCESS.encode()) # comm_11
            return (True,username)
        else: 
            client.send(CODES.OPFAILURE.encode()) # comm_11
            return (False,'')


def sign_up(client):
    """Function to sign-up inside Foodie, check if username and password chosen are
    valid and if already used by someone else, if everything is OK add the user to DB

    Args:
        client (Socket Connection): socket connection to single client

    Returns:
        String: Registered Username
    """
    checker = False
    username,password='',''
    while(checker != True):
        # Receiving Username and Password from Client
        client.send("Insert Username".encode()) # comm_2
        username = client.recv(1024).decode() # comm_3
        client.send("Insert Password".encode()) # comm_4
        password = client.recv(1024).decode() # comm_5
        print(username,password)
        # Performing Check on received data
        check1 = util.check_valid(username,password)
        check2 = util.check_existence(username)
        checker = ( check1 and check2 )
        
        # Analyzing the results of the check and giving the client appropriate response
        if(checker == False):
            if(check1 == False): 
                client.send(CODES.INVALIDOPTION.encode()) # comm_6
            else:
                client.send(CODES.ALREADYEXISTS.encode()) # comm_6
        else:
            client.send(CODES.OPSUCCESS.encode()) # comm_6
    # If everything went OK add user to DB       
    util.add_user_to_db(username,password)
    return username
    
        
    
def s_check_friends_requests(client,user:User,users_state:dict):
    """Check all the pending friend requests of the connected user, it send the 
    list through socket comm. TODO the requests are here accepted or denied

    Args:
        client (socket connection): socket connection to single client
        user (User): Object containing all the necessary info about the logged user
        users_state (dict): Dictionary Containing User Objects,
    """
    # Ask server the friends request list
    data = str(user.get_requests())  
    
    client.send(data.encode()) # comm_13
    while(True):
        option = client.recv(1024).decode()
        if(option == -1):
            break
        acc_deny = client.recv(1024).decode()
        
        if(acc_deny==1):
            users_state.get(data[option]).add_friend(user.get_username())
            users_state.get(user.get_username()).add_friend(data[option])
    # Select with cli the friend
    # Accept or Deny
    pass
        
def s_send_friend_request(client,user:User,users_state:dict):
    """The connected user send to the socket the username of the friend who want to 
    add to his friends list, then the existence of the userame is checked, if there was
    an already pending request from this user it's automatically accepted, otherwise
    the request is added to the user list

    Args:
        client (socket connection): socket connection to single client
        user (User): Object containing all the necessary info about the logged user
        users_state (dict): Dictionary Containing User Objects,
    """
    while(True):
        friend_name = client.recv(1024).decode()
        if(user.get_requests().count(friend_name) > 0): # If there was an already pending request from the desired friend
            user.add_friend(friend_name)
            users_state[friend_name].add_friend(user.get_username())
        elif(users_state.keys(friend_name)): # If name exist 
            users_state[friend_name].add_request(user.get_username())
            client.send(CODES.OPSUCCESS).encode()
            break
        else: # If name not exist
            client.send(CODES.OPFAILURE).encode()

def s_remove_friend_request(client,user:User,users_state:dict):
    """ Function to remove a friend from the connected user friends request list

        Args:
        client (socket connection): socket connection to single client
        user (User): Object containing all the necessary info about the logged user
        users_state (dict): Dictionary Containing User Objects,
    """
    while(True):
        friend_name = client.recv(1024).decode()
        if(user.get_requests().count(friend_name) > 0):
            user.remove_request(friend_name)
        else:
            client.send(CODES.OPFAILURE).encode()
            
def s_remove_friend(client,user:User,users_state:dict):
    """ Function to remove a friend from the connected user friends list

        Args:
        client (socket connection): socket connection to single client
        user (User): Object containing all the necessary info about the logged user
        users_state (dict): Dictionary Containing User Objects,
    """
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
    
# Once the user logged in move to board
def board(client,user:User,users_state:dict):
    """Main Board of Foodie, from here the user can select which function
    want to use

    Args:
        client (socket connection): socket connection to single client
        user (User): Object containing all the necessary info about the logged user
        users_state (dict): Dictionary Containing User Objects, 
    """
    print(user)
    
    print(f"THIS IS THE BOARD of {user.get_username()} ")
    while(True):
        option = client.recv(1024).decode() # comm_12
        match option:
            case '1':
                s_check_friends_requests(client,user,users_state)
                pass
            case '3':
                s_send_friend_request(client,user,users_state)
        
