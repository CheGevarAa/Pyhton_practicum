import socket
import random
import math
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import hashlib

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #подключение к серверу

while True:
    server.connect(('localhost', 8080))

    ## Log in to server
    ID = input("Enter your ID: ")
    server.send(ID.encode())

    challenge = server.recv(1024)
    password = input("Enter your password: ")
    key = hashlib.sha256(password.encode()).digest()  # создание ключа из пароля
    IV = 16 * '\x00'
    encryptor = AES.new(key, AES.MODE_CFB, IV)
    response = encryptor.encrypt(challenge) # получение ответа
    ##print "Response:"+response
    server.send(response)
    ack = server.recv(1024)
    print(ack)
    if ack == "Incorrect password!": #проверка ответа от сервера
        break

    ###генерация ключа сессии
    g = 5
    p = 23
    server.send(str(g).encode())
    server.send(str(p).encode())

    a = 6
    print("secret value a:".encode() + str(a).encode()) #проверка создания части ключа
    A = (g ** a) % p  # g^a mod(p)
    server.send(str(A).encode())
    hashA = hashlib.sha256(str(A).encode()).digest()

    file = open("publickey1.pem", "r") #чтение из файла
    RSAkey1 = file.read()
    file.close()

    signA = RSAkey1.encode().encrypt(hashA, 32) #раскодирование
    server.send(signA[0])
    print("g:".encode() + str(g).encode())
    print("p:".encode() + str(p).encode())
    print("A:".encode() + str(A).encode())
    print("signA:".encode() + signA[0])
    print("Send g, p, g^a mod(p), sign(A) to Server".encode())

    file = open("privatekey2.pem", "r")#чтение файла
    RSAkey2 = file.read()
    file.close()
    RSAkey2 = RSA.importKey(RSAkey2)

    B = server.recv(1024)
    signB = server.recv(1024)
    print("Receive g^b mod(p), sign(B) from Server".encode())#вывод для проверки генерации и расшифровки
    print("B:".encode() + str(B).encode())
    print("signB".encode() + signB)

    hashB = hashlib.sha256(B).digest()
    checkHash = RSAkey2.decrypt(signB)
    print("hashB:".encode() + hashB)
    print("CheckHashB:".encode() + checkHash)

    if hashB == checkHash: #проверки правильности
        print("CheckHash Sucess!".encode())

        sessionKey = str((int(B) ** a) % p)
        print("Generate session key:".encode() + sessionKey)
    else:
        print("CheckHash Failed!".encode())
        break

    encryptedEMR = server.recv(1024)
    print("Recieve encrypted EMR from Server".encode())

    sessionKey = hashlib.sha256(sessionKey).digest() #расшифровка
    decryptor = AES.new(sessionKey, AES.MODE_CFB, IV)
    decryptedEMR = decryptor.decrypt(encryptedEMR)
    print("Decrypted EMR:".encode() + decryptedEMR)
    break
