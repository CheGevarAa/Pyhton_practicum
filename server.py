import socket
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import hashlib


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создание сервера
print("Socket created")
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('localhost', 8080)) #развертывание сервера
print("Socket bind complete")
server.listen(5)
print("Server is now listening...")

while True: #процесс работы сервера
    connection, address = server.accept()#узнаем кто подключился
    print("Connected with " + address[0])

    ## вход на сервер
    data = connection.recv(1024)

    challenge = Random.new().read(16)
    connection.sendall(challenge)

    response = connection.recv(1024)#получение ответа
    password = "Abc1234" #пароль на вход
    key = hashlib.sha256(password.encode()).digest()
    IV = 16 * '\x00'
    decryptor = AES.new(key, AES.MODE_CFB, IV) #расшифровка с клиента
    plain = decryptor.decrypt(response)

    if plain == challenge: #проверка входа на сервер
        connection.sendall("Welcome!".encode())
        print("Client logged in".encode())
    else:
        connection.sendall("Incorrect password!".encode())
        break

    ## генерация кдюча сессии
    g = connection.recv(1024)
    p = connection.recv(1024)
    A = connection.recv(1024)
    signA = connection.recv(1024)
    print("Recieve g, p, g^a mod(p), sign(A) from Client".encode())
    print("g:".encode() + str(g).encode())
    print("p:".encode() + str(p).encode())
    print("A:".encode() + str(A).encode())
    print("signA:".encode() + signA)

    file = open("privatekey1.pem", "r") #чтение файла
    RSAkey1 = file.read()
    file.close()
    RSAkey1 = RSA.importKey(RSAkey1)

    checkHash = RSAkey1.decrypt(signA) #проверка ключа
    hashA = hashlib.sha256(A).digest()

    file = open("publickey2.pem", "r") #чтение файла
    RSAkey2 = file.read()
    file.close()
    RSAkey2 = RSA.importKey(RSAkey2)

    print("hashA:" + hashA)
    print("CheckHashA:" + checkHash)

    if hashA == checkHash: #проверка контрольной суммы
        print
        "CheckHash Success!"

        b = 15
        B = (int(g) ** b) % int(p)
        print("secret value b:" + str(b))

        hashB = hashlib.sha256(str(B)).digest() #отправка клиенту ключа
        signB = RSAkey2.encrypt(hashB, 32)
        connection.sendall(str(B))
        connection.sendall(signB[0])
        print("B:" + str(B))
        print("signB:" + signB[0])
        print("Send g^b mod(p), sign(B) to Client")

        sessionKey = str((int(A) ** b) % int(p))
        print("Generate session key:" + sessionKey)
    else:
        print("CheckHash failed!")
        break

    file = open("EMR.txt", "r") #чтение файла
    EMRfile = file.read()
    file.close()

    sessionKey = hashlib.sha256(sessionKey).digest()
    encryptor = AES.new(sessionKey, AES.MODE_CFB, IV)
    encryptedEMR = encryptor.encrypt(EMRfile)

    connection.send(encryptedEMR)
    print("Send encrypted EMR to Client")
    print("Encrypted file:" + encryptedEMR)
    break

connection.close()
server.close()
