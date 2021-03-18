import platform
"""
Главный файл, он же файл запуска всего этого добра
1. Тут написаны сообщения для пользователя, плюс предлагается выбрать в каком менеджере он хочет работать
2. Весь файл - работа с одним вводом, который отвечает за выбор ОС
3. После ввода идет считывание, а вместе с ним и выполнение того файла, который нужен пользователю
4. Контроль за правильным запуском идет через функцию platform.system(), оно вытаскивает название текущей ОС
5. Если пользователь в выборке ввел не то, будет ошибка
"""
print('Welcome\n')
print('Choose OS to work with:\n')
print('1.Windows')
print('2.Linux OS\n')

while True:
    result = input("Choose one of the following: ")
    if result == '1':
        if platform.system() == "Windows":
            exec(open("falemanage.py").read())
            break
        else:
            print("You are not in Windows")
    elif result == '2':
        if platform.system() == "Linux":
            exec(open("linuxmanager.py").read())
            break
        else:
            print("You are not in Linux")
    else:
        print("Wrong input")
