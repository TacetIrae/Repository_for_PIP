

tutors = []
group = []

print("When you want to stop entering more names of the students, please enter 'stop' when a name is requested")
while True:
    name = None
    name = input("Enter a name of a student")
    if name == '':
        tutors.append('None')
    elif name.lower() == 'stop':
        break
    else:
        tutors.append(name)
    clas = None
    clas = input("Enter a class that this students is from")
    if clas == '':
        group.append('None')
    else:
        group.append(clas)

list_of_tuples = list(zip(tutors,group))
for i in list_of_tuples:
    print(i)
