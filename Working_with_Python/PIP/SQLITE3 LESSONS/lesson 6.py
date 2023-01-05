import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Search for specific information in database

c.execute("SELECT * FROM people WHERE last_name = 'Brylev'")
# c.execute("SELECT * FROM people WHERE age >= 20 ")
# c.execute("SELECT * FROM people WHERE last_name LIKE 'B%'")
# c.execute("SELECT * FROM people WHERE email LIKE '%.com')

items = c.fetchall()

for i in items:
    print(i)


conn.commit()

conn.close()