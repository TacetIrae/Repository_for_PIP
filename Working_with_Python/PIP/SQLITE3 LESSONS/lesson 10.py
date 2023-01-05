import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

#  and , or
def a_nd ():
    c.execute("SELECT rowid, * FROM people WHERE last_name LIKE 'B%' AND rowid = 2")

    item = c.fetchall()

    print(item)
def o_r():
    c.execute("SELECT rowid, * FROM people WHERE last_name LIKE 'B%' OR rowid = 2")
    item = c.fetchall()
    print (item)

a_nd()
o_r()

conn.commit()

conn.close()