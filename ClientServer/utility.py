
import hashlib
import sqlite3

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
    
def add_user(username,password):
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    user,pssw = username, hashlib.sha256(password.encode()).hexdigest()
    cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(user,pssw))
    conn.commit()
    
def check_values(type:str,min:int,max:int):
    pass

