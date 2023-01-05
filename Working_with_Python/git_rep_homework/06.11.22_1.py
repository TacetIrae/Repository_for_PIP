my_file = open("text.txt","w+")
my_file.write("Hello file, I'm abc")
my_file.close()


with open('text.txt') as f1, open('text_out.txt', 'w') as f2:
    f2.write(''.join(i for i in f1.read() if i not in 'abc'))