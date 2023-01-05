import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Ordering

def order_rowid ():
    c.execute("SELECT rowid, * FROM people ORDER BY rowid")

def order_descending():
    c.execute("SELECT rowid, * FROM people ORDER BY rowid DESC")
    items = c.fetchall()
    for i in items:
        print(i)
def order_ascending():
    c.execute("SELECT rowid, * FROM people ORDER BY rowid ASC")
    items = c.fetchall()
    for i in items:
        print(i)

def order_last_name():
    c.execute("SELECT rowid, * FROM people ORDER BY last_name")
    items = c.fetchall()
    for i in items:
        print(i)


order_descending()

order_ascending()

order_last_name()

conn.commit()

conn.close()