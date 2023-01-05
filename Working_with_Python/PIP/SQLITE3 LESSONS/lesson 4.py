import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Query and fetchall

c.execute("SELECT * FROM people")
items = c.fetchall()

for item in items:
    print(item[0] + " " + item[1] + "|\t" + item[2])
# for item in items:
#   print(item[0])
#   print(item[1])
#   print(item[2])

# c.execute("SELECT * FROM people")
# print(c.fetchone())
# print()

# c.execute("SELECT * FROM people")
# print(c.fetchmany(2))

conn.commit()

conn.close()
