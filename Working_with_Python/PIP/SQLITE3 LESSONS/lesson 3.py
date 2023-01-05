import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# Inserting many records inside a table

many_customers = [
    ('Sergei','Brylev','sergei@brylev.com'),
    ('Hanna','Lissy','hanna@lissy.com'),
    ('George','Assy','george@assy.com')
]
c.executemany(f"INSERT INTO people VALUES (?,?,?)", many_customers)

conn.commit()

conn.close()
