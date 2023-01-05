import controller as con


def choice():
    while True:
        function = int(input("There are following functions in the database:\n"
                             "1.Insert one person\n"
                             "2.Show all records\n"
                             "3.Delete one record\n"
                             "4.Search for information\n"
                             "5.Update information in database\n"
                             "If you want to stop the program enter 6\n"))
        if function == 1:
            con.insert_one_person()
        elif function ==2:
            con.show_all()
        elif function == 3:
            con.delete_one()
        elif function == 4:
            con.search_fuction()
        elif function == 5:
            con.update_info()
        elif function == 6:
            break
        else:
            print("Following command does not exist")



def starting():
    start = input("If you started this program for the first time, answer yes.\n"
                  "This will initialize creation of the database\n"
                  " Answer no if you already had created database\n"
                  " Answer Y/N\n").lower()
    if start == 'y' or start == 'yes':
        con.create_db()
        print("Database is created")
        con.create_table()
        choice()
    elif start == 'n' or start == 'no':
        print("If your database is already created, than lets start with options you have")
        choice()
    else:
        print("Incorrect input\n"
              "Please try again")
        starting()


print("This is phone library database program")
starting()
