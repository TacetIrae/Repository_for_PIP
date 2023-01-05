import sqlite3

def create_db():
    conn = sqlite3.connect('phone_library.db')
    conn.commit()
    conn.close()

def create_table():
    try:
        conn = sqlite3.connect('phone_library.db')
        c = conn.cursor()
        c.execute(f""" CREATE TABLE table_one(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name text,
        last_name text,
        age integer,
        phone_number text)""")
        print("Table is created")
    except sqlite3.Error:
        print("Failed to execute the command")
    finally:
        conn.commit()
        conn.close()

def insert_one_person():
    conn = sqlite3.connect('phone_library.db')
    c = conn.cursor()
    first_name = input("Enter first name of a person\n")
    last_name = input ("Enter last name of a person\n")
    age = int(input("Input persons age\n"))
    phone_number =input("Enter persons phone number\n")
    c.execute(f"INSERT INTO table_one (first_name, last_name, age, phone_number) VALUES ('{first_name}','{last_name}',{age},'{phone_number}')")
    conn.commit()
    conn.close()

def delete_one():
    conn = sqlite3.connect("phone_library.db")
    c = conn.cursor()
    deleteid = input("Enter an id of person you want to remove\n")
    c.execute(f"DELETE FROM table_one WHERE id = {deleteid}")
    conn.commit()
    conn.close()

def show_all():
    conn = sqlite3.connect("phone_library.db")
    c = conn.cursor()
    c.execute("SELECT * FROM table_one")
    item = c.fetchall()
    for i in item:
        print(i)
    conn.commit()
    conn.close()

def search_fuction():
    conn = sqlite3.connect("phone_library.db")
    c = conn.cursor()
    choice = input("Which method you want to use to search for information?\n"
                   "1.Search using id\n"
                   "2.Search using first name\n"
                   "3.Search using last name\n"
                   "4.Search using age\n")
    if choice == '1':
        id = input("Enter an id you want to look for\n")
        c.execute(f"SELECT * FROM table_one WHERE id = '{id}'")
        info = c.fetchall()
        for i in info:
            print(i)

    elif choice == '2':
        func = input("There are multiple ways to search for information this way\n"
                     "1. If you know full first name\n"
                     "2. If you know only few words\n")
        if func == '1':
            name = input("Enter a name you want to search for\n")
            c.execute(f"SELECT * FROM table_one WHERE first_name = '{name}'")
            info = c.fetchall()
            for i in info:
                print(i)

        elif func == '2':
            name = input("Enter a letters you want to search for in first names of people in database\n"
                         "To use this function, please enter either *letters*% or %letters\n"
                         "'%' identifies if there are more letter later or beforehand\n")
            c.execute(f"SELECT * FROM table_one WHERE first_name LIKE '{name}'")
            info = c.fetchall()
            for i in info:
                print(i)
        else:
            print("This function does not exist")
    elif choice == '3':
        func = input("There are multiple ways to search for information this way\n"
                     "1. If you know full last name\n"
                     "2. If you know only few words\n")
        if func == '1':
            name = input("Enter last name  you want to search for\n")
            c.execute(f"SELECT * FROM table_one WHERE last_name = '{name}'")
            info = c.fetchall()
            for i in info:
                print(i)

        elif func == '2':
            name = input("Enter a letters you want to search for in last names of people in database\n"
                         "To use this function, please enter either *letters*% or %letters\n"
                         "'%' identifies if there are more letter later or beforehand\n")
            c.execute(f"SELECT * FROM table_one WHERE last_name LIKE '{name}'")
            info = c.fetchall()
            for i in info:
                print(i)
        else:
            print("This function does not exist")
    elif choice == '4':
        func = input("There are 3 options of search you can choose here\n"
                     "1. You know exact age of someone you are looking for\n"
                     "2. You want to look for someone of certain age and older\n"
                     "3. You want to look for someone of certain age and younger\n")
        if func == '1':
            age_s = int(input("Enter exact age you are looking for\n"))
            c.execute(f"SELECT * FROM table_one WHERE age = {age_s}")
            info = c.fetchall()
            for i in info:
                print(i)

        elif func == '2':
            age_s = int(input("Enter minimum age you want to search for\n"))
            c.execute(f"SELECT * FROM table_one WHERE age >= {age_s}")
            info = c.fetchall()
            for i in info:
                print(i)

        elif func == '3':
            age_s = int(input("Enter maximum age you want to search for\n"))
            c.execute(f"SELECT * FROM table_one WHERE age <= {age_s}")
            info = c.fetchall()
            for i in info:
                print(i)
        else:
            print("This function does not exist")
    else:
        print("This function does not exist")
    conn.close()

def update_info():
    conn = sqlite3.connect('phone_library.db')
    c = conn.cursor()
    id_toChange = input("Which id you want to change?")
    choice = input("What do you want to change?\n"
                   "1.Change first name\n"
                   "2.Change last name\n"
                   "3.Change age\n"
                   "4.Change phone number\n")
    if choice == '1':
        name = input("Enter a name you want it to be replaced with")
        c.execute(f""" UPDATE table_one SET first_name = '{name}'
            WHERE id = {id_toChange}
            """)
    elif choice == '2':
        last_name = input("Enter last name you want to replace it with")
        c.execute(f""" UPDATE table_one SET last_name = '{last_name}' 
            WHERE id = {id_toChange}
            """)
    elif choice == '3':
        age = int(input("Enter new age"))
        c.execute(f""" UPDATE table_one SET age = {age} 
            WHERE id = {id_toChange}
            """)
    elif choice == '4':
        phone = input("Enter new telephone number")
        c.execute(f""" UPDATE table_one SET phone_number = '{phone}' 
            WHERE id = {id_toChange}
            """)
    else:
        print("This function does not exist")
    conn.commit()
    conn.close()
