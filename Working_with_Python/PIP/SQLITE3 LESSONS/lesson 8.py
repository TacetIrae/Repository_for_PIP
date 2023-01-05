import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# How to delete a record

c.execute("DELETE FROM people WHERE rowid = 4")

conn.commit()

conn.close()