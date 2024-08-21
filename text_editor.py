from inquirer import *
import encryption
import sys
import os
import re

to_do_list = []
ogfile_path = input('where do you want your file to be :')
if re.match(r'^([\'"]).+\1', ogfile_path):
    file_path = ogfile_path[1:-1]
else:
    file_path = ogfile_path

to_do_list.append(file_path)
confirmation = ""
print('''
 _____ _            _               _                   _                 _ _ _                                   
|_   _| |          | |             | |                 | |               | (_) |                                  
  | | | |__   ___  | |__   ___  ___| |_    ___ ___   __| | ___    ___  __| |_| |_ ___  _ __    _____   _____ _ __ 
  | | | '_ \\ / _ \\ | '_ \\ / _ \\/ __| __|  / __/ _ \\ / _` |/ _ \\  / _ \\/ _` | | __/ _ \\| '__|  / _ \\ \\ / / _ \\ '__|
  | | | | | |  __/ | |_) |  __/\\__ \\ |_  | (_| (_) | (_| |  __/ |  __/ (_| | | || (_) | |    |  __/\\ V /  __/ |   
  \\_/ |_| |_|\\___| |_.__/ \\___||___/\\__|  \\___\\___/ \\__,_|\\___|  \\___|\\__,_|_|\\__\\___/|_|     \\___| \\_/ \\___|_|   

''')
while True:
    actionchoice = List("choice", message='what would you like to do?',
                        choices=["add some text", "read the file", "destroy the file", 'close the program',
                                 'encrypt the file', 'decrypt the file'])
    choice = prompt([actionchoice])
    print(choice['choice'])

    if choice['choice'] == 'add some text':
        add = input("add something to your list  :")
        to_do_list.append(add)
        with open(file_path, "a") as file:
            file.write(add)
    elif choice['choice'] == 'read the file':
        with open(file_path) as file:
            print(file.read())
    elif choice['choice'] == 'destroy the file':
        while len(confirmation) == 0:
            confirmation = input("are you sure you want to delete your list : Y/N :").upper()
        if confirmation == "Y":
            os.remove(file_path)  # very scary
        elif confirmation == "N":
            pass
    elif choice['choice'] == 'close the program':
        sys.exit(0)
    elif choice['choice'] == 'encrypt the file':
        encryption.file_encryption(file_path)
    elif choice['choice'] == 'decrypt the file':
        encryption.file_decryption(file_path)

