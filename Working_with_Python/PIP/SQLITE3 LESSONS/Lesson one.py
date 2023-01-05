import sqlite3

# Process of creating database and creating table

# creating a database
conn = sqlite3.connect("database.db")

# Creating a cursor
c = conn.cursor()

# Creating a table
c.execute(""" CREATE TABLE people (
    first_name text,
    last_name text,
    email text 
)""")

# Data types of sqlite3:
# Null, Integer, Real, Text, Blob
# Null - does or doesnt exist
# Integer - whole number
# Real - decimal number
# Text - just text
# Blob - images, mp3.


# Next step is to commit connection to save
conn.commit()

# Close connection
conn.close()
