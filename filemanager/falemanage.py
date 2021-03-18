import os
import shutil
import send2trash

print('Welcome to the python-file-manager\n')

list_of_commands = ["1", "2", "3", "4", "5", "6", "exit"]
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]


def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)


while True:
    print("1.Open files/folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n6.Create files\nexit")
    result = input("Choose one of the following: ")
    if result == '1':
        # Home Screen
        print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')
        print('Drives: ')
        for x in range(len(drives)):
            print(str(5 + x) + '. ' + drives[x])
        while True:
            inp = input("\nEnter your Choice: ")
            if inp == '1':
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break
            elif inp == '2':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break
            elif inp == '3':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break
            elif inp == '4':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break
            elif inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct input / drive name.\n')
        while True:
            listDirectories()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            res = input('\nChoose a file/folder: ')
            print('\n')
            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    os.system('"' + res + '"')
                else:
                    os.chdir(res)
            elif res == 'exit':                          # Exit command to exit from loop
                break
            elif res == 'back':                          # Back command to go up one directory
                os.chdir('..')
            else:
                print('No file/folder exist of this name.')
    if result == '2':
        print("You chose to rename")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])
        while True:
            inp = input("\nEnter your Choice: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')
        while True:
            listDirectories()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            print('Type "rename" to rename this directory')
            res = input('\nChoose a file to rename: ')
            print('\n')
            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    new_name = input("Enter a new name: ")
                    ogDir = res
                    newDir = os.getcwd() + '\\' + new_name
                    shutil.move(ogDir, newDir)
                else:
                    os.chdir(res)
            elif res == 'exit':    # Exit command to exit from loop
                break
            elif res == 'back':    # Back command to go up one directory
                os.chdir('..')
            elif res == 'rename':  # Rename command to delete one directory
                new_name = input("Enter a new name: ")
                ogDir = os.getcwd()
                os.chdir('..')
                newDir = os.getcwd() + '\\' + new_name
                shutil.move(ogDir, newDir)
            else:
                print('No file/folder exist of this name.')
    if result == '3':
        print("You chose to move")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])
        while True:
            inp = input("\nEnter your Choice: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')
        while True:
            listDirectories()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            print('Type "cut" to move this directory')
            res = input('\nChoose a file to move: ')
            print('\n')
            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("\nMove " + res + " to a desired location.")
                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])
                        inp2 = input("\nEnter your Choice: ")
                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a correct drive name.\n')
                    while True:
                        listDirectories()
                        print('Type "paste" to paste this file in current directory')
                        res2 = input('\nChoose a file to move: ')
                        print('\n')
                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")
                            else:
                                os.chdir(res2)
                        elif res2 == 'paste':
                            shutil.move(og_path, os.getcwd())
                            break
                else:
                    os.chdir(res)
            elif res == 'exit':     # Exit command to exit from loop
                break
            elif res == 'back':                          # Back command to go up one directory
                os.chdir('..')
            elif res == 'cut':
                og_path = os.getcwd()
                print("Moving the current directory")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])
                    inp2 = input("\nEnter your Choice: ")
                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')
                while True:
                    listDirectories()
                    print('\nType "pasteManager" to paste this folder in current directory')
                    res2 = input('\nChoose a folder to open: ')
                    print('\n')
                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")
                        else:
                            os.chdir(res2)
                    elif res2 == 'paste':
                        shutil.move(og_path, os.getcwd())
                        break
            else:
                print('No file/folder exist of this name.')
    if result == '4':
        print("You chose to copy")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])
        while True:
            inp = input("\nEnter your Choice: ")
            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct drive name.\n')
        while True:
            listDirectories()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "backM" to go up one directory.')
            print('Type "copy" to copy this directory')
            res = input('\nChoose a file to copy: ')
            print('\n')
            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("Move " + res + " to a desired location.")
                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])
                        inp2 = input("\nEnter your Choice: ")
                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a correct drive name.\n')
                    while True:
                        listDirectories()
                        print('Type "paste" to copy this file in current directory')
                        res2 = input('\nChoose a file to move: ')
                        print('\n')
                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")
                            else:
                                os.chdir(res2)
                        elif res2 == 'paste':
                            shutil.copy(og_path, os.getcwd())
                            break
                else:
                    os.chdir(res)
            elif res == 'exit':  # Exit command to exit from loop
                break
            elif res == 'back':  # Back command to go up one directory
                os.chdir('..')
            elif res == 'copy':
                og_path = os.getcwd()
                print("Copying the current directory")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])
                    inp2 = input("\nEnter your Choice: ")
                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')
                while True:
                    listDirectories()
                    print('\nType "pasteManager" to copy this file in current directory')
                    res2 = input('\nChoose a folder to open: ')
                    print('\n')
                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")
                        else:
                            os.chdir(res2)
                    elif res2 == 'paste':
                        print(og_path)
                        folder_name = og_path.split('\\')[-1]
                        folder_directory = os.getcwd() + '\\' + folder_name
                        shutil.copytree(og_path, folder_directory)
                        break
            else:
                print('No file/folder exist of this name.')
    if result == '5':
        while True:
            # Options to delete files/folders to permanently or otherwise
            print('\n1. Permanently \n2. Recycle Bin')
            query = input('Would you like to permanently delete or send to Recycle Bin?: ')
            if query == '1':
                print('You chose to permanently delete files/folders.\n')
                print('Drives: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])
                while True:
                    inp = input("\nEnter your Choice: ")
                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')
                while True:
                    listDirectories()
                    print('\n\nType "exit" to exit from file manager.')
                    print('Type "back" to go up one directory.')
                    print('Type "delete" to permanently delete this directory')
                    res = input('\nChoose a file to delete: ')
                    print('\n')
                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            # Warning to prevent unnecessary deletion
                            print('Are you sure you want to permanently delete this file? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                os.unlink(res)
                        else:
                            os.chdir(res)
                    elif res == 'exit':                      # Exit command to exit from loop
                        break
                    elif res == 'back':                      # Back command to go up one directory
                        os.chdir('..')
                    elif res == 'delete':                    # Delete command to delete one directory
                        # Warning to prevent unnecessary deletion
                        print('Are you sure you want to permanently delete this folder? (YES/NO)')
                        ans = input('Yes or No: ')
                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            shutil.rmtree(path)
                    else:
                        print('No file/folder exist of this name.')
            elif query == '2':
                print('You chose to temporarily delete files/folders.')
                print('Drives: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])
                while True:
                    inp = input("\nEnter your Choice: ")
                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a correct drive name.\n')
                while True:
                    listDirectories()
                    print('\n\nType "exit" to exit from file manager.')
                    print('Type "back" to go up one directory.')
                    print('Type "delete" to send this directory to recycle bin')
                    res = input('\nChoose a file to delete: ')
                    print('\n')
                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            # Warning to prevent unnecessary deletion
                            print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                send2trash.send2trash(res)
                        else:
                            os.chdir(res)
                    elif res == 'exit':  # Exit command to exit from loop
                        break
                    elif res == 'back':  # Back command to go up one directory
                        os.chdir('..')
                    elif res == 'delete':  # Delete command to delete one directory
                        # Warning to prevent unnecessary deletion
                        print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                        ans = input('Yes or No: ')
                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            send2trash.send2trash(path)
                    else:
                        print('No file/folder exist of this name.')
            else:
                print('You chose wrong number')
    if result == '6':
        print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')
        print('Drives: ')
        for x in range(len(drives)):
            print(str(5 + x) + '. ' + drives[x])
        while True:
            inp = input("\nEnter your Choice: ")
            if inp == '1':
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break
            elif inp == '2':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break
            elif inp == '3':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break
            elif inp == '4':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break
            elif inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct input / drive name.\n')
        while True:
            listDirectories()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            res = input('\nChoose a folder or create now: ')
            if res in os.listdir(os.getcwd()):
                os.chdir(res)
                check_create = input("If you want to create file, write down filename:")
                if check_create == "exit":
                    break
                else:
                    os.system("copy nul " + check_create + " > nul")
            elif res == 'exit':  # Exit command to exit from loop
                break
            elif res == 'back':  # Back command to go up one directory
                os.chdir('..')
            elif res == "now":
                check_create = input("If you want to create file, write down filename:")
                if check_create == "exit":
                    break
                else:
                    os.system("copy nul " + check_create + " > nul")
            else:
                print('No folder exist of this name.')
    if result == "exit":
        break
    if not (result in list_of_commands):
        print("Wrong input")
