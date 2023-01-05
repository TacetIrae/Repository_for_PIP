import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Primary key

c.execute("SELECT rowid, * FROM people")

items = c.fetchall()

for i in items:
    print(i)


conn.commit()

conn.close()
