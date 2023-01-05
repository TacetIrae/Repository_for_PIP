import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Inserting one record inside a table

c.execute("INSERT INTO people VALUES ('Egor', 'Brylev', 'egor@brylev.com')")

conn.commit()

conn.close()
