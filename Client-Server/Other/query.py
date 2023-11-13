import sqlite3

conn = sqlite3.connect('userdata.db')
cur = conn.cursor()
cur.execute("SELECT * FROM userdata")
res = cur.fetchall()

for row in res:
    print(row)
