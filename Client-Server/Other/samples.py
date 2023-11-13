import sqlite3
import hashlib

conn = sqlite3.connect('./userdata.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)     
""")

username1,password1 = "andreasample", hashlib.sha256(b"andreapassword").hexdigest()
username2,password2 = "Fabio", hashlib.sha256(b"Fabiopassword").hexdigest()
username3,password3 = "Andrea", hashlib.sha256(b"Andreapassword").hexdigest()
username4,password4 = "Stefania", hashlib.sha256(b"Stefaniapassword").hexdigest()

# Using Prepared Statement
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username1,password1))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username2,password2))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username3,password3))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username4,password4))


conn.commit()
cur.execute("SELECT * FROM userdata")
res = cur.fetchall()

for row in res:
    print(row)
print(username1,password1)
