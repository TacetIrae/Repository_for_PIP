import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Limit

def basic_limit():
    c.execute("SELECT rowid, * FROM people LIMIT 2")
    item = c.fetchall()
    print(item)
def advanced_limit():
    c.execute("SELECT rowid, * FROM people ORDER BY rowid DESC LIMIT 2")
    item = c.fetchall()
    print(item)

basic_limit()

conn.commit()
print()
conn.close()