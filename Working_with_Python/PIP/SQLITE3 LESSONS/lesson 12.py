import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Delete a table

c.execute("DROP TABLE people")

conn.commit()
conn.close()