import socket
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
        connection.se
    connection.close()

#start = 0

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
#    check = input('Start ? (y/n) : ')
#    if(check == 'y'):
#        connection.
#       start = 1
#        break

#soal = 1
#if(start == 1):
#    question = 'Pertanyaan 1 : blablablablabla\\ a. a \\b. b \\c. c \\d. d'
#    connection.send(quesntion[soal].encode())
#    soal = soal+1
ServerSocket.close()