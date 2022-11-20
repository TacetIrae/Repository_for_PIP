def welcomig():
    print("Hello, and welcome to phone dictionary")

def input_data():
    first_name = input("Enter first name")
    last_name = input("Enter last name")
    phone_number = input("Enter telephone number")
    notes = input("Enter a note to the contact you are recording")
    return [first_name, last_name,phone_number,notes]

def export_data():
    with open('phone_dictionary.csv', 'r') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data

def import_data(data, sep=None):
    with open('phone_dictionary.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")


def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None

def print_data(data):
    if len(data) > 0:
        print("First Name".center(20), "Last Name".center(20), "Telephone".center(15), "Note".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
    else:
        print("Phone dictionary is empty")

def choice_sep():
    sep = input("Enter a separator: ")
    if sep == "":
        sep = None
    return sep

def choice():
    print("What do you need to do?:\n\
    1 - import;\n\
    2 - export;\n\
    3 - search for.")
    ch = input("Enter a number: ")
    if ch == '1':
        sep = choice()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Enter data for searching process: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Name".center(20), "Last name".center(20), "Telephone".center(15), "Note".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Data is not found")

