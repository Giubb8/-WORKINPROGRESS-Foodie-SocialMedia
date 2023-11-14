
import hashlib
import json
import pickle
import sqlite3
from multiprocessing import Manager,Process
import sys
sys.path.insert(0, './Classes')
from Classes.User import User
import jsonpickle
import pprint
from pathlib import Path

HERE = Path(__file__).parent

def check_valid(username,password):
    if(len(username)<5):
        print('INVALID USERNAME')
        return False
    elif(len(password)<5):
        print('INVALID PASSWORD')
        return False
    else:
        return True

def check_existence(username):
    
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()

    cur.execute('SELECT username FROM userdata WHERE username == (?)',[username])
    selection = cur.fetchall()
    if(len(selection) != 0):
        print(f"{username} IS NOT AVAILABLE")
        return False
    else:
        return True
    
def add_user_to_db(username,password):
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    user,pssw = username, hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(user,pssw))
    conn.commit()
    
def check_values(type:str,min:int,max:int):
    pass

def resume_state(users_state):
    #users_state.update({"TEST":User('test')})
    #print(users_state)
    #
    #with open('users.json','w') as f:
    #    jsonstring = jsonpickle.encode(users_state)
    #    json.dump(jsonstring,f)
    #users_state={}
    print(users_state)
    with open('./users.json','r') as f:
        jsonstring2 = json.load(f)
        print(jsonstring2)
        users_state=jsonpickle.decode(jsonstring2)
        print(users_state)
        return users_state
            
    
# NOT MULTIPROCESSING SAFE ALONE
def add_user_to_dict(users_state:dict,username):    
    # Adding to the current state dictionary
    users_state.update({username:User(username)})
    print(users_state)
    
    with open('users.json','w') as f:
        jsonstring = jsonpickle.encode(users_state)
        json.dump(jsonstring,f)