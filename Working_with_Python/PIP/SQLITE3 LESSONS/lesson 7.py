import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

# How to update records in already created table

# This will change all records
# c.execute("""UPDATE people SET first_name = 'Bob'
#    WHERE last_name = 'Brylev'
#    """)

# You want to do that with ID

c.execute(""" UPDATE people SET first_name = 'Sergei'
    WHERE rowid = 2
    """)


conn.commit()

conn.close()