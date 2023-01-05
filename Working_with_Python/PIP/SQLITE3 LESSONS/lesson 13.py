import sqlite3

# Using SQlite3 in real life

def show_all():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM people")
    item = c.fetchall()
    for i in item:
        print(i)
    conn.commit()
    conn.close()

def insert_info(first, second, third):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO people VALUES (?,?,?)", (first,second,third))
    conn.commit()
    conn.close()

def delete_one(id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM people WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

def multiple_record(list):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.executemany("INSERT INTO people VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

def search_fuction(email):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM people WHERE email = (?)", (email,))
    search = c.fetchall()
    print(search)


