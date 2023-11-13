import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))

server.listen()


def handle_connection(client):
    client.send("Username: ".encode())
    username = client.recv(1024).decode()    
    client.send("Password: ".encode())
    password = client.recv(1024)
    
    password = hashlib.sha256(password).hexdigest()
    
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?",(username,password))
    
    if cur.fetchall():
        client.send("Login Succesful".encode())
    else:
        client.send("Login Failed".encode())


while(True):
    client,addr = server.accept()
    threading.Thread(target=handle_connection,args=(client,)).start()