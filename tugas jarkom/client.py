import socket
import time


host = socket.gethostname()
port = 8888

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((host,port))

nama = input('Masukkan Nama : ')
clientSocket.send(nama.encode())
print(clientSocket.recv(1024).decode())

while True:
    pertanyaan = clientSocket.recv(1024).decode()
    print(pertanyaan)
    waktuAwal = time.time()
    jawaban = input('Jawaban Anda : ')
    waktuAkhir = time.time()
    waktuMenjawab = waktuAkhir - waktuAwal
    if(waktuMenjawab<=10):
        clientSocket.send((nama+' ').encode())
        clientSocket.send((jawaban+' ').encode())
        clientSocket.send(str(waktuMenjawab).encode())    
    else:
        print('Timeout')
    hasil = clientSocket.recv(1024).decode()
    print(hasil+'\n')
