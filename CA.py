import socket
from Crypto import Random
from Crypto.PublicKey import RSA

rng1 = Random.new().read
RSAkey1 = RSA.generate(1024, rng1) #генерация последовательности дляключа

privatekey1 = RSAkey1 #генерация приватного ключа
publickey1 = RSAkey1.publickey() #генерация публичного ключа
f = open("privatekey1.pem", 'w') #запись в файл
f.write(str(privatekey1))
f.close()

f2 = open("publickey1.pem", 'w') #запись в файл
f2.write(str(publickey1))
f2.close()


rng2 = Random.new().read
RSAkey2 = RSA.generate(1024, rng2) #генерация для второй пары

privatekey2 = RSAkey2
publickey2 = RSAkey2.publickey()

f3 = open("privatekey2.pem", 'w') #запись в файл
f3.write(str(privatekey1))
f3.close()

f4 = open("publickey2.pem", 'w')
f4.write(str(publickey1))
f4.close()

mydict1 = {'Client': privatekey1.exportKey(), 'Server': publickey1.exportKey()}
mydict2 = {'Client': publickey2.exportKey(), 'Server': privatekey2.exportKey()}

CA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создание подключения
print("Socket created")

CA.bind(('localhost', 9999))
print("Socket bind complete")
CA.listen(5)
print("Server is now listening...")

while True: #проверки в ходе работы
    connection, address = CA.accept()
    print("Connected with " + address[0])

    user = connection.recv(1024)
    for name, key1 in mydict1.items():
        if name == user:
            connection.sendall(key1)
            print("key1 sended")
        else:
            print("Access denied!")
            connection.close()

    for name, key2 in mydict2.items():
        if name == user:
            connection.sendall(key2)
            print("key2 sended")
        else:
            print("Access denied!")
            connection.close()

    CA.close()
