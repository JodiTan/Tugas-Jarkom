
import socket
import threading
import time


host = socket.gethostname()
port = 8888

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((host,port))

nama = input('Masukkan Nama : ')
clientSocket.send(nama.encode())
print(clientSocket.recv(1024).decode())

while True:
    timer = threading.Timer(10,()) 
    pertanyaan = clientSocket.recv(1024).decode()
    print(pertanyaan)
    waktuAwal = time.time()
    timer.start()
    jawaban = input('Jawaban Anda : ')
  #  while(timer.isAlive()):
    clientSocket.send(jawaban.encode())
    waktuAkhir = time.time()
    waktuMenjawab = waktuAkhir - waktuAwal
    clientSocket.send(str(waktuMenjawab).encode())
    #timer.cancel()
    
    hasil = clientSocket.recv(1024).decode()
    print(hasil)
